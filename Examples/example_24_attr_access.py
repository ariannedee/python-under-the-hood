class SharedAttributes:
    """Setting an attribute sets it on every instance of the class"""
    class_dict = {}

    def __getattribute__(self, name):
        print(f'__getattribute__({repr(name)})')

        # Avoid infinite recursion from getting self.dict_
        d = object.__getattribute__(self, 'class_dict')
        try:
            return d[name]
        except KeyError:
            raise AttributeError()

    def __getattr__(self, name):
        print(f'__getattr__({repr(name)})')
        return -1

    def __setattr__(self, name, value):
        print(f'__setattr__({repr(name)}, {repr(value)})')
        d = object.__getattribute__(self, 'class_dict')
        d[name] = value

    def __delattr__(self, name):
        print(f'__delattr__({repr(name)})')
        d = object.__getattribute__(self, 'class_dict')
        del d[name]

    def __dir__(self):
        d = object.__getattribute__(self, 'class_dict')
        base_dir = object.__dir__(self)
        return base_dir + list(d.keys())


if __name__ == '__main__':
    s1 = SharedAttributes()
    s2 = SharedAttributes()

    print(s1.a)  # Doesn't exist, returns -1

    s1.b = 10
    print(getattr(s1, 'b'))  # getattr() calls __getattribute__ first
    print(s2.b)      # Value exists on all instances
    print(dir(s1))
    print(dir(s2))

    del s2.b
    print(s1.b)
    print(dir(s1))
