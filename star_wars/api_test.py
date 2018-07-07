
import requests

req = requests.get(url="https://swapi.co/api/films/")
film_json = req.json()
film_data = film_json['results']
# for i in ep_titles
# crawl = film_data['results']['opening_crawl']
for i in range(len(film_data)):
    print(film_data[i]['title'])
# print(film_data)

