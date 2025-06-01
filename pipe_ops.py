def sim_echo(args, input_text=None):
    return " ".join(args) + "\n"

def sim_cat(args, input_text=None):
    output = ""
    if input_text:
        output += input_text
    for fname in args:
        try:
            with open(fname, "r") as f:
                output += f.read()
        except FileNotFoundError:
            output += f"[Archivo no encontrado: {fname}]\n"
    return output

def sim_sort(args, input_text=None):
    if not input_text:
        return ""
    lines = input_text.splitlines()
    lines.sort()
    return "\n".join(lines) + "\n"

def sim_head(args, input_text=None):
    if not input_text:
        return ""
    n = 10
    if args and args[0] == "-n" and len(args) > 1:
        try:
            n = int(args[1])
        except ValueError:
            pass
    lines = input_text.splitlines()
    return "\n".join(lines[:n]) + "\n"
