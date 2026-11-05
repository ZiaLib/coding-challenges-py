t = int(input())

for _ in range(t):
    _, k = map(int, input().split())
    s = input()
    print("YES" if all(s[i::k].count("1") % 2 == 0 for i in range(k)) else "NO")
