import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = [[] for i in range(n + 1)]
    for i in range(n - 1):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    v = list(map(int, input().split()))

    dist = [-1] * (n + 1)
    dist[n] = 0
    q = deque()
    q.append(n)
    while q:
        u = q.popleft()
        for w in g[u]:
            if w != 1 and dist[w] == -1:
                dist[w] = dist[u] + 1
                q.append(w)

    ans = 0
    for w in g[1]:
        if dist[w] != -1:
            ans = dist[w] + 1

    for x in v:
        if dist[x] != -1:
            ans = max(ans, dist[x] + 1)

    print(ans)