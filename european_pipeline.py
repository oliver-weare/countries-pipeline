import requests
import csv

try:
    response = requests.get('https://restcountries.com/v3.1/all')
    countries_data = response.json()

    european_countries = [country for country in countries_data if country.get('region') == 'Europe']

    csv_filename = 'data/european_countries.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['name', 'alpha2code', 'alpha3code', 'region', 'subregion', 'population']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for country in european_countries:
            writer.writerow({
                'name': country['name']['common'],
                'alpha2code': country['cca2'],
                'alpha3code': country['cca3'],
                'region': country['region'],
                'subregion': country['subregion'],
                'population': country['population']
            })

    print(f'European Countries successfully extracted, transformed and loaded into {csv_filename}')

except:
    print('Unable to run pipeline')