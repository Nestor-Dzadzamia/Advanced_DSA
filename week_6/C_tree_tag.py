import sys
from collections import deque
input = sys.stdin.readline

def bfs(src, g, n):
    d = [-1] * (n + 1)
    d[src] = 0
    q = deque([src])
    while q:
        v = q.popleft()
        for u in g[v]:
            if d[u] < 0:
                d[u] = d[v] + 1
                q.append(u)
    return d

t = int(input())

for tc in range(t):
    n, a, b, da, db = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    d1 = bfs(a, g, n)
    far = max(range(1, n + 1), key=lambda x: d1[x])
    d2 = bfs(far, g, n)
    diam = max(d2[1:n + 1])

    if d1[b] <= da or 2 * da >= diam or db <= 2 * da:
        print("Alice")
    else:
        print("Bob")