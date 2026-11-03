import sys
data = sys.stdin.buffer.read().split()

t = int(data[0])
pos = 1
ans = []

for tc in range(t):
    n = int(data[pos])
    pos += 1

    odd = 0
    for i in range(n):
        if int(data[pos + i]) % 2 == 1:
            odd += 1
    pos += n
    even = n - odd

    if odd == 1 and even == 1:
        ans.append("Larpity")
    elif odd == 3 and even == 0:
        ans.append("Larpity")
    else:
        ans.append("Moggity")

sys.stdout.write('\n'.join(ans) + '\n')