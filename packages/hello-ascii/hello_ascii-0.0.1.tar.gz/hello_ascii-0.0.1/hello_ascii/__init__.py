# from colorama import Fore, Style


def print_in_box(message, symbol='*'):
    """Prints a message in a decorative box."""
    length = len(message) + 4
    print(symbol * length)
    print(f"{symbol} {message} {symbol}")
    print(symbol * length)


message = "Hello World!"
print_in_box(message, symbol='@')  # Change symbol for different borders

# colored_message = Fore.YELLOW + message + Style.RESET_ALL
# print_in_box(colored_message)
