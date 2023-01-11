#Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a portion
# of str1 characters can be rearranged to match str2, otherwise return the string false. For example: if str1 is "rkqodlw"
# and str2 is "world" the output should return true. Punctuation and symbols will not be entered with the parameters.
#Examples
#Input: "cdore" & str2 = "coder"
#Output: true
#Input: "h3llko" & str2 = "hello"
#Output: false
#incomplete
from itertools import combinations
def StringScramble(str1,str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if str1_len >= str2_len:
        combination = combinations(str1, str2_len)
        x = [' '.join(j) for j in combination]
        if str2 in x:
            return 'true'
        else:
            return 'false'
    else:
        return 'false'

Input1_str1= "cdore"; Input1_str2 = "coder"
Input2_str1= "h3llko"; Input2_str2 = "hello"
print(StringScramble(Input1_str1,Input1_str2))
print(StringScramble(Input2_str1,Input2_str2))
