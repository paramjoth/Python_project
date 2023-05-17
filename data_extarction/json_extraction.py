import json
import requests
import pandas as pd
import mysql.connector
import csv


response = requests.get('https://formulae.brew.sh/api/bottle/a2ps.json')
data = json.loads(response.text)
print(data)
df = pd.json_normalize(data)
print(df)
df.to_csv('/Users/paramjothchahal/desktop/json_to_csv.csv')
with open('/Users/paramjothchahal/desktop/json_to_csv.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  column_names = []
  for rows in csv_reader:
    column_names.append(rows)
    break
print(column_names)
#column_def = []
column_def = [('col_' + column_name + ' ' + 'varchar(500)') for column_name in column_names[0][1:]]
#  column_def.append('"' + column_name + '" ' + 'varchar(500)')
print(column_def)
#print(', '.join(column_def))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Reshu3314",
  database="Test"
)

cursor = mydb.cursor()
sql = 'create table if not exists __bulkinstable1('
sql += ', '.join(column_def).replace('.','_')
sql += ');'

print(sql)
cursor.execute(sql)
sql = 'create table if not exists __bulkinstable1('
sql += ', '.join(column_def).replace('.','_')
sql += ');'

mydb.commit()
cursor.close()
mydb.close()