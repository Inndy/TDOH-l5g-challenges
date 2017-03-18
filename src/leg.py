import random

flag = b'TDOH{Here_is_your_super_looooooooooong_flaggggggggggggggggg_in_a_matrixxxxxxxxxxxxx}'

for i in range(len(flag)):
    idxs = [i] + random.sample(range(len(flag)), random.randint(7, len(flag) - 3))
    idxs = list(sorted(idxs))

    exp = ' + '.join('flag[%3d]' % i for i in idxs)
    s = sum(flag[i] for i in idxs)
    print('%s == %d' % (exp, s))
