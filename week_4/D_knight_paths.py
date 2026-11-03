import sys

def main():
    k = int(sys.stdin.buffer.read().split()[0])
    MOD = 1 << 32
    N = 64
    W = 72
    MASK = (1 << W) - 1

    mv = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
    adj = [[] for _ in range(N)]
    for r in range(8):
        for c in range(8):
            for dr, dc in mv:
                nr = r + dr; nc = c + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    adj[r * 8 + c].append(nr * 8 + nc)

    def mul(A, B):
        pb = []
        for row in B:
            x = 0
            for c in range(N - 1, -1, -1):
                x = (x << W) | row[c]
            pb.append(x)
        res = []
        for row in A:
            acc = 0
            for j in range(N):
                v = row[j]
                if v:
                    acc += v * pb[j]
            new = [0] * N
            for c in range(N):
                new[c] = (acc & MASK) % MOD
                acc >>= W
            res.append(new)
        return res

    M = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    u = [0] * N

    for bit in bin(k + 1)[2:]:
        u = [(u[i] + sum(x * y for x, y in zip(M[i], u))) % MOD for i in range(N)]
        M = mul(M, M)
        if bit == '1':
            u = [(u[i] + sum(M[i])) % MOD for i in range(N)]
            M = [[sum(col) % MOD for col in zip(*[M[j] for j in adj[i]])] for i in range(N)]

    print(u[0] % MOD)

main()