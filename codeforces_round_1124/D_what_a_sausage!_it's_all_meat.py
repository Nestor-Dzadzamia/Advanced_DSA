import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    bad = [0] * 16
    for v in range(16):
        bad[v] = bin(v).count('1') % 2

    cnt = 0
    for v in a:
        if bad[v] == 0:
            cnt += 1

    res = [cnt]

    for i in range(q):
        p, x = map(int, input().split())
        p -= 1
        if bad[a[p]] == 0:
            cnt -= 1
        a[p] = x
        if bad[x] == 0:
            cnt += 1
        res.append(cnt)

    print(*res)