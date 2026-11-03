import sys
input = sys.stdin.readline

def par(v):
    s = sorted(v)
    pos = {}
    for i in range(len(s)):
        pos[s[i]] = i
    p = [pos[x] for x in v]
    seen = [0] * len(p)
    c = 0
    for i in range(len(p)):
        if seen[i] == 0:
            c += 1
            j = i
            while seen[j] == 0:
                seen[j] = 1
                j = p[j]
    return (len(p) - c) % 2

t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sorted(a) != sorted(b):
        print("NO")
    elif par(a) == par(b):
        print("YES")
    else:
        print("NO")