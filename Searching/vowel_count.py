# Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels
# the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.
# Examples
# Input: "hello"
# Output: 2
# Input: "coderbyte"
# Output: 3

def VowelCount(str):
    str = str.lower()
    vowel = ['a','e','i','o','u']
    result = 0
    for alpha in str:
        if alpha in vowel:
            result += 1
    return result

print(VowelCount("All cows eat grass and moo"))