t = int(input())

for _ in range(t):
    _ = input()
    s = input().split()
    ans = 0
    zero = s.count("0")
    one = (s[0] + s[-1]).count("1")
    if zero < 2:
        ans = -1
    else:
        ans = one
    print(ans)
