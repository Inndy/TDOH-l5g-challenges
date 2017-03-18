#!/usr/bin/env python3
import urllib.parse
from pprint import pprint

data = open('dist/log/access.log').readlines()
data = map(urllib.parse.unquote, data)
data = ( i for i in data if 'CAST(val AS CHAR)' in i )
data = [ (i[0] == '2', *i[116:-10].split(',1))>')) for i in data ]

flag = []

for success, idx, val in data:
    idx = int(idx) - 1
    while len(flag) <= idx:
        flag.append(set(range(0x20, 0x7f)))
    val = int(val)

    if success: # data[idx] > val
        flag[idx] = flag[idx].intersection(range(val + 1, 0x7f))
    else: # data[idx] <= val
        flag[idx] = flag[idx].intersection(range(0x20, val + 1))

flag = [ chr(list(i)[0]) for i in flag if i ]

print(''.join(flag))
