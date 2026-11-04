import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if min(a) <= n - 1:
        print(n)
    else:
        print(0)