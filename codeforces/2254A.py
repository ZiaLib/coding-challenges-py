t = int(input())

for _ in range(t):
    arr = sorted(map(int, input().split()))
    print(min(arr[2] - arr[1], arr[1] - arr[0]))