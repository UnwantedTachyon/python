import itertools

chrs = 'abcd'
n = 3

for xs in itertools.product(chrs, repeat = n):
    print(''.join(xs))
