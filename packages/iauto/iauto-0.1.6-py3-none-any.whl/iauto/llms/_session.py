import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Union

from .._logging import get_logger
from ..actions import Action
from ._llm import LLM, ChatMessage


class Session:
    def __init__(self, llm: LLM, actions: Optional[List[Action]] = None) -> None:
        self._log = get_logger("LLM")
        self._llm = llm
        self._actions = actions
        self._messages = []

    def add(self, message: ChatMessage):
        self._messages.append(message)

    @property
    def llm(self) -> LLM:
        return self._llm

    @property
    def messages(self) -> List[ChatMessage]:
        return self._messages

    @property
    def actions(self) -> List[Action]:
        return self._actions or []

    def _execute_tools(
        self,
        message: ChatMessage,
        history: List[ChatMessage],
        actions: List[Action],
        save_message: bool = True,
        **kwargs
    ) -> ChatMessage:
        if message.tool_calls is None or len(message.tool_calls) == 0:
            return message

        functions = dict([(func.spec.name.replace(".", "_"), func) for func in actions])

        if message.tool_calls and len(message.tool_calls) > 0:
            tool_call = message.tool_calls[0]
            if not tool_call.function:
                raise ValueError(f"Invalid function: {tool_call.function}")

            call_id = tool_call.id
            func_name = tool_call.function.name
            func_args = tool_call.function.arguments or '{}'

            if func_name not in functions:
                raise ValueError(f"Function not found: {func_name}")

            func_to_call = functions[func_name]

            func_resp = None
            try:
                func_args = json.loads(func_args)
                func_resp = func_to_call(**func_args)
            except Exception as e:
                self._log.warn(f"Function call err: {e}, func_name={func_name}, args={func_args}, resp={func_resp}")
                func_resp = str(e)

            if func_resp is not None and not isinstance(func_resp, str):
                try:
                    func_resp = json.dumps(func_resp or {}, ensure_ascii=False, indent=4)
                except TypeError:
                    self._log.warn("Function return values cannot be JSONized")

            if save_message:
                self.add(message=message)

            if call_id is None:
                raise ValueError("tool_call_id required.")
            m = ChatMessage(
                role="tool",
                content='\n'.join(func_resp or f"{func_name} return nothing."),
                tool_call_id=call_id,
                name=func_name,
            )
            return m
        else:
            return message

    def run(
        self,
        instructions: Optional[str] = None,
        messages: Optional[List[ChatMessage]] = None,
        history: int = 5,
        rewrite: bool = False,
        expect_json: int = 0,
        tools: Optional[List[Action]] = None,
        use_tools: bool = True,
        auto_exec_tools: bool = True,
        **kwargs
    ) -> Union[ChatMessage, Dict]:
        if rewrite:
            self.rewrite(history=history, **kwargs)

        if messages is None or len(messages) == 0:
            messages = self._messages[-1 * history:]
        if instructions is not None:
            messages.insert(0, ChatMessage(role="system", content=instructions))

        tools_spec = None
        if use_tools:
            if tools:
                tools_spec = [t.spec for t in tools]
            elif self._actions:
                tools_spec = [t.spec for t in self._actions]
        m = self._llm.chat(messages=messages, tools=tools_spec, **kwargs)
        if auto_exec_tools:
            m = self._execute_tools(message=m, history=messages, actions=tools or self._actions or [], **kwargs)

        json_obj = None
        if expect_json > 0:
            for i in range(expect_json):
                try:
                    json_obj = json.loads(m.content)
                    break
                except json.JSONDecodeError:
                    m = self._llm.chat(messages=messages, tools=tools_spec, **kwargs)
                    if auto_exec_tools:
                        m = self._execute_tools(
                            message=m,
                            history=messages,
                            actions=tools or self._actions or [],
                            **kwargs
                        )
            if json_obj is None:
                m.content = "{}"

        self.add(m)

        if json_obj:
            return json_obj
        else:
            return m

    def react(
        self,
        instructions: Optional[str] = None,
        messages: Optional[List[ChatMessage]] = None,
        history: int = 5,
        rewrite: bool = False,
        log=False,
        max_steps=3,
        tools: Optional[List[Action]] = None,
        use_tools: bool = True,
        auto_exec_tools: bool = True,
        **kwargs
    ) -> ChatMessage:
        """Ref : https://www.width.ai/post/react-prompting"""

        if messages is None or len(messages) == 0:
            messages = self._messages[-1 * history:]

        if len(messages) < 1 and messages[-1].role != "user":
            return ChatMessage(role="assistant", content="Ask me a question.")

        tools_spec = None
        if use_tools:
            if tools:
                tools_spec = [t.spec for t in tools]
            elif self._actions:
                tools_spec = [t.spec for t in self._actions]

        original_question = messages[-1].content
        question = original_question
        if rewrite:
            self.rewrite(history=history, **kwargs)
            question = messages[-1].content

        if instructions is None:
            instructions = ""

        primary_prompt = """{instructions}
Solve a question answering task with interleaving Thought, Action, Observation steps.

Thought can reason about the current situation, and Action can be two types:
(1) Generate[entity], which use tools to generate an obersvation.
(2) Finish[answer], which returns the answer and finishes the task.

Use the following format:

Task: the task you must solve
Thought: you should always think about what to do
Action: Generate["the action to take"]
Observation: the result of the action
... (this Thought/Action/Observation can be repeated zero or more times)
Thought: I now know the final answer
Action: Finish["the final answer to the original input question"]

Refer to the conversation hisotry to help you understand the task.

Begin!

Task: {task}
{steps}
        """
        THOUGHT = "Thought: "
        ACTION = "Action: "
        OBSERVATION = "Observation: "

        if log:
            self._log.info(f"Task: {question}")

        anwser = ChatMessage(role="assistant", content="NOT ENOUGH INFO")

        # Generate steps
        action_pattern = re.compile(r'Generate\[(.+?)\]')
        steps = []
        finished = False
        anwser_found = False

        def _save_step(s):
            steps.append(s)
            if log:
                self._log.info(s)

        steps_count = 0
        while not finished and steps_count < max_steps:
            prompt = primary_prompt.format(
                task=question,
                steps="\n".join(steps),
                instructions=instructions
            )

            m = self._llm.chat(messages=messages + [ChatMessage(role="user", content=prompt)], **kwargs)

            content = m.content
            ss = content.split("\n")

            for s in ss:
                s = s.strip()
                if s.startswith(OBSERVATION):
                    break  # drop observation and followed generated by LLM

                if s.startswith(ACTION):
                    _save_step(s)
                    if "Finish" in s:
                        finished = True
                        anwser_pattern = re.compile(r'Finish[(.*)]')
                        founds = anwser_pattern.findall(s)
                        if len(founds) > 0:
                            found = founds[0]
                            found = found.lstrip('"').rstrip('"')
                            anwser.content = found
                            anwser_found = True
                        break
                    else:
                        actions = action_pattern.findall(s)
                        new_obversation = False
                        for action in actions:
                            m = self._llm.chat(messages=[
                                ChatMessage(role="user", content=action)
                            ], tools=tools_spec)

                            if auto_exec_tools:
                                m = self._execute_tools(
                                    message=m,
                                    history=messages,
                                    actions=tools or self._actions or [],
                                    save_message=False,
                                    **kwargs
                                )

                            o_content = m.content.replace("\n", " ")
                            observation = f"Observation: {o_content}"
                            _save_step(observation)
                            new_obversation = True
                        if not new_obversation:
                            observation = "Observation: NOTHING. Think again:\n"
                            _save_step(observation)
                elif s.startswith(THOUGHT):
                    _save_step(s)

            steps_count += 1
            if steps_count > max_steps:
                _save_step("Thought: No enough infomation to solve this task, i have to give up.")
                _save_step("Action: Finish[NOT ENOUGH INFO]")

        final_anwser_prompt = """{instructions}
Please answer the final user question based on the following thought steps.

Task: {task}
Thought Steps:
```
{steps}
```

Final question: {question}
Your Answer:"""
        if not anwser_found:
            prompt = final_anwser_prompt.format(
                task=question,
                steps="\n".join(steps),
                question=original_question,
                instructions=instructions
            )
            messages.append(ChatMessage(role="user", content=prompt))
            anwser = self._llm.chat(messages=messages, **kwargs)

        content = anwser.content
        if content:
            z = content.rfind('\nFinal Answer: ')
            if z >= 0:
                content = content[z + len('\nFinal Answer: '):]

            anwser.content = content.replace("Final", "").replace("Answer:", "").replace("Thought:", "")
        self.add(anwser)
        return anwser

    def rewrite(self, history: int = 5, **kwargs):
        instructions = """
Rewrite the following user question into a clearer and more complete question based on the context of the conversation.

Conversation:
```
{conversation}
```

Question: {question}
Rewrite as:
        """

        if len(self._messages) < 1 or self._messages[-1].role != "user":
            return

        messages = self._messages[-1 * history:-1]
        plain = self.plain_messages(messages=messages)
        instructions = instructions.format(
            conversation=plain, question=self._messages[-1].content, datetime=datetime.now())

        m = self._llm.chat(messages=[ChatMessage(role="user", content=instructions)], **kwargs)
        self._messages[-1].content = m.content

    def plain_messages(self, messages: List[ChatMessage], norole=False, nowrap=False):

        plain = []
        for m in messages:
            role = "" if norole else f"{m.role}: "
            content = m.content if not nowrap else m.content.replace("\n", "\\n")
            plain.append(f"{role}{content}")
        return "\n".join(plain)
