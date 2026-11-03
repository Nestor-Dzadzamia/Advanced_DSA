import sys
from operator import mul

MOD = 10**9 + 7


def mat_mul(a, b):
    bt = list(zip(*b))
    return [[sum(map(mul, row, col)) % MOD for col in bt] for row in a]


def vec_mul(v, m):
    mt = list(zip(*m))
    return [sum(map(mul, v, col)) % MOD for col in mt]


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))

    z = a.count(0)
    x0 = sum(a[:z])
    m = min(z, n - z)

    total = n * (n - 1) // 2
    inv_total = pow(total, MOD - 2, MOD)

    trans = [[0] * (m + 1) for _ in range(m + 1)]
    for x in range(m + 1):
        down = x * x
        up = (z - x) * (n - z - x)
        stay = total - down - up
        if x > 0:
            trans[x][x - 1] = down * inv_total % MOD
        if x < m:
            trans[x][x + 1] = up * inv_total % MOD
        trans[x][x] = stay * inv_total % MOD

    vec = [0] * (m + 1)
    vec[x0] = 1
    while k:
        if k & 1:
            vec = vec_mul(vec, trans)
        trans = mat_mul(trans, trans)
        k >>= 1

    print(vec[0])


main()