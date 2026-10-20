t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_sorted = sorted(a)
    no_swap = 0
    swap = c
    for i in range(n):
        if no_swap == -1 and swap == -1:
            print(-1)
            break
        if no_swap != -1:
            sub = a[i] - b[i]
            if sub < 0:
                no_swap = -1
            else:
                no_swap += sub
        if swap != -1:
            closest = next((a_e for a_e in a_sorted if a_e >= b[i]), None)
            if closest is None:
                swap = -1
            else:
                a_sorted.remove(closest)
                swap += closest - b[i]
    else:
        candidates = [no_swap, swap]
        if -1 in candidates:
            candidates.remove(-1)
        print(min(candidates))
