# Write a Python program that takes an integer as input and outputs its prime factorization. 
# The prime factorization of a number is the representation of that number as the product of 
# its prime factors.

def prime_factorization(number):
    factors = {}
    divisor = 2  # Start with the smallest prime factor

    while number > 1:
        while number % divisor == 0:
            if divisor not in factors:
                factors[divisor] = 0
            factors[divisor] += 1
            number //= divisor
        divisor += 1

    return factors

number = 36
print(prime_factorization(number))