import json
from types import SimpleNamespace

from autogen import ModelClient
from typing_extensions import Dict, Optional

from iauto.llms import ChatMessage, Session

from .. import log


class IASessionClient(ModelClient):
    def __init__(
        self,
        config,
        session: Session,
        react: Optional[bool] = False,
        llm_args: Optional[Dict] = None,
        **kwargs
    ) -> None:
        self._model = config.get("model")
        self._session = session
        self._react = react
        self._llm_args = llm_args or {}

        self._log = log.get_logger("IASessionClient")

    def create(self, params):
        if self._log.isEnabledFor(log.DEBUG):
            self._log.debug(json.dumps(params, indent=4, ensure_ascii=False))
        resp = SimpleNamespace()
        resp.choices = []
        resp.model = self._model
        messages = []

        for m in params.get("messages") or []:
            messages.append(ChatMessage(
                role=m["role"],
                content=m["content"] or "",
                tool_call_id=m.get("tool_call_id"),
                name=m.get("name"),
                tool_calls=m.get("tool_calls")
            ))

        tool_calls = params.get("tools") or []
        use_tools = len(tool_calls) > 0

        if self._react:
            m = self._session.react(messages=messages, use_tools=use_tools, auto_exec_tools=False, **self._llm_args)
        else:
            m = self._session.run(messages=messages, use_tools=use_tools, auto_exec_tools=False, **self._llm_args)
        if self._log.isEnabledFor(log.DEBUG):
            self._log.debug(json.dumps(m.model_dump(), indent=4, ensure_ascii=False))

        choice = SimpleNamespace()
        choice.message = SimpleNamespace()
        choice.message.role = m.role
        choice.message.content = m.content
        choice.message.tool_calls = None
        if m.tool_calls:
            choice.message.tool_calls = [t.model_dump() for t in m.tool_calls]
            # for tool_call in choice.message.tool_calls:
            #    tool_call["function"]["arguments"] = json.dumps(tool_call["function"]["arguments"], ensure_ascii=False)

        resp.choices.append(choice)

        return resp

    def message_retrieval(self, response):
        choices = response.choices

        messages = []
        has_tool_calls = False
        for choice in choices:
            tool_calls = choice.message.tool_calls
            if tool_calls:
                has_tool_calls = True
            messages.append({
                "role": choice.message.role,
                "content": choice.message.content,
                "tool_calls": tool_calls
            })

        if not has_tool_calls:
            messages = [c.message.content for c in choices]
        return messages

    def cost(self, response) -> float:
        response.cost = 0
        return 0

    @staticmethod
    def get_usage(response) -> Dict:
        return {}
