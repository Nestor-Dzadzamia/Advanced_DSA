import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    head = [0] * (n + 1)
    nxt = [0] * (2 * n)
    dst = [0] * (2 * n)
    e = 1
    for _ in range(n - 1):
        a, b = map(int, input().split())
        dst[e] = b; nxt[e] = head[a]; head[a] = e; e += 1
        dst[e] = a; nxt[e] = head[b]; head[b] = e; e += 1

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        pv = parent[v]
        dv = depth[v]
        it = head[v]
        while it:
            u = dst[it]
            if u != pv:
                parent[u] = v
                depth[u] = dv + 1
                stack.append(u)
            it = nxt[it]

    sz = [1] * (n + 1)
    heavy = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        v = order[i]
        best = 0
        h = 0
        it = head[v]
        pv = parent[v]
        while it:
            u = dst[it]
            if u != pv:
                s = sz[u]
                if s > best:
                    best = s; h = u
            it = nxt[it]
        heavy[v] = h
        p = pv
        if p > 0:
            sz[p] += sz[v]

    chain_end = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        v = order[i]
        h = heavy[v]
        chain_end[v] = chain_end[h] if h else v

    def ask(s):
        sys.stdout.write(s)
        sys.stdout.flush()
        return int(input())

    dx = ask("d 1\n")
    u = 1
    while True:
        if depth[u] == dx:
            break
        cl = chain_end[u]
        dl = ask("d %d\n" % cl)
        dm = (depth[cl] + dx - dl) >> 1
        m = u
        while depth[m] < dm:
            m = heavy[m]
        if dm == dx:
            u = m
            break
        u = ask("s %d\n" % m)
    sys.stdout.write("! %d\n" % u)
    sys.stdout.flush()

main()