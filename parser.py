from message import Message
from sys import exit as sysexit



# Parser

class Parser:
    def __init__(self, code: str) -> None:
        self.code = code.strip().split("\n")

        self.code = self.ParseImports(code)

    def ParseAll(self, code):
        pass

    def ParseImports(self, code: str) -> str:
        for line in code:
            print(line)


Parser("code\nfd")
