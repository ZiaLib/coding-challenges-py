import collections

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for i in range(m):
        arr += map(int, input().split())
    if len(set(arr)) != n:
        print("Brain Melt")
    elif sorted(collections.Counter(arr).values())[-1] == m:
        print(2)
    else:
        print("Many")
