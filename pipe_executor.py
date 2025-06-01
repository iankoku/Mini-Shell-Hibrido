
import shlex
from pipe_ops import sim_echo, sim_cat, sim_sort, sim_head

def execute_pipeline(command_line: str) -> None:
    stages = [stage.strip() for stage in command_line.split('|')]
    input_text = None
    for stage in stages:
        if not stage:
            continue
        args = shlex.split(stage)
        if not args:
            continue
        cmd, *rest = args
        match cmd:
            case "echo":
                input_text = sim_echo(rest, input_text)
            case "cat" | "type":
                input_text = sim_cat(rest, input_text)
            case "sort":
                input_text = sim_sort(rest, input_text)
            case "head":
                input_text = sim_head(rest, input_text)
            case _:
                print(f"Comando no soportado en pipe: {cmd}")
                return
    if input_text:
        print(input_text, end="")
