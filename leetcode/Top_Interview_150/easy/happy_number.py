# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def is_happy(n: int) -> bool:
    # 1^2 + 9^2 = 82
    # 8^2 + 2^2 = 68
    # 6^2 +  8^2 = 100
    # 1^2 + 0^2 + 0^2 = 1

    seen_number = set()

    def square_sum(num: int) -> int:
        result = 0
        while num > 0:
            digit = num % 10
            result += digit*digit 
            num //= 10
        
        return result 
    
    while n != 1 and n not in seen_number:
        seen_number.add(n)
        n = square_sum(n)
    
    return n == 1


n = 200
print(is_happy(n))














# def is_happy(n):
#     def square_sum(num):
#         result = 0
#         while num > 0:
#             digit = num % 10
#             result += digit ** 2
#             num //= 10
#         return result
    
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = square_sum(n)
    
#     return n == 1

# n = 19
# print(is_happy(n))

