import sys
from bisect import bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []

    for tc in range(t):
        n = int(data[pos]); m = int(data[pos + 1]); k = int(data[pos + 2]); pos += 3
        l = [0] * n
        r = [0] * n
        for i in range(n):
            l[i] = int(data[pos]); r[i] = int(data[pos + 1]); pos += 2

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + r[i] - l[i] + 1

        def cov(x):
            i = bisect_right(l, x) - 1
            if i < 0:
                return 0
            e = r[i]
            if e > x:
                e = x
            return pre[i] + e - l[i] + 1

        def f(s):
            return cov(s + m - 1) - cov(s - 1)

        if k == 0:
            out.append(r[n - 1] + 1)
            continue

        got = -1
        for i in range(n):
            hi = f(l[i])
            if hi < k:
                continue
            lo = f(r[i])
            if lo > k:
                continue
            a = l[i]
            b = r[i]
            while a < b:
                mid = (a + b) // 2
                if f(mid) >= k:
                    a = mid + 1
                else:
                    b = mid
            if f(a) == k:
                got = a
            elif f(a - 1) == k:
                got = a - 1
            if got != -1:
                break

        out.append(got)

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()