t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    memory = []
    ans = []
    for i in range(n):
        if s[i] == "1":
            memory.append(len(ans))
            ans.append(i + 1)
        if s[i] == "2":
            if len(memory) > 0:
                index = memory.pop()
                ans.pop(index)
                ans.append(i + 1)
    print(len(ans))
    print(*ans)
