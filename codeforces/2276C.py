t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    rems = [0] * (n + 1)
    for i in range(1, n + 1):
        rems[i] = (rems[i - 1] + arr[i - 1]) % k
    ans = 0
    freq = [0] * k
    for i in range(k + 1, n + 1):
        freq[rems[i - k - 1]] += 1
        ans += freq[rems[i]]
    print(ans)