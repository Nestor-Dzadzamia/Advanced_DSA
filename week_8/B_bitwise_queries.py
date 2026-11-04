n = int(input())
x = [0] * (n + 1)
for i in range(2, n + 1):
    print('XOR 1', i, flush=True)
    x[i] = int(input())
print('AND 1 2', flush=True)
p = int(input())
print('AND 1 3', flush=True)
q = int(input())
print('AND 2 3', flush=True)
r = int(input())
s12 = x[2] + 2 * p
s13 = x[3] + 2 * q
s23 = (x[2] ^ x[3]) + 2 * r
a1 = (s12 + s13 - s23) // 2
ans = [a1]
for i in range(2, n + 1):
    ans.append(a1 ^ x[i])
print('!', *ans, flush=True)