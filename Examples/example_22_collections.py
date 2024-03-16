"""Emulate a sequence with a LinkedList class.
Supports +, *, iteration, len(), """
from copy import copy


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            for value in values:
                if isinstance(value, Node):
                    value = value.value
                self.append(value)

    def append(self, value):
        if isinstance(value, Node):
            value = value.value
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def count(self, value):
        num = 0
        for node in self:
            if node.value == value:
                num += 1
        return num

    def index(self, value):
        for i, node in enumerate(self):
            if node.value == value:
                return i
        raise ValueError(f'{repr(value)} is not in LinkedList')

    def extend(self, iter):
        self.__iadd__(iter)

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f"index should be type 'int' but got '{type(index).__name__}'")
        if index < 0:
            index = len(self) + index + 1
        elif index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        cur_i = 1
        cur_node = self.head
        while cur_node is not None:
            if cur_i == index:
                new_node = Node(value)
                next_node = cur_node.next
                cur_node.next = new_node
                new_node.next = next_node
                return
            cur_i += 1
            cur_node = cur_node.next
        new_node = Node(value)
        next_node = cur_node.next
        cur_node.next = new_node
        new_node.next = next_node

    def pop(self):
        ...

    def remove(self, value):
        ...

    def reverse(self):
        ...

    def sort(self):
        ...

    def copy(self):
        new_ll = LinkedList()
        for node in self:
            new_ll.append(node.value)
        return new_ll

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __getitem__(self, idx):
        as_list = list(self)
        try:
            result_from_list = as_list.__getitem__(idx)
        except TypeError as e:
            raise TypeError(str(e).replace('list', 'LinkedList'))
        if isinstance(result_from_list, list):
            return LinkedList(result_from_list)
        return result_from_list

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            raise TypeError('LinkedList only supports single item assignment')
        as_list = [n for n in self]
        print(repr(as_list))
        try:
            node_to_edit = as_list.__getitem__(idx)
            node_to_edit.value = value
        except TypeError as e:
            raise TypeError(str(e).replace('list', 'LinkedList'))

    def __delitem__(self, key):
        if isinstance(key, slice):
            raise TypeError('LinkedList only supports single item deletion')
        len_list = len(self)
        if key < 0:
            key = len_list + key
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
            yield node
            node = node.next

    def __add__(self, other):
        if not is_iter(other):
            raise TypeError(f'can only concatenate an iterable (not {type(other).__name__}) to LinkedList')

        new_ll = self.copy()
        for val in other:
            new_ll.append(val)
        return new_ll

    def __radd__(self, other):
        other_copy = copy(other)
        for node in self:
            other_copy.append(node.value)
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
        new_ll = self.copy()
        if not isinstance(other, int):
            raise TypeError(f"can't multiply sequence by non-int of type '{type(other).__name__}'")

        if other <= 0:
            return LinkedList()

        for i in range(other):
            for node in self:
                new_ll.append(node)
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
            for node in self:
                new_ll.append(node)
        self.__iadd__(new_ll)
        return self

    def __contains__(self, item):
        for node in self:
            if node.value == item:
                return True
        return False

    def __str__(self):
        contents = " -> ".join(str(i) for i in self)
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

    # __add__
    print(ll + LinkedList(['a', 'b', 'c']))

    # __radd__
    print(['a', 'b', 'c'] + ll)

    # __mul__
    print(ll * 4)

    # __iadd__
    ll += ['A', 'B']
    print(ll)

    # __getitem__, printing with = calls repr()
    print(f"{ll[2]=}")
    print(f"{ll[-2]=}")
    print(f"{ll[1:3]=}")
    print(f"{ll[::-1]=}")

    # __setitem__
    ll[-4] = 100
    print(ll)

    # __delitem__
    del ll[-2]
    print(ll)

    # __iter__
    for i in ll:
        print(repr(i))

    # __contains__
    if 100 in ll:
        print("Found 100")

    # __reversed__ not implemented, but __len__ and __iter__ are
    for i in reversed(ll):
        print(i)

    # __imul__
    ll *= 2
    print(ll)
