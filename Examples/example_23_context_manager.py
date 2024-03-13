class BlueConsole:
    BLUE = '\033[94m'
    ENDCOLOR = '\033[0m'

    def __enter__(self):
        print(BlueConsole.BLUE, end='')
        print('Enter called')
        return 'Some value'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(BlueConsole.ENDCOLOR, end='')
        print('Exit called')
        # return True if you don't want exceptions to be propagated

    def __repr__(self):
        return "BlueConsole()"


if __name__ == '__main__':
    with BlueConsole() as value:
        print('I should be blue')
        print(value)
        # If an error is raised in the context, stop execution and call exit

    print('I should be black')
