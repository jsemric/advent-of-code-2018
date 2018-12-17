#!/usr/bin/env python

import sys
import numpy as np

def main():
    a = np.zeros((1000,1000))
    lines = [line for line in sys.stdin]

    for i in lines:
        s = i.split(' ')
        k,l = s[2][:-1].split(',')
        k,l = int(k), int(l)
        x,y = s[3].strip().split('x')
        x,y = int(x), int(y)

        a[k:k+x,l:l+y] += 1

    print('Answer 1:', (a > 1).sum())

    for i in lines:
        s = i.split(' ')
        id_ = s[0]
        k,l = s[2][:-1].split(',')
        k,l = int(k), int(l)
        x,y = s[3].strip().split('x')
        x,y = int(x), int(y)

        if (a[k:k+x,l:l+y] == 1).all():
            print('Answer 2:', id_[1:])
            break

if __name__ == '__main__':
    main()
