t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = 1
    for start in range(2):
        ways = 0
        for first_check in "01":
            next_check = first_check
            for i in range(start, n, 2):
                if s[i] != "?" and s[i] != next_check:
                    break
                next_check = "1" if next_check == "0" else "0"
            else:
                ways += 1
        ans *= ways
    print(ans % 998244353)
