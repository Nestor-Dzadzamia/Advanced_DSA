import sys

# n, m, c



def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    col = data[2:2 + n]
    pos = 2 + n
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[pos]); b = int(data[pos + 1]); pos += 2
        adj[a].append(b); adj[b].append(a)

    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        tin[v] = len(order)
        order.append(v)
        pv = parent[v]
        for u in adj[v]:
            if u != pv:
                parent[u] = v
                stack.append(u)
    sz = [1] * (n + 1)
    for v in reversed(order):
        p = parent[v]
        if p > 0:
            sz[p] += sz[v]
    for v in range(1, n + 1):
        tout[v] = tin[v] + sz[v]

    size = 1
    log = 0
    while size < n:
        size <<= 1
        log += 1
    d = [0] * (2 * size)
    lz = [0] * size
    for i, v in enumerate(order):
        d[size + i] = 1 << int(col[v - 1])
    for k in range(size - 1, 0, -1):
        d[k] = d[2 * k] | d[2 * k + 1]

    out = []
    for _ in range(m):
        t = data[pos]
        if t == b'1':
            v = int(data[pos + 1]); c = int(data[pos + 2]); pos += 3
            l = tin[v] + size; r = tout[v] + size
            for i in range(log, 0, -1):
                if (l >> i) << i != l:
                    k = l >> i
                    z = lz[k]
                    if z:
                        bit = 1 << z
                        a = 2 * k
                        d[a] = bit; d[a + 1] = bit
                        if a < size:
                            lz[a] = z; lz[a + 1] = z
                        lz[k] = 0
                if (r >> i) << i != r:
                    k = (r - 1) >> i
                    z = lz[k]
                    if z:
                        bit = 1 << z
                        a = 2 * k
                        d[a] = bit; d[a + 1] = bit
                        if a < size:
                            lz[a] = z; lz[a + 1] = z
                        lz[k] = 0
            l2 = l; r2 = r
            bit = 1 << c
            while l < r:
                if l & 1:
                    d[l] = bit
                    if l < size:
                        lz[l] = c
                    l += 1
                if r & 1:
                    r -= 1
                    d[r] = bit
                    if r < size:
                        lz[r] = c
                l >>= 1; r >>= 1
            l = l2; r = r2
            for i in range(1, log + 1):
                if (l >> i) << i != l:
                    k = l >> i
                    d[k] = d[2 * k] | d[2 * k + 1]
                if (r >> i) << i != r:
                    k = (r - 1) >> i
                    d[k] = d[2 * k] | d[2 * k + 1]
        else:
            v = int(data[pos + 1]); pos += 2
            l = tin[v] + size; r = tout[v] + size
            for i in range(log, 0, -1):
                if (l >> i) << i != l:
                    k = l >> i
                    z = lz[k]
                    if z:
                        bit = 1 << z
                        a = 2 * k
                        d[a] = bit; d[a + 1] = bit
                        if a < size:
                            lz[a] = z; lz[a + 1] = z
                        lz[k] = 0
                if (r >> i) << i != r:
                    k = (r - 1) >> i
                    z = lz[k]
                    if z:
                        bit = 1 << z
                        a = 2 * k
                        d[a] = bit; d[a + 1] = bit
                        if a < size:
                            lz[a] = z; lz[a + 1] = z
                        lz[k] = 0
            res = 0
            while l < r:
                if l & 1:
                    res |= d[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res |= d[r]
                l >>= 1; r >>= 1
            out.append(bin(res).count('1'))
    if out:
        sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()