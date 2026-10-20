t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * 3
    for i in range(n):
        if arr[i] % 2 != 0:
            freq[0] += 1
        elif arr[i] % 4 == 0:
            freq[1] += 1
        else:
            freq[2] += 1
    print(max(freq))
