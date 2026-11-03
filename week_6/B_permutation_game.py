import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[a[i]] = i

win = [False] * n

for v in range(n, 0, -1):
    i = pos[v]
    w = False
    j = i - v
    while j >= 0:
        if a[j] > v and not win[j]:
            w = True
            break
        j -= v
    if not w:
        j = i + v
        while j < n:
            if a[j] > v and not win[j]:
                w = True
                break
            j += v
    win[i] = w

print(''.join('A' if win[i] else 'B' for i in range(n)))