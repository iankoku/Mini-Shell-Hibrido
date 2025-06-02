
from hybrid_executor import execute_command
from history import add_to_history, show_history

def main():
    print("Mini Shell Híbrido - Simula comandos básicos")
    while True:
        try:
            command = input(">>> ").strip()
            if not command:
                continue
            if command.lower() == "exit":
                break
            elif command.lower() == "history":
                show_history()
            else:
                add_to_history(command)
                execute_command(command)
        except KeyboardInterrupt:
            print("\nEscriba 'exit' para salir.")
        except EOFError:
            break
