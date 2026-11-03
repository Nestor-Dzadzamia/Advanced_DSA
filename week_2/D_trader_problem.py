import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); q = int(data[2])
    a = data[3:3 + n]
    b = data[3 + n:3 + n + m]
    ks = data[3 + n + m:3 + n + m + q]

    items = [(int(x), 1) for x in a] + [(int(x), 0) for x in b]
    items.sort()
    N = n + m
    vals = [v for v, _ in items]
    P = [0] * (N + 1)
    C = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + vals[i]
        C[i + 1] = C[i] + items[i][1]

    right = list(range(N))
    parent = list(range(N))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    gaps = sorted(range(N - 1), key=lambda i: vals[i + 1] - vals[i])
    order = sorted(range(q), key=lambda j: int(ks[j]))
    ans = [0] * q
    total = sum(v for v, mine in items if mine)

    gi = 0
    for j in order:
        k = int(ks[j])
        while gi < N - 1 and vals[gaps[gi] + 1] - vals[gaps[gi]] <= k:
            i = gaps[gi]; gi += 1
            l1 = find(i)
            r1 = right[l1]
            l2 = r1 + 1
            r2 = right[l2]
            c1 = C[r1 + 1] - C[l1]
            c2 = C[r2 + 1] - C[l2]
            total -= (P[r1 + 1] - P[r1 + 1 - c1]) + (P[r2 + 1] - P[r2 + 1 - c2])
            total += P[r2 + 1] - P[r2 + 1 - c1 - c2]
            parent[l2] = l1
            right[l1] = r2
        ans[j] = total
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

main()