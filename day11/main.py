#!/usr/bin/env python

import numpy as np
import itertools

SNO = 3031

def power(x,y, sno=SNO):
    rackid  = x + 10
    v = rackid * (rackid * y + sno)
    return int(str(v)[-3]) - 5

def max_power(a,k):
    l = []
    n = 301 - k
    for i,j in itertools.product(range(n),range(n)):
        s = a[i:i+k,j:j+k].sum()
        l.append(((i+1,j+1,k),s))

    return max(l, key=lambda x: x[1])

def main():
    a = np.zeros((300,300))

    for i,j in itertools.product(range(300),range(300)):
        a[i][j] = power(i+1,j+1)

    print('Answer 1:', max_power(a,3))

    l = []
    for k in range(2,301):
        if k % 10 == 0: print(k)
        l.append(max_power(a,k))

    print('Answer 2:', max(l, key=lambda x: x[1]))

if __name__ == '__main__':
    main()