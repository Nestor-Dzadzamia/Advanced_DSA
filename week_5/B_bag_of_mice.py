w, b = map(int, input().split())

dp = [[0.0] * (b + 1) for _ in range(w + 1)]

for i in range(1, w + 1):
    for j in range(b + 1):
        tot = i + j
        res = i / tot
        if j >= 2:
            p = (j / tot) * ((j - 1) / (tot - 1))
            rem = tot - 2
            res += p * (i / rem) * dp[i - 1][j - 2]
            if j >= 3:
                res += p * ((j - 2) / rem) * dp[i][j - 3]
        dp[i][j] = res

print("%.12f" % dp[w][b])