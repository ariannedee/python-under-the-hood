""" Context manager for printing to the console in a different color.
Exceptions are suppressed and printed out in red.

Codes are 'r', 'g', 'y', 'b' and 'p', for red, green, yellow, blue and purple.

with ColorConsole(code):
    # prints to the console with a color defined by code
"""


class ColorConsole:
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\033[94m'
    PURPLE = '\33[35m'

    ENDCOLOR = '\033[0m'

    def __init__(self, code='b'):
        self.code = code
        match code:
            case 'b':
                self.color = ColorConsole.BLUE
            case 'g':
                self.color = ColorConsole.GREEN
            case 'y':
                self.color = ColorConsole.YELLOW
            case 'p':
                self.color = ColorConsole.PURPLE
            case 'r':
                self.color = ColorConsole.RED
            case other:
                self.color = ColorConsole.ENDCOLOR
                print(f"Invalid code: {repr(code)}. Must be 'b', 'g', 'y', or 'r'.")

    def __enter__(self):
        print(self.color, end='')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(ColorConsole.RED, end='')
            print(f'{exc_type.__name__} caught in exit function:')
            print(f'    {exc_val}')
        print(ColorConsole.ENDCOLOR, end='')
        # return True if you don't want exceptions to be propagated
        return True

    # Async functions used in example 27
    async def __aenter__(self):
        return self.__enter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.__exit__(exc_type, exc_val, exc_tb)

    def __repr__(self):
        return f"ColorConsole({repr(self.code)})"


if __name__ == '__main__':
    with ColorConsole('b') as value:
        print('I should be blue')
        print(value)
        # If an error is raised in the context, stop execution and call exit
        int(None)

    print('I should be black')
