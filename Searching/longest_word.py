#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
#Input: "fun&!! time"; Output: time
#findall() -	Returns a list containing all matches
#search() -	Returns a Match object if there is a match anywhere in the string
#split() -	Returns a list where the string has been split at each match
#sub() -	Replaces one or many matches with a string

import re #using regular expression library
def LongestWord(sen):
    pattern = re.compile(r'\w+')
    word = pattern.findall(sen)
    result = sorted(word, key=len, reverse=True)
    return result[0]

print(LongestWord('this is the longest word'))
print(LongestWord('fun&!! time'))
print(LongestWord('this is the highest longest largest word'))