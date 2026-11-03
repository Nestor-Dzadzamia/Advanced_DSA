import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a)

    cand = [m]
    for p in range(31):
        if m >> p & 1:
            cand.append(((m >> (p + 1)) << (p + 1)) | ((1 << p) - 1))

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] | a[i]
    suf = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] | a[i]

    ans = pre[n]
    for i in range(n):
        b = pre[i] | suf[i + 1]
        for c in cand:
            if c >= a[i]:
                x = b | c
                if x > ans:
                    ans = x

    print(ans)