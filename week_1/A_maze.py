import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    g = [list(row.decode()) for row in data[3:3 + n]]


    s = 0
    sr = sc = -1
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                s += 1
                sr, sc = i, j

    keep = s - k
    vis = [[False] * m for _ in range(n)]
    vis[sr][sc] = True
    cnt = 1
    q = deque([(sr, sc)])
    while q and cnt < keep:
        r, c = q.popleft()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if cnt >= keep:
                break
            if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == '.' and not vis[nr][nc]:
                vis[nr][nc] = True
                cnt += 1
                q.append((nr, nc))

    out = []
    for i in range(n):
        row = g[i]
        for j in range(m):
            if row[j] == '.' and not vis[i][j]:
                row[j] = 'X'
        out.append(''.join(row))
    sys.stdout.write('\n'.join(out) + '\n')

main()