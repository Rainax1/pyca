from sys import exit as sysexit
from colorama import Fore, Style


# Add way to track line and col
# Add Did you mean stuff

class Error:
    def __init__(self, error_message: str,
                 filename: str,
                 line: int,
                 col: int,
                 highlight: tuple = ()) -> None:

        if highlight:
            word_list = []
            for word in error_message.split():
                if (word == highlight[0]):
                    word = f"{getattr(Fore, highlight[1].upper())}{word}{Fore.RESET}"

                word_list.append(word)
            error_message = f" ".join(i for i in word_list)


        file = f"[{Fore.YELLOW}{filename}{Fore.RESET}:{line}:{col}]"
        error = f" [{Fore.RED}ERROR{Style.RESET_ALL}] :: {error_message}"

        print(f"\n{file}{error}")
        sysexit(1)

if __name__ == "__main__":
    Error("'dcwrite', Unknown keyword, Did you mean 'cwriteln'?", "hello.casm", 1,1, highlight=("Unknown","Yellow"))
