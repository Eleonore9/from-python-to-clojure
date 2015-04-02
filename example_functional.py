import csv

def process_csv(filename):
    with open(filename, 'rb') as csvfile:
        content = csv.reader(csvfile)
        headers = content.next()
        data = [row for row in content]
        list_data = [dict(zip(headers, row)) for row in data]
    return list_data

if __name__ == "__main__":
    disaster_data_2014 = process_csv('data.csv')

