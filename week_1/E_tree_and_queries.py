import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    col = [0] * (n + 1)
    for i in range(1, n + 1):
        col[i] = int(data[1 + i])
    pos = 2 + n
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[pos]); b = int(data[pos + 1]); pos += 2
        adj[a].append(b); adj[b].append(a)

    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append(u)
    size = [1] * (n + 1)
    heavy = [0] * (n + 1)
    for v in reversed(order):
        p = parent[v]
        if p > 0:
            size[p] += size[v]
    for v in order:
        best = 0; h = 0
        for u in adj[v]:
            if u != parent[v] and size[u] > best:
                best = size[u]; h = u
        heavy[v] = h
    tin = [0] * (n + 1)
    for i, v in enumerate(order):
        tin[v] = i

    qv = [[] for _ in range(n + 1)]
    for j in range(m):
        v = int(data[pos]); k = int(data[pos + 1]); pos += 2
        qv[v].append((k, j))
    ans = [0] * m

    cnt = [0] * 100002
    ge = [0] * (n + 2)

    stack = [(1, True, 0)]
    while stack:
        v, keep, state = stack.pop()
        if state == 0:
            stack.append((v, keep, 1))
            h = heavy[v]
            if h:
                stack.append((h, True, 0))
            pv = parent[v]
            for u in adj[v]:
                if u != pv and u != h:
                    stack.append((u, False, 0))
        else:
            c = col[v]
            cnt[c] += 1
            ge[cnt[c]] += 1
            h = heavy[v]
            pv = parent[v]
            for u in adj[v]:
                if u != pv and u != h:
                    s = tin[u]
                    for x in order[s:s + size[u]]:
                        c = col[x]
                        cnt[c] += 1
                        ge[cnt[c]] += 1
            for k, j in qv[v]:
                if k <= n:
                    ans[j] = ge[k]
            if not keep:
                s = tin[v]
                for x in order[s:s + size[v]]:
                    c = col[x]
                    ge[cnt[c]] -= 1
                    cnt[c] -= 1

    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

main()