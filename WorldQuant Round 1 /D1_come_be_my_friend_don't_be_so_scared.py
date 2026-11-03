import sys
data = sys.stdin.buffer.read().split()

t = int(data[0])
pos = 1
out = []

for tc in range(t):
    n = int(data[pos])
    m = int(data[pos + 1])
    pos += 2 + 2 * m

    if n == 1:
        out.append('0')
    else:
        k = (n + 1) // 2
        out.append(str(k))
        for i in range(1, k + 1):
            l = 2 * i - 2
            if l < 1:
                l = 1
            r = 2 * i
            if r > 2 * k - 1:
                r = 2 * k - 1
            out.append('%d %d' % (l, r))

sys.stdout.write('\n'.join(out) + '\n')