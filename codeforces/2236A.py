t = int(input())

for _ in range(t):
    _ = input()
    top_heights = list(map(int, input().split()))
    print(max(top_heights) + 1 - min(top_heights))
