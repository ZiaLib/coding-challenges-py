t = int(input())

for _ in range(t):
    n = int(input())
    print(sum((n // i) ** 2 for i in range(1, n + 1)))
