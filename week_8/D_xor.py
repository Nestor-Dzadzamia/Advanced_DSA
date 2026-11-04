import random

n = int(input())


def ask(i, j):
    print('?', i, j, flush=True)
    return int(input())


B = (n - 1).bit_length()
w = [0] * B
while 0 in w:
    i = random.randint(1, n)
    j = random.randint(1, n)
    if i == j:
        continue
    r = ask(i, j)
    for b in range(B):
        if w[b] == 0 and (r >> b) & 1 == 0:
            w[b] = i


def get(x):
    v = 0
    for b in range(B):
        if w[b] != x and (ask(x, w[b]) >> b) & 1:
            v += 1 << b
    return v


a = list(range(1, n + 1))
random.shuffle(a)
cur = a[0]
val = get(cur)
for i in a[1:]:
    if ask(cur, i) == val:
        cur = i
        val = get(i)

ans = [0] * (n + 1)
for i in range(1, n + 1):
    if i != cur:
        ans[i] = ask(cur, i)
print('!', *ans[1:], flush=True)