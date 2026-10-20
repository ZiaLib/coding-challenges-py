t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    base = 1
    best = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            base += 1
        if i < n - 1 and s[i - 1] != s[i] and s[i] != s[i + 1]:
            best = max(best, 1 + (s[i - 1] == s[i + 1]))
    print(base - best)