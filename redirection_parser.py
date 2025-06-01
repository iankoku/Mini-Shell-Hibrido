
import shlex

def parse_redirection(command: str):
    tokens = shlex.split(command)
    cmd = []
    input_file = None
    output_file = None
    append = False
    it = iter(tokens)
    for token in it:
        if token == '>':
            output_file = next(it, None)
        elif token == '>>':
            output_file = next(it, None)
            append = True
        elif token == '<':
            input_file = next(it, None)
        else:
            cmd.append(token)
    return {
        'cmd': cmd,
        'input_file': input_file,
        'output_file': output_file,
        'append': append
    }
