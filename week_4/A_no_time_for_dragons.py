import sys
input = sys.stdin.readline

n = int(input())

d = []
for i in range(n):
    a, b = map(int, input().split())
    d.append((a - b, a, b))

d.sort(reverse=True)

ans = 0
cur = 0
for x, a, b in d:
    if cur + a > ans:
        ans = cur + a
    cur += b

print(ans)