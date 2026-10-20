t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ans = [[0] * n for i in range(n)]
    collapse_count = n * 2 - k
    if collapse_count > n or collapse_count == 0:
        print(-1)
        continue
    for i in range(collapse_count):
        ans[i][i] = i + 1
    for i in range(k - collapse_count):
        row_col = collapse_count + i // 2
        is_col = i % 2 == 0
        ans[0 if is_col else row_col][row_col if is_col else 0] = collapse_count + i + 1
    fill = k
    for i in range(n ** 2):
        row = i // n
        col = i % n
        if ans[row][col] == 0:
            ans[row][col] = fill + 1
            fill += 1
    for row in ans:
        print(" ".join(map(str, row)))
