def solve(r, s, p):
    dp = [[[0.0] * (p + 1) for _ in range(s + 1)] for _ in range(r + 1)]
    dp[r][s][p] = 1.0

    for i in range(r, -1, -1):
        for j in range(s, -1, -1):
            for k in range(p, -1, -1):
                cur = dp[i][j][k]
                if cur == 0.0:
                    continue
                total = i * j + j * k + k * i
                if total == 0:
                    continue
                if i and j:
                    dp[i][j - 1][k] += cur * i * j / total
                if j and k:
                    dp[i][j][k - 1] += cur * j * k / total
                if k and i:
                    dp[i - 1][j][k] += cur * k * i / total

    rock = sum(dp[i][0][0] for i in range(1, r + 1))
    scissors = sum(dp[0][j][0] for j in range(1, s + 1))
    paper = sum(dp[0][0][k] for k in range(1, p + 1))
    return rock, scissors, paper


r, s, p = map(int, input().split())
print("%.12f %.12f %.12f" % solve(r, s, p))