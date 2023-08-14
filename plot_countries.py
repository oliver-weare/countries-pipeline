import matplotlib.pyplot as plt
import csv

try: 
    data = []
    with open('data/european_countries.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
        
        sorted_data = sorted(data, key=lambda x: float(x['population']), reverse=True)

        top_10 = sorted_data[:10]

    x = [row['name'] for row in top_10]
    y = [int(row['population']) for row in top_10]

    plt.bar(x, y, color = 'g', width = 0.50, label = 'Population')

    plt.xlabel('Countries')
    plt.ylabel('Populations (Billions)')
    plt.title('Top 10 Highest Populated European Countries')

    plt.legend()
    plt.show()

except:
    print('Unable to plot csv contents')