# // Given two strings, output the words that are unique to each string.
# // Example:
# // String 1: The quick brown fox jumped over the lazy fox
# // String 2: The slow blue whale swam over the quick shark
# // Output: slow, brown, blue, fox, whale, jumped, swam, lazy, shark
# // Explanation: The words "the", "quick", and "over" appear in both string, so they are not
# returned.
# // All other words are unique to their respective string and are returned in the output
#

def unique_words(string_1,string_2):
    result = []
    for items in string_1.split():
        if items not in string_2.split():
            if items not in result:
                result.append(items)
    for items in string_2.split():
        if items not in string_1.split():
            if items not in result:
                result.append(items)
    result = ','.join(result)
    return result



string_1 = 'The quick brown fox jumped over the lazy fox'
string_2 = 'The slow blue whale swam over the quick shark'
print(unique_words(string_1,string_2))

# def unique_words (string_1,string_2):
#     count ={}
#     for word in string_1.split():
#         count[word] =count.get(word,0) + 1
#     for word in string_2.split():
#         count[word] =count.get(word,0) + 1
#     return [word for word in count if count[word] == 1 ]
# string_1 ='The quick brown fox jumped over the lazy fox'
# string_2 ='The slow blue whale swam over the quick shark'
# print(unique_words(string_1,string_2))


