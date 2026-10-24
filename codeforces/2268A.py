t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    while len(a) >= k:
        if a[len(a) - k] > a[k - 1]:
            ans += a.pop(len(a) - k)
        else:
            ans += a.pop(k - 1)
    print(ans)
