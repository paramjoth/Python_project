import pandas as pd

df = pd.read_csv('/Users/paramjothchahal/desktop/details_.csv', index_col='emp_id')
print(df)
df.drop(columns='email', inplace=True)
df['full_name'] = df['fname']+ ' '+ df['lname']
#access first letter of the fname and whole lname
df['email'] = df['fname'].str[0] + df['lname'] + '@gmail.com'
#print(df.to_string())

#sort by fname,lname
df.sort_values(by=['fname','lname'], ascending=[True, True], inplace=True)
print(df.to_string())

#sort by department asc and salary desc
df.sort_values(by=['Department','Salary'], ascending=[True, False], inplace=True)
print(df.to_string())

#sort by department, country, city asc and salary desc
df.sort_values(by=['Department','country', 'City', 'Salary'], ascending=[True,True,True, False], inplace=True)
print(df[['Department','country','City','Salary']].to_string())

#nth largest or nth smallest values
print(df['Salary'].nlargest(10))
print(df.nlargest(10, 'Salary'))
print(df.nsmallest(5, 'Salary'))
