import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    c = min(k - 1, n - k + 1)
    for i in range(c):
        x = a[i]
        y = a[n - 1 - i]
        if x > y:
            ans += x
        else:
            ans += y

    ans += sum(a[k-1:n-k+1])

    print(ans)