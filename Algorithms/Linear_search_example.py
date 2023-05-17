#locate a card say num 3 from the given cards list
#inputs: cards, query
#outou: should match query

def locate_card(cards, query):
    position = 0
    print(f'cards are: {cards}')
    print(f'querying for number : {query}')
    while True:
        if cards[position] == query:
            print(f'found the number {query} at position: {position}')
            return position

        position += 1

        if position == len(cards):
            print(f'did not find the number {query} anywhere in the list: {cards}')
            return -1

tests = []
tests.append({'input': {'cards': [1,5], 'query': 5},
        'output': 1})
tests.append({'input': {'cards': [2, 5, 13, 6], 'query': 1},
        'output': -1})
tests.append({'input': {'cards': [9], 'query': 9},
        'output': 0})

for test in tests:
    print(locate_card(**test['input']) == test['output'])

