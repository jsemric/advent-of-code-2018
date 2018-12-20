from collections import defaultdict
import sys

def foo(map_):
    stack = []
    d = defaultdict(lambda: 1000000000000000)
    last = (0,0)
    d[last] = 0

    for c in map_:
        if c == '(':
            stack.append(last)
        elif c == ')':
            stack.pop()
        elif c == '|':
            last = stack[-1]
        else:
            if c == 'E': n = (last[0]+1,last[1])
            elif c == 'W': n = (last[0]-1,last[1])
            elif c == 'N': n = (last[0],last[1]+1)
            elif c == 'S': n = (last[0],last[1]-1)
            d[n] = min(d[n],d[last]+1)
            last = n

    return d

def main():
    map_ = next(sys.stdin)[1:-2]
    d = foo(map_)
    max_ = max(i for i in d.values())
    atleast1000 = sum(i >= 1000 for i in d.values())
    print('Answer 1:', max_)
    print('Answer 2:', atleast1000)

if __name__ == '__main__':
    main()