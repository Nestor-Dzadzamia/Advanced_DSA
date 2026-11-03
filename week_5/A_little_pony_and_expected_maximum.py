m, n = map(int, input().split())

ans = 0.0
prev = 0.0
for v in range(1, m + 1):
    cur = (v / m) ** n
    ans += v * (cur - prev)
    prev = cur

print("%.12f" % ans)