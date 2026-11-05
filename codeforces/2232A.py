t = int(input())

for _ in range(t):
    _ = input()
    a: list[int] = sorted(list(map(int, input().split())))
    center = a[len(a) // 2]
    l = [char for char in a if char < center]
    r = [char for char in a if char > center]
    ans = abs(len(l) - len(r))
    ans += min(len(l), len(r))
    print(ans)