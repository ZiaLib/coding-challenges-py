t = int(input())

for _ in range(t):
    s = input()
    s = max(s[0:i] + s[i + 1 :] for i in range(len(s)) if s[i] == "0")
    s = min(s[0:i] + s[i + 1 :] for i in range(len(s)) if s[i] == "1")
    print(s)
