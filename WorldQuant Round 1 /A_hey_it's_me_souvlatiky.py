t = int(input())

for tc in range(t):
    n = int(input())
    s = input()

    pos = []
    for i in range(n):
        if s[i] == '1':
            pos.append(i)

    cnt = len(pos)

    if cnt == 1:
        print(0)
    elif cnt == 2:
        print(1)
    else:
        print(pos[-1] - pos[0])