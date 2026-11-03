import sys
from itertools import accumulate



def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); q = int(data[1])
    a = sorted(map(int, data[2:2 + n]))
    diff = [0] * (n + 2)
    pos = 2 + n
    for _ in range(q):
        l = int(data[pos]); r = int(data[pos + 1]); pos += 2
        diff[l] += 1
        diff[r + 1] -= 1
    frq = sorted(accumulate(diff[1:n + 1]))
    print(sum(x * f for x, f in zip(a, frq)))

main()