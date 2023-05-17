#pandas are used for data analysis
import pandas as pd

#pandas read csv's in to Dataframe with read_csv() method
#pandas convert dictionary's in DataFrames with DataFrame() method
# df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_public.csv')
#schema_df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_schema.csv', index_col='qid') # it will set index on this column
#schema_df.sort_index()
#schema_df.sort_index(inplace=True)
#schema_df.sort_index(ascending=False)
# schema_df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_schema.csv')
# print(schema_df['qid'])
# print(df.head(10))
# print(schema_df.tail(10))
# print(df.shape)
# print(schema_df.info())


people = {
    'fname': ['param', 'srikanth', 'sri', 'reshu', 'param'],
    'lname' : ['chahal', 'Pandem', 'Reddy', 'kaur', 'chahal'],
    'email' : ['param.chahal@gmail.com', 'srikanth@gmail.com', 'sri.reddy@gmail.com', 'reshu.kaur@gmail.com','param.chahal@gmail.com'],
    'age' : [30, 31, 29 , 29, 30]
}

# print(people['age'])
# print(people['lname'])

df = pd.DataFrame(people)
df.set_index('fname', inplace=True)
df.sort_index()
df.sort_values(by=['fname','lname'], inplace=True)
print(df)
df.to_csv('/Users/paramjothchahal/desktop/Python/data/details_.csv')


df.drop_duplicates(inplace=True)

print(df)
# print(df['lname']) #this is the prefered way of accessing series of a Dataframe
# print(df[['fname','lname','email']])#list inside
# print(df.fname)

#to get columns list
# print(df.columns)
# print(df.columns[1])
#
# #to get rows from list use loc and iloc (integer location)
# print(df.iloc[1])
# print(df.iloc[[1],2])
# print(df.iloc[[1,2],2])
# print(df.loc[[1,2],'email'])

# print(df.iloc[[1,2],[2,3]])
# print(df.loc[[1,2],['age','email']]) #it allows us to use label instead os integer


# df.set_index('email', inplace=True)
# df.reser_index(inplace=True)


################################################
#Filtering
################################################
#salary between 70k and 120k
#
# range_sal = (df['salary'] > 75000) & (df['salary'] < 120000)
# df.loc[range_sal] # this will give all cols for matching rows
# # to get interested cols and matching rows
# df.loc[range_sal, 'name', 'role', 'department', 'salary']
# print(df)
#
# #similar to like '%python%' in sql we have str.contain('python', na=False) method
#
# new_filter = df['languages'].str.lower()
# new_filter = df['languages'].str.contain('python', na=False)
# #if you just print(new_filter) this will result Boolean values for all the rows
# df.loc[new_filter] # this will give all columns for matching rows
# df.loc[new_filer, 'languages', 'names'] # will also filter the cols fetched for matching rows

##################################################
#updating data in Rows and Cols
#################################################
# print(df.columns)
#
# # upper case call col names
# df.columns = [x.upper() for x in df.columns]
# print(df.columns)
#
# #repplace spaces with underscore
# df.columns = df.columns.str.replace(' ','_')
#
# df.rename(columns={'FNAME': 'first_name', 'LNAME': 'last_name'}, inplace=True)
# df.columns = [x.lower() for x in df.columns]
#
#
# df.loc[2] = ['sreekanth','Pandem', 'sree@gmail.com', 30]
# df.loc[3, 'last_name'] = 'chahal'
# df.loc[0, ['first_name', 'email']] = ['paramjoth', 'paramjoth.chahal@gmail.com']
# print(df)

#apply()
#applymap()
#map()
#replace()

##############################
#Add/remove rows and columns
##############################

# df['full_name'] = df['fname'] + ' ' + df['lname']
# print(df)
#
# df.drop(columns=['fname', 'lname'], inplace=True)
# print(df)
# df[['first_name', 'last_name']] = df['full_name'].str.split(' ', expand=True)
# print(df)
#
# df.drop(columns=['email','age'], inplace=True)
# print(df)
# df['email'] = df['first_name']+df['last_name']+'@gmail.com'
# print(df)
# df.applymap(str.lower)
# print(df)


