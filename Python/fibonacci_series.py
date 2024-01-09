# Write a Python function to generate the Fibonacci series up to a specified number of terms.

def fibo_finder(input_term):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377   
    fibo_seq = [0, 1]
    
    for i in range(input_term - 2):
        fibo_seq.append(fibo_seq[i] + fibo_seq[i+1])
        
    return fibo_seq

print(fibo_finder(10))

# ChatGPT's Answer:
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Test the fibonacci function
terms = 10
print(f'The Fibonacci series up to {terms} terms is: {fibonacci(terms)}')