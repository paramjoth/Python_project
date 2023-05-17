from datetime import datetime
import pandas as pd

start_time = datetime.now()
print(f'program start time : {start_time}')
df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_schema.csv')
print(df.info)
print(list(df.columns))

#drop a column from DF
df.drop(columns='question', inplace=True)
df['enabled'] = 'Y'
print(list(df.columns))
print(df.head())
#deleting rows from DF
df.drop(index=[1,3,25], inplace=True)
df.drop(df.index[15:76] , inplace=True)
print(df)

end_time = datetime.now()
print(f'program end time : {end_time}')

time_elapsed = end_time - start_time
print(f'total time for execution : {time_elapsed}')