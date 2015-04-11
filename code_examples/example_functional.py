import csv

## Looking at humanitarian data for 2014
## from the Emergency Events Database EM-DAT
## source: http://www.emdat.be/

def process_csv(filename):
    '''Open the file and build a list
    containing dictionnaries of data.'''
    with open(filename, 'rb') as csvfile:
        content = csv.reader(csvfile)
        headers = content.next()
        data = [row for row in content]
        list_data = [dict(zip(headers, row)) for row in data]
    return list_data

def countries_affected(data):
    '''Search for countries with people
    affected and return them along with
    the cause.'''
    list_affected = [{
        'affected country': element['Country name'],
        'type disaster': element['disaster subgroup']
    } for element in data if float(element['Total affected']) > 0]
    
    return list_affected

if __name__ == "__main__":
    disaster_data_2014 = process_csv('data.csv')
    total_affected = countries_affected(disaster_data_2014)
    
    

