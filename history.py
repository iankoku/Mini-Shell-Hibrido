
command_history = []

def add_to_history(command: str) -> None:
    command_history.append(command)

def show_history() -> None:
    for idx, cmd in enumerate(command_history, start=1):
        print(f"{idx}: {cmd}")
