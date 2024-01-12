# Print the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead 
# of the number, and for the multiples of 5, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".


for i in range(1, 101):
    to_print = ""
    if i % 3 == 0:
        to_print += 'Fizz'
    if i % 5 == 0:
        to_print += 'Buzz'

    print(to_print or i)

for i in range(1, 101):
    to_print = ''.join(['Fizz'*(i % 3 == 0), 'Buzz'*(i % 5 == 0)]) or i
    
    print(to_print)