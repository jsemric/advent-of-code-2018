#!/usr/bin/env python

import sys
import unittest

def play(n,last):

    l = [0]
    scores = [0] * n
    c = 1

    for i in range(1,last+1):
        if i % 10000 == 0:
            print(f'{i}/{last}')
            sys.stdout.flush()

        # print(l)
        if i % 23 == 0:
            m = (c - 7) % len(l)
            if m < 0:
                m = len(l) + m
            scores[i % len(scores)] += l[m] + i
            l.pop(m)
            c = m
        else:
            c = (c + 1) % (len(l)) + 1
            l.insert(c,i)

    return max(scores)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(play(10,35), 32)        
        self.assertEqual(play(10 , 1618),   8317)
        self.assertEqual(play(13 , 7999),   146373)
        self.assertEqual(play(17 , 1104),   2764)
        self.assertEqual(play(21 , 6111),   54718)
        self.assertEqual(play(30 , 5807),   37305)

def main():
    if len(sys.argv) < 3:
        sys.stderr.write("need 2 arguments: <n-players> <n-rounds>\n")
        sys.exit(1)
    
    n = int(sys.argv[1])
    last = int(sys.argv[2])
    res = play(n,last)
    print()
    print(res)


if __name__ == '__main__':
    # unittest.main()
    main()