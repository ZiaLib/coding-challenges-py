t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = input()
    ans = 0
    for i in range(0, n, k):
        if "0" not in arr[i:i+k]:
            ans += 1
    print(ans)