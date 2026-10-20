t = int(input())

for _ in range(t):
    arr = sorted(list(map(int, input().split())))
    min_sum = arr[0] + arr[1]
    max_val = arr[-1]
    if min_sum >= max_val:
        print(max_val - arr[0])
    else:
        print(min_sum - arr[0])