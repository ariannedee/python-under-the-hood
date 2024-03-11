class LinkedListIterator:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        cur = self.node
        if cur:
            self.node = cur.next
        else:
            raise StopIteration
        return cur.value


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

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __reversed__(self):
        return LinkedListIterator

    def __str__(self):
        contents = " -> ".join(str(i) for i in self)
        return f'{contents}'

    def __repr__(self):
        as_list = ", ".join(str(i) for i in self)
        return f"LinkedList([{as_list}])"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({repr(self.value)})"


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3])
    print(ll)
    ll.append(4)
    for i in ll:
        print(i)

    for i in reversed(ll):
        print(i)

    print(repr(ll))