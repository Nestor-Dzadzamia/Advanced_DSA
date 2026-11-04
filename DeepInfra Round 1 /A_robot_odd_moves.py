t = int(input())

for tc in range(t):
    a, b = map(int, input().split())

    if b <= a and (a - b) % 2 == 0:
        print(a)
    elif b <= a + 1 and (a + 1 - b) % 2 == 0:
        print(a + 1)
    else:
        print(-1)