import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); q = int(data[2])
    cnt = [0] * (m + 1)
    for i in range(3, 3 + n):
        cnt[int(data[i])] += 1
    order = sorted(range(1, m + 1), key=cnt.__getitem__)
    kraw = [int(x) - n - 1 for x in data[3 + n:3 + n + q]]
    queries = sorted(range(q), key=kraw.__getitem__)
    ks = [kraw[j] for j in queries]
    ans = [0] * q

    tree = [0] * (m + 1)
    LOG = 1
    while (1 << LOG) <= m:
        LOG += 1

    qi = 0
    start = 0
    for i in range(1, m):
        c = order[i - 1]
        j = c
        while j <= m:
            tree[j] += 1
            j += j & (-j)
        end = start + (cnt[order[i]] - cnt[c]) * i
        while qi < q and ks[qi] < end:
            k = (ks[qi] - start) % i + 1
            pos = 0
            step = 1 << LOG
            while step:
                nxt = pos + step
                if nxt <= m and tree[nxt] < k:
                    pos = nxt
                    k -= tree[nxt]
                step >>= 1
            ans[queries[qi]] = pos + 1
            qi += 1
        start = end
        if qi >= q:
            break
    while qi < q:
        ans[queries[qi]] = (ks[qi] - start) % m + 1
        qi += 1
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

main()