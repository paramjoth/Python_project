import csv
from datetime import date, datetime
import os

todays_date = date.today()
todays_time = datetime.now()
print(todays_date)
print(todays_time)

path = '/users/paramjothchahal/desktop'
file_name = 'details.csv'
file_path = os.path.join(path, file_name)
file_base = os.path.basename(f'{file_path}')
file_dir = os.path.dirname(f'{file_path}')

print(file_path)
print(file_base)
print(file_dir)

with open(f'{file_path}', 'r') as rf:
    csv_read = csv.DictReader(rf)
    with open('details_copy.csv', 'w') as wf:
        fieldnames = ['firstname', 'email', 'phone']
        csv_write = csv.DictWriter(wf, fieldnames=fieldnames)
        for line in csv_read:
            del line['lastname']
            csv_write.writerow(line)
