import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []

    for tc in range(1, t + 1):
        n = int(data[tc])
        p = 1 << n.bit_length()

        a = [0]
        prev = 0
        for i in range(1, p):
            g = i ^ (i >> 1)
            a.append(g ^ prev)
            a.append(0)
            prev = g

        out.append(str(len(a)))
        out.append(' '.join(map(str, a)))

    sys.stdout.write('\n'.join(out) + '\n')

main()