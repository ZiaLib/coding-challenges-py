def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


t = int(input())

for _ in range(t):
    _, x = map(int, input().split())
    a = list(map(int, input().split()))
    primes = prime_factors(x)
    ans = 0
    for prime in primes:
        ans = max(ans, sum(elem for elem in a if elem % prime == 0))
    print(ans)
