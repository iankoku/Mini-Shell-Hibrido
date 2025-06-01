
from pipe_executor import execute_pipeline
from sys_ops import execute_sys_command
from redirection_parser import parse_redirection
from pipe_ops import sim_echo, sim_cat, sim_sort, sim_head

def execute_command(command: str) -> None:
    if '|' in command:
        execute_pipeline(command)
    elif '>' in command or '>>' in command or '<' in command:
        parsed = parse_redirection(command)
        cmd = parsed['cmd']
        input_file = parsed['input_file']
        output_file = parsed['output_file']
        append = parsed['append']
        if not cmd:
            print("Error: comando vacío tras analizar redirección.")
            return
        base_cmd = cmd[0]
        args = cmd[1:]
        input_text = None
        if input_file:
            try:
                with open(input_file, "r") as f:
                    input_text = f.read()
            except FileNotFoundError:
                print(f"No se encontró el archivo de entrada: {input_file}")
                return
        match base_cmd:
            case "echo":
                result = sim_echo(args, input_text)
            case "cat" | "type":
                result = sim_cat(args, input_text)
            case "sort":
                result = sim_sort(args, input_text)
            case "head":
                result = sim_head(args, input_text)
            case _:
                print(f"Comando no soportado con redirección: {base_cmd}")
                return
        if output_file:
            mode = "a" if append else "w"
            try:
                with open(output_file, mode) as f:
                    f.write(result)
            except Exception as e:
                print(f"Error al escribir en {output_file}: {e}")
        else:
            print(result, end="")
    else:
        execute_sys_command(command)
