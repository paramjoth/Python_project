# Write code to consume data from JSON file and flatten the nested data prior to loading into
# database.

import json, sys
from pandas import json_normalize
import pandas as pd

sample_object={
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}

#print(json_normalize(sample_object).to_string())
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

flat = flatten_json(sample_object)
#print(type(flat)) #dict
#print(flat)
print(json_normalize(flat)) #dataframe
df = json_normalize(flat)
df.to_csv('/Users/paramjothchahal/desktop/json_csv.csv')

# try:
#     conn = psycopg2.connect(database='wolfnet_data_services',
#                             user='wntdba', password='YGSeZPwadyFvVVw',
#                             host='pgsqlc1.prod.aws.wolfnet.com', port='5432')
#
# except Exception as err:
#     print('Error while creating the connection ', err)
#
# else:
#     print('connection established to pgload02')
# 	try:
# 		cursor = conn.cursor()
# 		json_csv.seek(0)
# 		contents = json_csv.getvalue()
# 		cursor.execute(f'SET search_path TO schema_name')
# 		cursor.copy_from(json_csv, 'table_name')
# 	except Exception as err:
# 		print('Error while inserting data from csv to attributes_report_raw ', err)
# 	else:
# 		print('loaded data to schema.table_name')
#
# finally:
#     cursor.close()
#     conn.close()




