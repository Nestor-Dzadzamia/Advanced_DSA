import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    d = [0] * (n + m)
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            d[i + j] ^= row[j]

    ok = False
    for x in d:
        if x != 0:
            ok = True
            break

    print("Ashish" if ok else "Jeel")