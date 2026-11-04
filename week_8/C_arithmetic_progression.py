import random
from math import gcd

n = int(input())
lo = 0
hi = 10 ** 9
while lo < hi:
    mid = (lo + hi) // 2
    print('>', mid, flush=True)
    r = int(input())
    if r == 1:
        lo = mid + 1
    else:
        hi = mid
mx = lo

d = 0
for k in range(30):
    i = random.randint(1, n)
    print('?', i, flush=True)
    x = int(input())
    d = gcd(d, mx - x)

print('!', mx - (n - 1) * d, d, flush=True)