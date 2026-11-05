t = int(input())

for _ in range(t):
    _ = input()
    h = list(map(int, input().split()))
    print(max(h) + 1 - min(h))
