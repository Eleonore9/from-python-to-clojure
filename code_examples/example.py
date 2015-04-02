import csv

## Looking at humanitarian data for 2014
## from the Emergency Events Database EM-DAT
## source: http://www.emdat.be/

def process_csv(filename):
    '''Open the file and build a list
    containing dictionnaries of data.'''
    list_data = []

    with open(filename, 'rb') as csvfile:
        content = csv.reader(csvfile)
        headers = content.next()
        data = content

        for row in data:
            dict_data = {}
            for i in range(len(headers)):
                dict_data[headers[i]] = row[i]
            list_data.append(dict_data)
    return list_data


def countries_affected(data):
    '''Search for countries with people
    affected and return them along with
    the cause.'''
    list_affected = []
    
    for element in data:
        if float(element['Total affected']) > 0:
            list_affected.append({
                'affected country': element['Country name'],
                'type disaster': element['disaster subgroup']
            })
    return list_affected
    


if __name__ == "__main__":
    disaster_data_2014 = process_csv('data.csv')
    #print len(disaster_data_2014)
    total_affected = countries_affected(disaster_data_2014)
    print '%d countries were affected by disasters in 2014' % len(total_affected)
    for r in total_affected:
        #print '%s was affected by a %s disaster' %(r.get('affected country'), r.get('type disaster'))
    
