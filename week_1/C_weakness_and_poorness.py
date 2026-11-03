import sys

def solve():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    values = [int(t) for t in tokens[1:1 + n]]

    def extremes(shift):
        best_high = 0.0
        best_low = 0.0
        run_high = 0.0
        run_low = 0.0
        for v in values:
            d = v - shift
            run_high = run_high + d if run_high > 0 else d
            run_low = run_low + d if run_low < 0 else d
            if run_high > best_high:
                best_high = run_high
            if run_low < best_low:
                best_low = run_low
        return best_high, -best_low

    def gap(shift):
        a, b = extremes(shift)
        return a - b, max(a, b)

    lo, hi = float(min(values)), float(max(values))
    d_lo, f_lo = gap(lo)
    d_hi, f_hi = gap(hi)
    if d_lo <= 0:
        answer = f_lo
    elif d_hi >= 0:
        answer = f_hi
    else:
        side = 0
        for _ in range(100):
            mid = lo - d_lo * (hi - lo) / (d_hi - d_lo)
            d_mid, f_mid = gap(mid)
            answer = f_mid
            if abs(d_mid) <= 1e-8 * max(1.0, f_mid) or hi - lo <= 1e-13 * max(1.0, abs(mid)):
                break
            if d_mid > 0:
                lo, d_lo = mid, d_mid
                if side == 1:
                    d_hi *= 0.5
                side = 1
            else:
                hi, d_hi = mid, d_mid
                if side == -1:
                    d_lo *= 0.5
                side = -1
    print("%.15f" % answer)

solve()