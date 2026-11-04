t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    used = 0
    while True:
        if a.count(ans) == 0:
            break
        small = 0
        for x in a:
            if x <= ans:
                small += 1
        if small - used < k:
            break
        used += k
        ans += 1
    print(ans)