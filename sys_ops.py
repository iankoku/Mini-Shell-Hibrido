import shlex
import os

def execute_sys_command(command: str) -> None:
    try:
        args = shlex.split(command)
        if not args:
            return
        cmd, *rest = args

        match cmd:
            case "ls" | "dir":
                path = rest[0] if rest else "."
                try:
                    for entry in os.listdir(path):
                        print(entry)
                except FileNotFoundError:
                    print(f"No existe el directorio: {path}")

            case "cd":
                if not rest:
                    print(os.getcwd())
                else:
                    try:
                        os.chdir(rest[0])
                    except FileNotFoundError:
                        print(f"No existe el directorio: {rest[0]}")

            case "mkdir":
                for dirname in rest:
                    try:
                        os.mkdir(dirname)
                        print(f"Directorio creado: {dirname}")
                    except FileExistsError:
                        print(f"Ya existe el directorio: {dirname}")

            case "rm" | "del":
                for filename in rest:
                    try:
                        os.remove(filename)
                        print(f"Archivo eliminado: {filename}")
                    except FileNotFoundError:
                        print(f"No existe el archivo: {filename}")

            case "cat" | "type":
                if not rest:
                    print("Error: especifica al menos un archivo.")
                else:
                    for fname in rest:
                        try:
                            with open(fname, "r") as f:
                                print(f.read(), end="")
                        except FileNotFoundError:
                            print(f"[Archivo no encontrado: {fname}]")

            case _:
                print(f"Comando no reconocido o no soportado: {cmd}")

    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
