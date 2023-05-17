#binary search needs list to be in sorted order
# it searches the mid val of a sorrted list and then decide whether to search left/ right if the val is not the mid val

def locate_num(cards, query):
    low = 0
    hi = len(cards)-1

    while low <= hi:
        mid = (low + hi) // 2
        mid_val = cards[mid]

        if mid_val == query:
            return mid
        elif mid_val < query:
            low = mid + 1
        else:
            hi = mid - 1
    return -1

tests =[]
tests.append({'input': {'cards': [1,5,7,10,15,25,30], 'query': 7},
        'output': 2})
tests.append({'input': {'cards': [1,5,7,10,15,25,30], 'query': 2},
        'output': -1})
tests.append({'input': {'cards': [1,5,7,10,15,25,30], 'query': 1},
        'output': 0})

for test in tests:
    print(locate_num(**test['input']) == test['output'])


