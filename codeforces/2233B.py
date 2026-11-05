t = int(input())

for _ in range(t):
    n = int(input())
    ans = []
    if n == 2:
        ans = [1, 2, 1, 1, 2, 2, 1, 2]
    else:
        for i in range(1, n + 1):
            ans += [i, i + 1 if i < n else 1, i, i]
    print(*ans)
