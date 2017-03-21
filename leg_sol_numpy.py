import numpy
import re
import collections
from numpy.linalg import solve

mat = []
val = []

for line in open('dist/leg/leg.txt'):
    r = re.findall(r'flag\[\s*(\d+)\]', line)
    ctr = collections.Counter(map(int, r))
    mat.append([ctr[i] for i in range(84)])
    val.append(int(line.split()[-1]))

mat, val = map(numpy.array, (mat, val))

sol = solve(mat, val)
flag = ''.join(map(chr, map(int, map(round, sol))))
print(flag)
