import numpy as np
import sys
import re

def find_largest(l):
    max_ = max(l, key=lambda x: x[3])
    x,y,z,r = max_

    cnt = 0
    for i in range(len(l)):
        xx,yy,zz,_ = l[i]
        cnt += r >= abs(x-xx) + abs(y-yy) + abs(z-zz)

    return cnt

def in_range(x,y,z,l):
    cnt = 0
    for i in range(len(l)):
        xx,yy,zz,r = l[i]
        cnt += r >= abs(x-xx) + abs(y-yy) + abs(z-zz)
    return cnt

def hill_climbing(p,l,n=100,it=100000):
    max_ = in_range(*p,l)
    j = 0

    for i in range(it):
        dx = np.random.randint(-n,n) 
        dy = np.random.randint(-n,n)
        dz = np.random.randint(-n,n)

        new = p[0] + dx, p[1] + dy, p[2] + dz

        if sum(new) < sum(p):
            cnt = in_range(*new,l)    

            if cnt >= max_:
                p = new
                max_ = cnt
                if j % 10000 == 0:
                    print(p, max_, sum(p))
                j += 1

    return p,max_,sum(p)

def main():
    l = []
    regex = re.compile('pos=<(.*)>, r=(.*)')
    for i in sys.stdin:
        a = regex.search(i).groups()
        x,y,z = [int(j) for j in a[0].split(',')]
        r = int(a[1])
        l.append((x,y,z,r))

    a = np.array(l,dtype=int)
    print('Answer 1:', find_largest(a))
    
    p = max(((i,in_range(*i[:-1],a)) for i in a), key=lambda x: x[1])[0][:-1]
    it = 100000
    res = hill_climbing(p,a,100,it)
    print('Answer 2:', res)

if __name__ == '__main__':
    main()