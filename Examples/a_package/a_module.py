class AClass:
    def a_method(self, arg_1, arg_2='a', *, key_1='b', key_2='c'):
        print(f'regular args: {arg_1=}, {arg_2=}')
        print(f'keyword only args: {key_1=}, {key_2=}')

        def inner_function():
            print(f'Enclosed vars: {arg_1=}, {arg_2=}, {key_1}, {key_2}')

        return inner_function


if __name__ == '__main__':
    AClass().a_method(1)
