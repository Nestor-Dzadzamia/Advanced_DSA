n = int(input())
M = 1000000007

a, b = 0, 1
for bit in bin(n)[2:]:
    c = a * (2 * b - a) % M
    d = (a * a + b * b) % M
    if bit == '1':
        a, b = d, (c + d) % M
    else:
        a, b = c, d

print(a)