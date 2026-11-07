t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if s[0] == "1":
        print(s.count("0"))
        continue
    cost = s.count("0")
    ans = cost
    for i in range(n):
        if s[i] == "1":
            cost += 1
        else:
            cost -= 1
        ans = min(ans, cost)
    print(ans)
