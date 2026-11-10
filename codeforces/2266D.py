t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = sorted(a[i] - i for i in range(n))
    ans = 1
    current_len = 1
    for i in range(1, len(d)):
        if d[i - 1] == d[i]:
            continue
        if d[i - 1] == d[i] - 1:
            current_len += 1
        else:
            current_len = 1
        ans = max(ans, current_len)
    print(ans)
