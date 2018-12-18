import re
import sys
import time
import numpy as np

def render(pos):
    min_x = min(pos, key=lambda x: x[0])[0]
    max_x = max(pos, key=lambda x: x[0])[0]
    min_y = min(pos, key=lambda x: x[1])[1]
    max_y = max(pos, key=lambda x: x[1])[1]
    dx = 1 + max_x - min_x
    dy = 1 + max_y - min_y
    area = dx*dy
    if area < 1000:
        out = np.zeros((dy,dx))

        for (x,y) in pos:
            out[y - min_y,x - min_x] = 1

        return '\n'.join([''.join('#' if j else '.' for j in i) for i in out])
    # return out

def main():

    regex = re.compile('position=<(.*)> velocity=<(.*)>')
    pos = []
    vel = []

    for i in sys.stdin:
        a,b = regex.search(i).groups()
        x,y = a.strip().split(',')
        pos.append((int(x),int(y)))
        x,y = b.strip().split(',')
        vel.append((int(x),int(y)))

    for i in range(21000):
        r = render(pos)
        if r is not None:
            print('='*30)
            print('After', i, 'seconds')
            print('='*30)
            print(r)
            break

        pos = [(p[0] + v[0], p[1] + v[1]) for p,v in zip(pos, vel)]


if __name__ == '__main__':
    main()