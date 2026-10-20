t = int(input())

for _ in range(t):
    _ = input()
    arr = list(map(int, input().split()))
    bessie_count = arr.count(1)
    elsie_count = arr.count(0)
    print("Bessie" if bessie_count >= elsie_count else "Elsie")