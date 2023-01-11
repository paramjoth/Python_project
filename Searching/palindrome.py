#Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a
# palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter entered
# may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
# For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.
#Examples
#Input: "Noel - sees Leon"
#Output: true
#Input: "A war at Tarawa!"
#Output: true

import re

def PalindromeTwo(str):
    str = str.lower()
    result = re.sub(r'\W+', '', str)
    #pattern = re.compile(r'\w+')
    #result = pattern.findall(str)
    #result = ''.join(result)
    if result[::] == result[::-1]:
        return 'true'
    else:
        return 'false'

Input1="Anne, I vote more cars race Rome-to-Vienna"
Input2= "Noel - sees Leon"
Input3 = "Noel - sees Leon A"
print(PalindromeTwo(Input1))
print(PalindromeTwo(Input2))
print(PalindromeTwo(Input3))
