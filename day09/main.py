#!/usr/bin/env python

import sys
import unittest

class RingBuffer:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.head is None:
            return "<empty>"
        buff = ""
        it = self.head
        while True:
            buff += f'<{it.value}>'
            it = it.right
            if it is self.head:
                break

        return buff

    class Item:
        def __init__(self, value):
            self.left = self
            self.right = self
            self.value = value

    def move(self, n):
        if n > 0:
            self.head = self.head.right
            self.move(n-1)
        elif n < 0:
            self.head = self.head.left
            self.move(n+1)
        return self

    def add(self, val):
        item = RingBuffer.Item(val)
        if self.head is not None:
            item.left = self.head
            item.right = self.head.right
            self.head.right.left = item
            self.head.right = item
        self.head = item
        return self

    def pop(self):
        head = self.head
        if self.head.left is self.head:
            self.head = None
        else:
            head.right.left = head.left
            head.left.right = head.right
            self.head = head.right

        return head.value


def play(n,last):

    l = RingBuffer()
    l.add(0)
    scores = [0] * n
    c = 1

    for i in range(1,last+1):
        if i % 10000 == 0:
            print(f'{i}/{last}')
            sys.stdout.flush()

        # print(l)
        if i % 23 == 0:
            scores[i % len(scores)] += l.move(-7).pop() + i
        else:
            l.move(1).add(i)

    return max(scores)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(play(10,  35), 32)

    def test2(self):
        self.assertEqual(play(10 , 1618),   8317)

    def test3(self):
        self.assertEqual(play(13 , 7999),   146373)

    def test4(self):
        self.assertEqual(play(17 , 1104),   2764)

    def test5(self):
        self.assertEqual(play(21 , 6111),   54718)

    def test6(self):
        self.assertEqual(play(30 , 5807),   37305)

def main():
    if len(sys.argv) < 3:
        sys.stderr.write("need 2 arguments: <n-players> <n-rounds>\n")
        sys.exit(1)
    
    n = int(sys.argv[1])
    last = int(sys.argv[2])
    res = play(n,last)
    print(res)

if __name__ == '__main__':
    # unittest.main()
    main()