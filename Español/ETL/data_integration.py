import pandas as pd
import unicodecsv as csv

#Se toman tres bases de datos con una estructura similar, se buca unificarlas y obtener una base tal que Phone 1 - Type sea el dato relevante
#las bases quedan unificadas en un misma base respetando en mayor posibilidad la estructura

data_0 = pd.read_csv('Cocorna_phone_numbers_consolidated.csv', usecols=['Name', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value'], encoding='utf-8')
data_1 = pd.read_csv('Cocorna_phone_numbers_enlaces.csv', usecols=['Name', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value'], encoding='utf-8')
data_2 = pd.read_csv('Cocorna_phone_numbers_people.csv', usecols=['Name', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value'], encoding='utf-8')

tel_filtered = []
data_filtered = []

def tel_rastering (database, i):
    value = False
    for j in tel_filtered:
        if (database[i] == j):
            value = True
    return value

def filtering (data):
    for i in range(0, len(data)):
        if (tel_rastering(data['Phone 1 - Value'], i) != True):
            tel_filtered.append(data['Phone 1 - Value'][i])


with open('Cocorna_phone_numbers_integrated.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(data_0)):
        if (tel_rastering(data_0['Phone 1 - Value'], i) != True):
            tel_filtered.append(data_0['Phone 1 - Value'][i])
            writer.writerow([data_0['Name'][i], '* myContacts', 'Mobile', data_0['Phone 1 - Value'][i]])
    for i in range(0, len(data_1)):
        if (tel_rastering(data_1['Phone 1 - Value'], i) != True):
            tel_filtered.append(data_1['Phone 1 - Value'][i])
            writer.writerow([data_1['Name'][i], '* myContacts', 'Mobile', data_1['Phone 1 - Value'][i]])
    for i in range(0, len(data_2)):
        if (tel_rastering(data_2['Phone 1 - Value'], i) != True):
            tel_filtered.append(data_2['Phone 1 - Value'][i])
            writer.writerow([data_2['Name'][i], '* myContacts', 'Mobile', data_2['Phone 1 - Value'][i]])
print(len(tel_filtered))
