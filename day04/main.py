#!/usr/bin/env python

import re
import sys
import numpy as np
from datetime import datetime
from pprint import pprint
from collections import defaultdict

def compute_minutes(records):
    regex = re.compile('Guard #(\d+) begins shift')
    results = defaultdict(lambda: np.zeros(60))
    current = None
    start = None

    for (d,r) in records:
        if r == "falls asleep":
            start = d.minute
        elif r == "wakes up":
            assert current is not None
            results[current][start:d.minute] += 1
        else:
            current = int(regex.search(r).groups()[0])

    return results

def find_result(results, f=np.sum):
    tmp = [(k,f(v)) for k,v in results.items()]
    a = np.array([i[1] for i in tmp])
    i = np.argmax(a)
    max_id = tmp[i][0]
    max_min = results[max_id].argmax()
    return max_id, max_min

def main():
    regex = re.compile('\[(.+)\] (.+)')
    l = []
    for line in sys.stdin:
        m = regex.search(line)
        date, action = m.groups()
        date = datetime.strptime(date,'%Y-%m-%d %H:%M')
        l.append((date,action))

    l = sorted(l, key=lambda x: x[0].timestamp())
    results = compute_minutes(l)
    max_id, max_min = find_result(results)
    print("First answer:", max_id * max_min)
    max_id, max_min = find_result(results, np.max)
    print("Second answer:", max_id * max_min)


if __name__ == '__main__':
    main()