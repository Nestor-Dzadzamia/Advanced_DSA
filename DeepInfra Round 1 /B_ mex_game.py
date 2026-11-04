import sys
data = sys.stdin.buffer.read().split()

t = int(data[0])
pos = 1
ans = []

for tc in range(t):
    n = int(data[pos]); k = int(data[pos + 1]); pos += 2

    cnt = [0] * (n + 2)
    for i in range(n):
        cnt[int(data[pos + i])] += 1
    pos += n

    v = 0
    while cnt[v] >= 2 * k:
        v += 1

    if cnt[v] == 2 * k - 1:
        ans.append("YES")
    else:
        ans.append("NO")

sys.stdout.write('\n'.join(ans) + '\n')