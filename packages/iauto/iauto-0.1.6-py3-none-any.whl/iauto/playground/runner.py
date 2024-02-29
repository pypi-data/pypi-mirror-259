import os
import sys

from streamlit.web.cli import main as streamlit_main


def run(app, playbook_dir=None):
    here = os.path.dirname(__file__)
    app_py = os.path.join(here, f"{app}.py")

    if playbook_dir is None:
        playbook_dir = os.getcwd()

    os.environ["IA_PLAYBOOK_DIR"] = playbook_dir

    # cmd = f"streamlit run {app_py}"
    # os.system(cmd)

    sys.argv = ["streamlit", "run", f"{app_py}"]
    streamlit_main()
