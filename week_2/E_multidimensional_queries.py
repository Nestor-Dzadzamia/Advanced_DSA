import sys



def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); k = int(data[1])
    M = 1 << k
    FULL = M - 1
    HALF = M >> 1
    NEG = -(1 << 60)
    size = 1
    while size < n:
        size <<= 1
    tree = [NEG] * (2 * size * M)

    signs = [[1 if (mask >> i) & 1 else -1 for i in range(k)] for mask in range(M)]

    pos = 2
    for i in range(n):
        base = (size + i) * M
        p = [int(x) for x in data[pos:pos + k]]
        pos += k
        for mask in range(M):
            sg = signs[mask]
            s = 0
            for d in range(k):
                s += sg[d] * p[d]
            tree[base + mask] = s
    for node in range(size - 1, 0, -1):
        b = node * M; l = 2 * b; r = l + M
        for mask in range(M):
            x = tree[l + mask]; y = tree[r + mask]
            tree[b + mask] = x if x > y else y

    q = int(data[pos]); pos += 1
    out = []
    res = [NEG] * M
    for _ in range(q):
        if data[pos] == b'1':
            i = int(data[pos + 1]) - 1
            p = [int(x) for x in data[pos + 2:pos + 2 + k]]
            pos += 2 + k
            node = size + i
            base = node * M
            for mask in range(M):
                sg = signs[mask]
                s = 0
                for d in range(k):
                    s += sg[d] * p[d]
                tree[base + mask] = s
            node >>= 1
            while node:
                b = node * M; l = 2 * b; r = l + M
                for mask in range(M):
                    x = tree[l + mask]; y = tree[r + mask]
                    tree[b + mask] = x if x > y else y
                node >>= 1
        else:
            lo = int(data[pos + 1]) - 1 + size
            hi = int(data[pos + 2]) + size
            pos += 3
            for mask in range(M):
                res[mask] = NEG
            while lo < hi:
                if lo & 1:
                    b = lo * M
                    for mask in range(M):
                        v = tree[b + mask]
                        if v > res[mask]:
                            res[mask] = v
                    lo += 1
                if hi & 1:
                    hi -= 1
                    b = hi * M
                    for mask in range(M):
                        v = tree[b + mask]
                        if v > res[mask]:
                            res[mask] = v
                lo >>= 1; hi >>= 1
            best = 0
            for mask in range(HALF):
                v = res[mask] + res[mask ^ FULL]
                if v > best:
                    best = v
            out.append(best)
    if out:
        sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()