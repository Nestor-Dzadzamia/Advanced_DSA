import sys

def solve():
    tokens = sys.stdin.buffer.read().split()
    total_ops = int(tokens[0])
    BIT_WIDTH = 30
    zero_branch = [0]
    one_branch = [0]
    occupancy = [0]

    def adjust(value, delta):
        node = 0
        occupancy[node] += delta
        for level in range(BIT_WIDTH - 1, -1, -1):
            if (value >> level) & 1:
                step = one_branch[node]
                if step == 0:
                    step = len(occupancy)
                    one_branch[node] = step
                    zero_branch.append(0); one_branch.append(0); occupancy.append(0)
            else:
                step = zero_branch[node]
                if step == 0:
                    step = len(occupancy)
                    zero_branch[node] = step
                    zero_branch.append(0); one_branch.append(0); occupancy.append(0)
            node = step
            occupancy[node] += delta

    def best_xor(value):
        node = 0
        acc = 0
        for level in range(BIT_WIDTH - 1, -1, -1):
            if (value >> level) & 1:
                opposite, same = zero_branch[node], one_branch[node]
            else:
                opposite, same = one_branch[node], zero_branch[node]
            if opposite and occupancy[opposite] > 0:
                acc |= 1 << level
                node = opposite
            else:
                node = same
        return acc

    adjust(0, 1)
    results = []
    pos = 1
    for _ in range(total_ops):
        kind = tokens[pos]; value = int(tokens[pos + 1]); pos += 2
        if kind == b'+':
            adjust(value, 1)
        elif kind == b'-':
            adjust(value, -1)
        else:
            results.append(best_xor(value))
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()