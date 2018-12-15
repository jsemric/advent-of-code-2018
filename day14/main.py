#!/usr/bin/env python

def solve(l,p1,p2,f):
    i = len(l)

    while f(l):
        r = l[p1] + l[p2]

        if r >= 10:
            l.append(r // 10)
            l.append(r % 10)
            i += 2
        else:
            l.append(r)
            i += 1

        p1 = (p1 + l[p1] + 1) % i
        p2 = (p2 + l[p2] + 1) % i

    return l

def main():
    l = [3,7]
    p1, p2 = 0,1
    res = solve(l, p1, p2, lambda x: len(x) < 580752)
    print('First answer:', ''.join(str(i) for i in res[580741:580741+10]))
    
    res = solve([3,7], p1, p2,
        lambda x: not (x[-6:] == [5,8,0,7,4,1] or x[-7:-1] == [5,8,0,7,4,1]))
    print('Second answer:', len(res[:-6])-1) # -1 because 2 recipes were added

if __name__ == '__main__':
    main()