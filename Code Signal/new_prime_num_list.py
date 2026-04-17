# CodeSignal — Filter Primes from a List
# Time: O(n * sqrt(max_val))  — is_prime runs O(sqrt(k)) per element k
# Space: O(p)                 — result list holds p prime numbers


# Time: O(sqrt(n)) per number | Space: O(1)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only check odd divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True


# Time: O(n * sqrt(max_val)) | Space: O(p) where p = number of primes
def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]


numbers = [10, 15, 3, 7, 13, 19, 21, 23]
print(filter_primes(numbers))   # Output: [3, 7, 13, 19, 23]
