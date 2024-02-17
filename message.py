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


        # The `highlight` tuple is used to specify a particular word and its desired color for highlighting within string.

        # Highlight a specific word in message
        #
        # highlight=("word", "Red")
        #             ^       ^  
        # Word to highlight,  Color

        # Note:
        #   - Only one word can be highlighted at a time.
        #   - The color parameter should be a valid color such as "Red," "Yellow," etc.

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


        print(f"{file}{message}")
        if wanna_exit:
            sysexit(1)


if __name__ == "__main__":
    Message("INFO", message="Compiling 'hello.pyca'", color="Yellow", highlight=("Compiling", "Green"))
    Message("CMD", message="pyca.py com hello.pyca", color="White", highlight=("com", "Magenta"))
    Message("ERROR","'cwrite', Unknown keyword, Did you mean 'cwriteln'?", filename="hello.pyca", line=4,col=17, wanna_exit=True, highlight=("Unknown","Yellow"))
