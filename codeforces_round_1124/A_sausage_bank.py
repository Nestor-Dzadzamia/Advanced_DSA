import sys

def sol():
    inp = sys.stdin.buffer.read().split()
    t = int(inp[0])

    res = []
    for i in range(t):
        n = int(inp[i * 2 + 1])
        k = int(inp[i * 2 + 2])

        res.append((1 << (n - k + 1)) + (k - 1) * 2)
    sys.stdout.write('\n'.join(map(str, res)) + '\n')


sol()