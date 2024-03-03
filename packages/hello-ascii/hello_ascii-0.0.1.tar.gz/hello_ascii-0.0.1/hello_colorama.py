import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def fancy_hello_world():
    print(f"{Fore.GREEN}{Style.BRIGHT}")
    print("   _    _      _ _")
    print("  | |  | |    | | |")
    print("  | |__| | ___| | | ____")
    print("  |  __  |/ _ \\ | ||   |")
    print("  | |  | |  __/ | || | |")
    print("  |_|  |_|\\___|_|_||___|")
    print(f"{Fore.RESET}{Back.RESET}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}Hello, World!{Fore.RESET}{Style.RESET_ALL}")


if __name__ == "__main__":
    fancy_hello_world()
