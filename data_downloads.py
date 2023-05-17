import pandas as pd
import requests
import csv

api_key = 'a5f07203d4018f4d15e2c407b90b8d3a'
link = 'https://api.themoviedb.org/3/movie/top_rated?api_key=a5f07203d4018f4d15e2c407b90b8d3a&language=en-US&page=1'
response = requests.get(link)
print(response.headers)
result = response.json()["results"]
print(result)

#with open('result') as json_file:
#    data = json.load(json_file)

movie_csv_file = open('/users/paramjothchahal/desktop/movie_output.csv', 'w', newline='')
csv_write = csv.writer(movie_csv_file)

count = 0
for data in result:
    if count == 0:
        header = data.keys()
        csv_write.writerow(header)
        count += 1
    csv_write.writerow(data.values())
movie_csv_file.close()
