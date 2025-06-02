
import shlex
from pipe_ops import sim_echo, sim_cat, sim_sort, sim_head

def execute_pipeline(command_line: str) -> None:
    # Detectar redirección al final del pipeline
    output_file = None
    append = False
    if '>>' in command_line:
        command_line, output_file = command_line.rsplit('>>', 1)
        output_file = output_file.strip()
        append = True
    elif '>' in command_line:
        command_line, output_file = command_line.rsplit('>', 1)
        output_file = output_file.strip()

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
        if output_file:
            mode = "a" if append else "w"
            try:
                with open(output_file, mode) as f:
                    f.write(input_text)
            except Exception as e:
                print(f"Error al escribir en archivo: {output_file} -> {e}")
        else:
            print(input_text, end="")
