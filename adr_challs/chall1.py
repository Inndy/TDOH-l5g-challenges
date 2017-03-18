from z3 import *

key = [ BitVec('k%d' % i, 8) for i in range(4) ]
data = [ BitVec('d%d' % i, 8) for i in range(24) ]

a = bytearray('040201010701010105020101050101000402010104020101'.decode('hex'))
b = bytearray('10001c04041f1f010a151c110a1f2c4304051b010f010c39'.decode('hex'))
known = bytearray('TDOH{')

s = Solver()

for i, v in enumerate(known):
    s.add(data[i] == v)

s.add(data[-1] == ord('}'))

for i in range(24):
    s.add(a[i] == data[i] / key[i % 4])
    s.add(b[i] == data[i] - a[i] * key[i % 4])

assert str(s.check()) == 'sat'

model = s.model()

print(', '.join(hex(model[i].as_long()) for i in key))
print(''.join(chr(model[i].as_long()) for i in data))
