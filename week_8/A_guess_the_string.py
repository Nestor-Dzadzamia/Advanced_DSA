n = int(input())
s = ''
pos = {}
for i in range(1, n + 1):
    if i == 1:
        print('? 1 1', flush=True)
        c = input().strip()
        s += c
        pos[c] = 1
        continue
    print('? 2 1', i, flush=True)
    x = int(input())
    if x > len(pos):
        print('? 1', i, flush=True)
        c = input().strip()
        s += c
        pos[c] = i
        continue
    a = sorted(pos.values())
    k = len(a)
    lo = 0
    hi = k - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        print('? 2', a[mid], i, flush=True)
        x = int(input())
        if x == k - mid:
            lo = mid
        else:
            hi = mid - 1
    c = s[a[lo] - 1]
    s += c
    pos[c] = i
print('!', s, flush=True)