#Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest
# number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's
# (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1.
# Words will be separated by spaces.
#Examples
#Input: "Hello apple pie"
#Output: Hello
#Input: "No words"
#Output: -1

def LetterCountI(str):
    str = lower(str)
    words = str.split(' ')
    repeated = 1
    result = -1
    for word in words:
        for alpha in word:
            if word.count(alpha) > repeated:
                repeated = word.count(alpha)
                result = repeated
    return result


print(LetterCountI("Hello appple pie"))
