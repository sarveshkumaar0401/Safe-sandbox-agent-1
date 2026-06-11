from agent import agent
from executor import execute_code
from file_tools import save_result, read_report

@agent.tool_plain
def run_python(code: str) -> str:
    return execute_code(code)

@agent.tool_plain
def save_text(content: str) -> str:
    return save_result(content)

@agent.tool_plain
def show_report() -> str:
    return read_report()