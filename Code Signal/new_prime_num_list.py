# Question: Write a Python function that takes a list of integers and returns a new list containing only the prime numbers from the original list.
def is_prime(n):

    if n <= 1:

        return False

    if n == 2:

        return True

    if n % 2 == 0:

        return False

    for i in range(3, int(n**0.5) + 1, 2):

        if n % i == 0:

            return False

    return True

def filter_primes(numbers):

    return [num for num in numbers if is_prime(num)]

# Example usage

numbers = [10, 15, 3, 7, 13, 19, 21, 23]

print(filter_primes(numbers))

# Output: [3, 7, 13, 19, 23]



# Explanation: This question evaluates your ability to implement algorithms, particularly for checking prime numbers, and write clean, efficient, and reusable code. 
# It also tests your familiarity with Python’s list comprehensions and logical problem-solving skills, as you need to filter prime numbers from a given list.
