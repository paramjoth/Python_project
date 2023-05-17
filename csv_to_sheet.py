import pandas as pd
import gspread


df=pd.read_csv("attribute_stats_all_mls_2022_04_01_00_31_57.csv")
df=df[['OJO Source Name ','New Listings Requests','First Found - New']]
Plaid_feeds = ['al_bamls','ca_tcmls','fl_nefmls','ma_bcmls','mt_nmar','tn_maar','va_rvar']
df.insert(1, 'pipeline', 'Pyrets')
print(df.head(5))

for i in range(len(df['OJO Source Name '])):
    if df['OJO Source Name '][i] in Plaid_feeds:
        df['pipeline'][i] = 'Plaid'
    else:
        df['pipeline'][i] = 'Pyrets'


print(df.head(5))

gc = gspread.service_account(filename='credentials.json')
sh = gc.open("Performace_tracker")
worksheet = gc.open("Performace_tracker").worksheet("RAW1")
worksheet.clear()
worksheet.update([df.columns.values.tolist()] + df.values.tolist())
#gc.open("Performace_tracker").del_worksheet(worksheet)

#new_sheet = sh.add_worksheet(title="RAW1", rows=df.shape[0], cols=df.shape[1])
#new_sheet.update([df.columns.values.tolist()] + df.values.tolist())

#sh.update([df.columns.values.tolist()] + df.values.tolist())




