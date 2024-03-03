import termcolor


def fancy_hello_world():
    print(termcolor.colored("   _    _      _ _", "green", attrs=["bold"]))
    print(termcolor.colored("  | |  | |    | | |", "green", attrs=["bold"]))
    print(termcolor.colored("  | |__| | ___| | | ____", "green", attrs=["bold"]))
    print(termcolor.colored("  |  __  |/ _ \\ | ||   |", "green", attrs=["bold"]))
    print(termcolor.colored("  | |  | |  __/ | || | |", "green", attrs=["bold"]))
    print(termcolor.colored("  |_|  |_|\\___|_|_||___|", "green", attrs=["bold"]))
    print(termcolor.colored("Hello, World!", "cyan", attrs=["bold"]))


if __name__ == "__main__":
    fancy_hello_world()
