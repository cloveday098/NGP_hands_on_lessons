# These are possible solutions to each of the advanced challenges.
# They are pulled from the Kattis online judge database. Good luck!
# The formatting and test cases have been handled for you. You goal is to write a script to solve the problem.

# 1) Champernowne Verification
def champVerif(n):
    for i in range(len(n)):
        if n[i] != str(i+1): return -1
    return(n[-1])

# 2) Harshad Numbers
def harshad(n):
    while True:
        numSum = sum([int(i) for i in str(n)])      # This line sums all the digits of n using a method called list comprehension
        if n % numSum==0:                           # If the remainder is 0, that means you found a divisor of n. Yay!
            return n
        n+=1