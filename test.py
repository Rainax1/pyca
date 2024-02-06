import colorama

a = "this 'is' a string"
word_list = []

def color(highlight: tuple = ()):
    for word in a.split():
        if word == highlight[0]:
            print(f"{getattr(colorama.Fore, highlight[1].upper())}{word}")


color(("'is'", "red"))
