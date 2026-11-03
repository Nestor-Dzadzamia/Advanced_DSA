import sys

# n,

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    head = [0] * (n + 1)
    nxt = [0] * (2 * n)
    dst = [0] * (2 * n)
    pos = 1
    e = 1
    for _ in range(n - 1):
        a = int(data[pos]); b = int(data[pos + 1]); pos += 2
        dst[e] = b; nxt[e] = head[a]; head[a] = e; e += 1
        dst[e] = a; nxt[e] = head[b]; head[b] = e; e += 1

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
        it = head[v]
        while it:
            u = dst[it]
            if u != pv:
                parent[u] = v
                stack.append(u)
            it = nxt[it]
    sz = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        v = order[i]
        p = parent[v]
        if p > 0:
            sz[p] += sz[v]
    for v in range(1, n + 1):
        tout[v] = tin[v] + sz[v]

    size = 1
    while size < n:
        size <<= 1
    A = [0] * (2 * size)
    B = [0] * (2 * size)

    q = int(data[pos]); pos += 1
    out = []
    for t in range(1, q + 1):
        c = data[pos]; v = int(data[pos + 1]); pos += 2
        if c == b'1':
            l = tin[v] + size; r = tout[v] + size
            while l < r:
                if l & 1:
                    A[l] = t
                    l += 1
                if r & 1:
                    r -= 1
                    A[r] = t
                l >>= 1; r >>= 1
        elif c == b'2':
            x = tin[v] + size
            B[x] = t
            x >>= 1
            while x:
                y = B[2 * x]; z = B[2 * x + 1]
                B[x] = y if y > z else z
                x >>= 1
        else:
            x = tin[v] + size
            f = 0
            while x:
                y = A[x]
                if y > f:
                    f = y
                x >>= 1
            l = tin[v] + size; r = tout[v] + size
            g = 0
            while l < r:
                if l & 1:
                    y = B[l]
                    if y > g:
                        g = y
                    l += 1
                if r & 1:
                    r -= 1
                    y = B[r]
                    if y > g:
                        g = y
                l >>= 1; r >>= 1
            out.append(1 if f > g else 0)
    if out:
        sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()