t = int(input())


def matches_euclidean_sequence(expected: list[int], a: int, b: int) -> bool:
    sequence: list[int] = [a]
    while b != 0 and len(sequence) < len(expected):
        a, b = b, a % b
        sequence.append(a)
    return sequence == expected


for _ in range(t):
    _ = int(input())
    b = sorted(map(int, input().split()), reverse=True)
    print(f"{b[0]} {b[1]}" if matches_euclidean_sequence(b, b[0], b[1]) else "-1")
