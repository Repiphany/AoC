#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.n_children = data.pop()
        self.n_metadata = data.pop()
        self.children = [Node(data) for _ in range(self.n_children)]
        self.metadata = [data.pop() for _ in range(self.n_metadata)]

    def checksum(self):
        return sum(self.metadata) + sum(child.checksum() for child in
                self.children)

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            return sum(self.children[i - 1].value()
                    for i in self.metadata
                    if i and i-1 < self.n_children)

if __name__ == '__main__':
    with open('input', 'r') as f:
        data = [int(i) for i in f.read().split(' ')][::-1]
    root = Node(data)

    # part 1
    print(root.checksum())

    # part 2
    print(root.value())

