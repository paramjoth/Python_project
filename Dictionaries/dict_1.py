student = {'Education': 'Masters', 'course1': 'Computer_science', 'course2': 'electronics', 'course3': 'python'}
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
student['phone'] = '647-862-1607'
print(student)
for key,value in student.items():
    print(key,':',value)

del student['course3']
print(student)

deleted_item=student.popitem()
print(deleted_item)
print(student)
print('Adding new dicts')
location_details = {'place':'Windsor', 'country': 'Canada'}
PII = {'name':'Param', 'phone':'647-862-1607', 'email':'kaur.paramjoth@gmail.com', 'age': '30'}
student.update(location_details)
student_details = {**student, **location_details, **PII}
print(student)
print(student_details)
#del student # Delete the entire dictionary
#student.clear() # remove all item (key-values) from dict

#student = dict({'name': 'Param', 'age': 30, 'course': 'Computer_science', 'email': 'kaur.paramjoth@gmail.com'})