import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n, k = map(int, input().split())

    if k % 3 != 0:
        if n % 3 == 0:
            print("Bob")
        else:
            print("Alice")
    else:
        r = n % (k + 1)
        if r == k:
            print("Alice")
        elif r % 3 == 0:
            print("Bob")
        else:
            print("Alice")