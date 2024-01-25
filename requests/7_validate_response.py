import json
import requests
from pprint import pprint
import jsondiff

def find_mismatched_data(url, file_name):
    response = requests.get(url)
    planets_response = response.json()['results']

    with open(file_name, 'r') as planets_data:
        planets_data = json.load(planets_data)
        planets_initial = planets_data['results']

    planets_final = {}
    keys = planets_initial[0].keys()

    for i in range(len(planets_initial)):
        list1 = []

        for j in keys:
            if planets_initial[i][j] != planets_response[i][j]:
                list1.append({j: {'Actual': planets_response[i][j], 'Expected': planets_initial[i][j]}})
                planet_name = planets_initial[i]['name']
                planets_final.update({planet_name: list1})

    return planets_final





if __name__=="__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))