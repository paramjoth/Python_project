import pandas as pd

df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_public.csv')
schema_df = pd.read_csv('/Users/paramjothchahal/desktop/Python/data/survey_results_schema.csv') # it will set index on this column

#print(df.head(5))
#print(schema_df.to_string()) #MentalHealth,Accessibility, Gender, Sexuality, SOComm, Age, Language

#select gender from df where gender is not null
print(df['Gender'].count())

#select  gender,count(*) from df group by gender
print(df['Gender'].value_counts())

#select country, gender from df group by country, gender
country_grp = df.groupby(['Country'])
print(country_grp['Gender'].value_counts())

#select country, gender from df group by country, gender having country='India' in percentage
print((country_grp['Gender'].value_counts(normalize=True).loc['India'])*100)

#group by country
country_grp = df.groupby(['Country'])
#select country, ethnicity, count(*) from df group by country, ethnicity
#print(country_grp['Ethnicity'].value_counts().head(10))

#select country, ethnicity, count(*) from df group by country, ethnicity having country='India'
#print(country_grp['Ethnicity'].value_counts().loc['India'].head(10))

#print(df.count())