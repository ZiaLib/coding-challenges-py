t = int(input())

for _ in range(t):
    n, x, y, z = map(int, input().split())
    hours = 0
    direct_lines = 0
    ai_lines = 0
    while direct_lines < n and ai_lines < n:
        hours += 1
        direct_lines += x + y
        ai_lines += x
        ai_lines += 0 if hours <= z else y * 10
    print(hours)
