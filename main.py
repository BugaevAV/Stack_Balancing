class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('a')
    s.push(9)
    s.push('s')
    s.push(12)
    print(s.isEmpty())
    print(s.items)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.items)
