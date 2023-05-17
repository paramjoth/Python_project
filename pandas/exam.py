# Given a list of movie information,
# return the top k movies

# Your answer should be sorted in the following order:
# 1. Movie Ratings: Highest rating movies
# 2. Movie Frequency: How many times the movie showed up in the list?
# 3. Alphabetical: If ratings and frequency are tied, then represent the movies alphabetically

# If the first criteria is tied, then use the second and so on.

# Example 1:
# Input: [
#     ["Titanic", 4.5],
#     ["Inception", 4],
#     ["Social Network", 3.0]
# ], k = 2
# Output: ["Titanic", "Inception"]

# Explanation: "Titanic" and "Inception" are the two highest rated movies.

# Example 2:
# Input: [
#     ["Titanic", 4.5],
#     ["Inception", 4],
#     ["Captain Philips", 4.5],
#     ["Social Network", 3.0]
# ], k = 1
# Output: ["Captain Philips"]
# Explanation: "Titanic" and  "Captain Philips" are both rated equally and occur with the same frequency, thus the deciding factor is alphabetic order

# Example 3:
# Input: [
#     ["Titanic", 4.5],
#     ["Inception", 4],
#     ["Captain Philips", 4.5],
#     ["Titanic", 4.5],
#     ["Social Network", 3.0]
# ], k = 1
# Output: ["Titanic"]
# Explanation: "Titanic" and "Captain Philips" are rated equally, but "Titanic" occurs once more than the rest


#
# def topKMovies(k, l):
#     movies_dict = {}
#     for movie_entry in l:
#         name = movie_entry[0]
#         rating = movie_entry[1]
#         if movies_dict.get(name, False):
#             new_freq = movies_dict[name][1] + 1
#             movies_dict[name] = [rating, new_freq, name]
#         movies_dict[name] = [rating, 1, name]

        # Input: [
        #     ["Titanic", 4.5],
        #     ["Inception", 4],
        #     ["Captain Philips", 4.5],
        #     ["Social Network", 3.0]
        # ]
lists = [
["Titanic", 4.5],
["Inception", 4],
["Captain Philips", 4.5],
["Social Network", 3.0]
]
#print(lists[0])
#key_lists=[]
key_lists = [lists[index][0] for index in range(len(lists))]
  #  key_lists.append(lists[index][0])
print(key_lists)
my_dict ={}
for key_list, list in zip(key_lists,lists):
    my_dict[key_list]=list
print(my_dict)
print(my_dict.get('Inception', False))
print(my_dict.values())
print(my_dict.items())
new_dict = sorted(my_dict.items(), key=lambda x: x[1][1], reverse=True)
print(new_dict)