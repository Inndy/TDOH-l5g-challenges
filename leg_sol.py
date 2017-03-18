from z3 import *

flag = [ Int('f%d' % i) for i in range(84) ]
S = Solver()

for line in open('leg/leg.txt'):
    S.add(eval(line))

assert str(S.check()) == 'sat'
model = S.model()
flag = [ chr(model[f].as_long()) for f in flag ]
print ''.join(flag)
