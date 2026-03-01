import sys
from pathlib import Path
from colorama import init, Fore, Style
init(autoreset=True)

def print_tree(path: Path, level: int = 0):
    indent = "    " * level
    name = path.name + ("/" if path.is_dir() else "")
    if path.is_dir():
        color = Fore.BLUE + Style.BRIGHT
    else:
        color = Fore.GREEN
    print(f"{indent}{color}{name}{Style.RESET_ALL}")

    if path.is_dir():
        for item in sorted(path.iterdir()):
            print_tree(item, level + 1)


def get_file_path(path: Path):
    if path.is_dir():
        print("Структура директорії:")
        print_tree(path)
    else:
        print("Помилка: Ви не вказали шлях до директорії!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
        get_file_path(directory_path)
    else:
        print("Використання: python file_path.py <шлях_до_директорії>")