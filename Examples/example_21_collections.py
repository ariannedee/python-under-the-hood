from copy import deepcopy

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            for value in values:
                self.append(value)

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def count(self, value):
        ...

    def index(self, value):
        ...

    def extend(self, iter):
        ...

    def insert(self, index, value):
        ...

    def pop(self):
        ...

    def remove(self, value):
        ...

    def reverse(self):
        ...

    def sort(self):
        ...

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __getitem__(self, item):
        as_list = [i for i in self]
        try:
            result_from_list = as_list.__getitem__(item)
        except TypeError as e:
            raise TypeError(str(e).replace('list', 'LinkedList'))
        if isinstance(result_from_list, list):
            return LinkedList(result_from_list)
        return result_from_list

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            raise TypeError('LinkedList only supports single item assignment')
        self[key].value = value

    def __delitem__(self, key):
        if isinstance(key, slice):
            raise TypeError('LinkedList only supports single item deletion')

        index = 0
        prev = None
        node = self.head
        while True:
            if key == index:
                if node == self.head:
                    self.head = node.next
                else:
                    prev.next = node.next
                return
            index += 1
            prev = node
            node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __add__(self, other):
        new_ll = deepcopy(self)
        if not is_iter(other):
            raise TypeError(f'can only concatenate an iterable (not {type(other).__name__}) to LinkedList')
        for val in other:
            if isinstance(val, Node):
                val = val.value
            new_ll.append(val)
        return new_ll

    def __radd__(self, other):
        other_copy = deepcopy(other)
        for val in self:
            other_copy.append(val)
        return other_copy

    def __iadd__(self, other):
        if not is_iter(other):
            raise TypeError(f'can only concatenate an iterable (not {type(other).__name__}) to LinkedList')
        for val in other:
            if isinstance(val, Node):
                val = val.value
            self.append(val)
        return self

    def __mul__(self, other):
        new_ll = deepcopy(self)
        if not isinstance(other, int):
            raise TypeError(f"can't multiply sequence by non-int of type '{type(other).__name__}'")

        if other <= 0:
            return LinkedList()

        for i in range(other):
            vals = (val for val in self)
            for val in vals:
                new_ll.append(val)
        return new_ll

    def __imul__(self, other):
        new_ll = LinkedList()
        if not isinstance(other, int):
            raise TypeError(f"can't multiply sequence by non-int of type '{type(other).__name__}'")

        if other <= 0:
            while self.head:
                node = self.head
                self.head = self.head.next
                del node

        for i in range(other - 1):
            vals = (val for val in self)
            for val in vals:
                new_ll.append(val)
        self.__iadd__(new_ll)
        return self

    def __str__(self):
        contents = " -> ".join(repr(i) for i in self)
        if not contents:
            return f'Empty'
        return f'{contents}'

    def __repr__(self):
        as_list = ", ".join(repr(i) for i in self)
        return f"LinkedList([{as_list}])"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return f"Node({repr(self.value)})"


def is_iter(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3])
    print(ll + LinkedList(['a', 'b', 'c']))
    print(['a', 'b', 'c'] + ll)
    print(ll * 4)
    ll += ['A', 'B']
    print(ll)
    print(f"{ll[2.0]=}")
    print(f"{ll[-2]=}")
    print(f"{ll[1:3]=}")
    print(f"{ll[::-1]=}")

    del ll[0]

    ll.append(4)
    for i in reversed(ll):
        print(i)

    ll *= 0
    print(ll)
