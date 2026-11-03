import sys
from itertools import accumulate

def sweep_pattern(ans, W, l, r, p):
    j0 = l % p
    t = l
    for j in range(j0, p):
        ans[t] += W[j]
        t += 1
    while t + p - 1 <= r:
        for j in range(p):
            ans[t] += W[j]
            t += 1
    for j in range(r - t + 1):
        ans[t] += W[j]
        t += 1

def sweep_step(ans, D, l, r, p, V):
    rr = (l - 1) % p
    for t in range(l, r + 1):
        rr += 1
        if rr == p:
            rr = 0
        V += D[rr]
        ans[t] += V
    return V

def fill(ans, D, l, r, p, V):
    if r - l + 1 < p:
        return sweep_step(ans, D, l, r, p, V)
    W = list(accumulate(D))
    base = V - W[(l - 1) % p]
    for j in range(p):
        W[j] += base
    sweep_pattern(ans, W, l, r, p)
    return W[r % p]

def mark_long(big, a, b, x, y, p):
    for s in range(a + x, b - y + 1, p):
        big[s] += 1
        big[s + y] -= 1
    s = a + x
    lo = b - y + 1
    if s < lo:
        s += ((lo - s + p - 1) // p) * p
    if s < b:
        big[s] += 1
        big[b] -= 1

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    xs = [0] * (n + 1)
    ys = [0] * (n + 1)
    pos = 2
    for i in range(1, n + 1):
        xs[i] = int(data[pos]); ys[i] = int(data[pos + 1]); pos += 2

    added_day = [0] * (n + 1)
    by_period = {}
    for t in range(1, m + 1):
        isadd = data[pos] == b'1'; k = int(data[pos + 1]); pos += 2
        if isadd:
            added_day[k] = t
        else:
            p = xs[k] + ys[k]
            lst = by_period.get(p)
            if lst is None:
                lst = by_period[p] = []
            lst.append((added_day[k], t, k))
            added_day[k] = 0
    for k in range(1, n + 1):
        if added_day[k]:
            p = xs[k] + ys[k]
            lst = by_period.get(p)
            if lst is None:
                lst = by_period[p] = []
            lst.append((added_day[k], m + 1, k))

    periods = sorted(by_period)
    cand = []
    total_long = 0
    for p in periods:
        lst = by_period[p]
        if p > m:
            total_long += len(lst)
            continue
        lst.sort()
        tot = 0
        cs = ce = 0
        lc = 0
        for a, b, k in lst:
            if a > ce:
                tot += ce - cs
                cs, ce = a, b
            elif b > ce:
                ce = b
            lc += (b - a) // p + 1
        tot += ce - cs
        total_long += lc
        cand.append((p, tot + 3 * p, lc))

    best = total_long
    B = 0
    acc_s = 0
    acc_l = total_long
    for p, sc, lc in cand:
        acc_s += sc
        acc_l -= lc
        c = acc_s * 0.8 + acc_l
        if c < best:
            best = c
            B = p

    ans = [0] * (m + 2)
    big = [0] * (m + 3)

    scratch = [0] * 20005
    sweep_pattern(scratch, [1] * 2000, 1, 20000, 2000)
    sweep_step(scratch, [0] * 2000, 1, 20000, 2000, 0)
    mark_long(scratch, 1, 20000, 1, 1, 2)

    for p in periods:
        if p <= B:
            continue
        for a, b, k in by_period[p]:
            mark_long(big, a, b, xs[k], ys[k], p)

    cur = 0
    for t in range(1, m + 1):
        cur += big[t]
        ans[t] = cur

    for p in reversed(periods):
        if p > B:
            continue
        events = []
        for a, b, k in by_period[p]:
            events.append((a, 1, k))
            if b <= m:
                events.append((b, 0, k))
        events.sort()
        D = [0] * p
        V = 0
        prev = 0
        active = 0
        for day, isadd, k in events:
            if active and day - 1 >= prev + 1:
                V = fill(ans, D, prev + 1, day - 1, p, V)
            V += D[day % p]
            x = xs[k]
            if isadd:
                added_day[k] = day
                D[(day + x) % p] += 1
                D[day % p] -= 1
                active += 1
            else:
                a = added_day[k]
                D[(a + x) % p] -= 1
                D[a % p] += 1
                if (day - a) % p >= x:
                    V -= 1
                active -= 1
            ans[day] += V
            prev = day
        if active and prev < m:
            fill(ans, D, prev + 1, m, p, V)

    sys.stdout.write('\n'.join(map(str, ans[1:m + 1])) + '\n')

main()