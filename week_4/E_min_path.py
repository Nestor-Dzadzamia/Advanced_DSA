import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    INF = 1 << 62

    A = [[INF] * n for _ in range(n)]
    p = 3
    for _ in range(m):
        a = int(data[p]) - 1; b = int(data[p+1]) - 1; c = int(data[p+2]); p += 3
        if c < A[a][b]:
            A[a][b] = c

    def rows(Y):
        idx = []; val = []
        for j in range(n):
            Yj = Y[j]
            ii = []; vv = []
            for t in range(n):
                if Yj[t] < INF:
                    ii.append(t); vv.append(Yj[t])
            idx.append(ii); val.append(vv)
        return idx, val

    def mul(X, Y):
        idx, val = rows(Y)
        C = [[INF] * n for _ in range(n)]
        for i in range(n):
            Xi = X[i]; Ci = C[i]
            for j in range(n):
                x = Xi[j]
                if x < INF:
                    ii = idx[j]; vv = val[j]
                    for q in range(len(ii)):
                        w = x + vv[q]
                        t = ii[q]
                        if w < Ci[t]:
                            Ci[t] = w
            C[i] = Ci
        return C

    v = [0] * n
    while k:
        if k & 1:
            idx, val = rows(A)
            nv = [INF] * n
            for i in range(n):
                x = v[i]
                if x < INF:
                    ii = idx[i]; vv = val[i]
                    for q in range(len(ii)):
                        w = x + vv[q]
                        t = ii[q]
                        if w < nv[t]:
                            nv[t] = w
            v = nv
        k >>= 1
        if k:
            A = mul(A, A)

    best = min(v)
    print(best if best < INF else "IMPOSSIBLE")

main()