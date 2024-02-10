from sys import exit as sysexit
from colorama import Fore, Style



# Custom class to display messages related Error, INFO, OK, etc

class Message:
    def __init__(self,
                 message_type: str,
                 message: str,
                 color: str = "Red",
                 filename: str = "",
                 line: int = 0,
                 col: int = 0,
                 wanna_exit: bool = False,
                 highlight: tuple = ()) -> None:

        # highlight a specific word in message
        # highlight = ("word", "Red")
        #               ^       ^
        #   word to highlight, color
        # only one word

        if highlight:
            word_list = []
            for word in message.split():

                # split string and iterate through every word in string

                if (word == highlight[0]):
                    word = f"{getattr(Fore, highlight[1].upper())}{word}{Fore.RESET}"

                word_list.append(word)
            message = f" ".join(i for i in word_list)

        message = f" [{getattr(Fore, color.upper())}{message_type}{Style.RESET_ALL}] :: {message}"

        if (filename) and line > 0 and col > 0:
            file = f"[{Fore.YELLOW}{filename}{Fore.RESET}:{line}:{col}]"
        else:
            file = ""
            message = message.lstrip()


        print(f"\n{file}{message}")
        if wanna_exit:
            sysexit(1)


if __name__ == "__main__":
    Message("INFO", message="Compiling 'hello.pyca'", color="Yellow", highlight=("Compiling", "Green"))
    Message("ERROR","'cwrite', Unknown keyword, Did you mean 'cwriteln'?", filename="hello.pyca", line=4,col=17, wanna_exit=True, highlight=("Unknown","Yellow"))
