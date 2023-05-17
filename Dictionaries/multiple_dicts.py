Param = {'name':'Param', 'age':32, 'role': 'Data Engineer', 'Dept': 'Engineering'}
Srikanth = {'name': 'Srikanth', 'age': 30, 'role': 'Database Developer', 'Dept': 'Data'}
Reshu = {'name': 'Reshu', 'age': 32, 'Dept': 'Engineering'}

emp = {'emp_1': Param, 'emp_2': Srikanth, 'emp_3': Reshu}

for key, values in emp.items():
    print(f'\n{key} details')
    for nested_keys, nested_values in values.items():
        print(nested_keys,':',nested_values,)

print(sorted(emp.items(), key=lambda x: x[1]['age']))


# calculate the square of each even number from a list and store in dict
numbers = [1, 3, 5, 2, 8]
dict_square = {item: item ** 2 for item in numbers if item%2==0}
print(dict_square)

#list of key and value and zip
telephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']
output_dict = {key:value for key,value in zip(persons,telephone_book)}
print(output_dict)
