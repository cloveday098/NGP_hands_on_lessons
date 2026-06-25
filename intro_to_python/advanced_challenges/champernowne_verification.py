# Champernowne Verification
# Pulled from Kattis.com (https://open.kattis.com/problems/champernowneverification)

'''
The kth Champernowne word is obtained by writing down the first k positive integers and concatenating them together.
For example, the 10th Champernowne word is 12345678910.
Given a positive integer n, determine if it is a Champernowne word, and if so, which word.

If n is a kth Champernowne word, print k. Otherwise, print -1.
'''

def champVerif(n):
    for i in range(______):
        # TODO: n is treated a string. Loop through n and check that each character matches the Champernowne pattern.
        # Hint: String indexing is your friend here.
    
    return(n[-1])

# Test Cases
print(champVerif("123456789"))
print(champVerif("1000000000"))
print(champVerif("1324"))
print(champVerif("1234567"))

'''
Correct Output:
9
-1
-1
7
'''