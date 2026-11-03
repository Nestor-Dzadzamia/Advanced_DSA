t = int(input())

cycle = [4, 16, 37, 58, 89, 145, 42, 20]

def nxt(x):
    s = 0
    while x > 0:
        d = x % 10
        s += d * d
        x //= 10
    return s

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = {}
    for x in a:
        steps = 0
        # apply the rule until we land on 1 or step onto the cycle
        while x != 1 and x not in cycle:
            x = nxt(x)
            steps += 1

        if x == 1:
            key = 'happy'          # stays 1 forever, matches every other happy one
        else:
            key = (cycle.index(x) - steps) % 8   # phase in the 8-cycle

        cnt[key] = cnt.get(key, 0) + 1

    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    print(ans)

