import sys
import itertools
import copy

def neigh(l,i,j):
    return [
        l[i+1][j],l[i+1][j+1],l[i][j+1],
        l[i-1][j],l[i-1][j-1],l[i][j-1],
        l[i-1][j+1],l[i+1][j-1]
    ]

def next_minute(l,x,y):
    s = copy.deepcopy(l)
    for i,j in itertools.product(range(1,x-1),range(1,y-1)):
        a = l[i][j]
        if a == '.':
            if len([e for e in neigh(l,i,j) if e == '|']) >= 3:
                s[i][j] = '|'
        elif a == '|':
            if len([e for e in neigh(l,i,j) if e == '#']) >= 3:
                s[i][j] = '#'   
        elif a == '#':
            n = neigh(l,i,j)
            if len([e for e in n if e == '#']) == 0 or \
                len([e for e in n if e == '|']) == 0:
                s[i][j] = '.'
        else:
            raise RuntimeError("invalid cell")
    # l = s
    return s

def main():
    l = []
    for i in sys.stdin:
        l.append(['_']+list(i.strip())+['_'])
    y = len(l[0])
    l = [['_']*y] + l + [['_']*y]
    x = len(l)
    n = 10
    for k in range(n):
        l = next_minute(l,x,y)
    
    lumberyards = sum(1 for i in l for j in i if j == '#')
    wood = sum(1 for i in l for j in i if j == '|')
    print(lumberyards * wood)


if __name__ == '__main__':
    main()