# 1. is_prime(n) function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. digit_sum(k) function
def digit_sum(k):
    return sum(map(int, str(k)))

# 3. power_of_two(N) function
def power_of_two(N):
    res = []
    i = 1
    while i <= N:
        res.append(i)
        i *= 2
    return res

# Using map() to square numbers
numbers = [10, 23, 36, 41]
squared = list(map(lambda x: x**2, numbers))

# Using filter() to get prime numbers
primes = list(filter(is_prime, range(1, 20)))
