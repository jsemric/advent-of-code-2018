import numpy as np
import itertools

NEITHER, CGEAR, TORCH = 0,1,2
ROCK, WET, NARROW = 0,1,2

def adjacent(i,j):
    yield i+1, j
    yield i, j+1
    if i != 0: yield i-1,j
    if j != 0: yield i,j-1

def get_next(x,a):
    (i, j, tool), cost = x
    yield ((i,j,(tool + 1) % 3), cost + 7)
    yield ((i,j,(tool + 2) % 3), cost + 7)

    for (i2,j2) in adjacent(i,j):
        if a[i2,j2] % 3 == ROCK and tool != NEITHER:
            yield ((i2,j2,tool), cost + 1)
        elif a[i2,j2] % 3 == WET and tool != TORCH:
            yield ((i2,j2,tool), cost + 1)
        elif a[i2,j2] % 3 == NARROW and tool != CGEAR:
            yield ((i2,j2,tool), cost + 1)

def main():
    M = (0,0)
    T = (10,10)
    depth = 510
    # x,y = T[0]+10, T[1]+10
    T = (770,7)
    depth = 10647
    x,y = T[0]+1000, T[1]+1000

    a = np.zeros((x,y),dtype=np.int64)

    for i,j in itertools.product(range(x),range(y)):
        if i == 0 and j == 0:
            a[i,j] = 0
        elif i == 0:
            a[i,j] = j * 16807
        elif j == 0:
            a[i,j] = i * 48271
        elif i == T[0] and j == T[1]:
            a[i,j] = 0
        else:
            a[i,j] = a[i-1,j] * a[i,j-1]
        a[i,j] = (a[i,j] + depth) % 20183

    s = np.sum(a[:T[0]+1,:T[1]+1] % 3)
    print('Answer 1:', s)

    visited = {}
    next_ = {(0,0,TORCH): 0}

    while True:
        x = min(next_.items(), key=lambda x: x[1] + abs(x[0][0] - T[0]) + \
            abs(x[0][1] - T[1]))

        if x[0] == (T[0],T[1],TORCH):
            print('Answer 2:', x)
            break

        next_.pop(x[0])
        visited[x[0]] = x[1]

        for (k,v) in get_next(x, a):
            if k not in visited and (k not in next_ or next_[k] > v):
               next_[k] = v

        i += 1
        if i % 10000 == 1:
            print(x)

if __name__ == '__main__':
    main()