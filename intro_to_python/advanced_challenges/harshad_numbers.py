# Harshad Numbers
# Pulled from Kattis.com (https://open.kattis.com/problems/harshadnumbers)

'''
A harshad number is a number which is evenly divisible by the sum of its digits.
For example, 24 is a harshad number beacuse it is divisible by the sum of its digits: 24 is divisible by (2+4 = 6). 
156 is also a harshad number, since 1+5+6 = 12 and 156 = 12*13. 
Notice that 23 is NOT a harshad number since it is not divisible by 2+3=5.

For this problem, you will be given a number n and must find the smallest harshad number greater than or equal to n.
'''

def harshad(n):
    # I'll give you a hint here: try a while True loop
    while True:
        # TODO: Starting at n, check if the current number's digits add to one of its divisors. Keep adding to n until you find a harshad number, and return the first one you find.
        # Hint: You can use a function called sum() to condense your code.

# Test Cases
print(harshad(24))
print(harshad(25))
print(harshad(1))
print(harshad(123))

'''
Correct Output:
24
27
1
126
'''