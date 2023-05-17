#this works fine


import pandas as pd
import gspread


df=pd.read_csv("attribute_stats_all_mls_2022_04_01_00_31_57.csv")
df=df[['OJO Source Name ','New Listings Requests','First Found - New']]
print(df.head(5))

gc = gspread.service_account(filename='credentials.json')

sh = gc.open("Performace_tracker")

worksheet =sh.add_worksheet(title="RAW1", rows=df.shape[0], cols=df.shape[1])
worksheet.update([df.columns.values.tolist()] + df.values.tolist())




