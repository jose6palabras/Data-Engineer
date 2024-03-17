import pandas as pd
import unicodecsv as csv

#se filtra cada base de datos, se le da una organizacion dependiendo de la zona de residencia y un detalle que permita ubicar
#luego se escribe una base nueva filtrada con los datos filtrados para luego ser unificada con otra base.
data = pd.read_csv('db_cocorna_enlaces.csv', usecols=['TEL', 'NOM1', 'NOMBARRIO', 'NOMVEREDA'], encoding='utf-8')
tel_filtered = []
data_filtered = []

def rastering (numero):
    value = False
    for j in tel_filtered:
        if (data['TEL'][numero] == j):
            addMemberAndLabel(numero, 'No')            
            value = True
            return value

def addNewNumber (numero):
    json_model = {
        'number': 0,
        'label': "",
        'members': [],        
        'location': ""
        }
    json_model['number'] = data['TEL'][numero]
    json_model.get('members').append(data['NOM1'][numero])
    var_location = selectLocation(numero)
    json_model['location'] = var_location
    json_model['label'] = addMemberAndLabel(numero, var_location)

    data_filtered.append(json_model) 

    tel_filtered.append(data['TEL'][numero])

def addMemberAndLabel (numero, location):
    j = 1
    for i in data_filtered:
        if (data['TEL'][numero] == i.get('number')):
            i.get('members').append(data['NOM1'][numero])    
        if (location == i.get('location')):
            j += 1
    mensaje = "Familiae" + " " + location + " " + str(j)
    return mensaje        

def selectLocation (numero):
    if (data['NOMBARRIO'][numero] == 'SIN CORREGIMIENTO'):
        location = data['NOMVEREDA'][numero]
        return location
    else:
        location = data['NOMBARRIO'][numero]
        return location   

for i in range (0, len(data)):
    if (len(str(data['TEL'][i]))==10):
        if (rastering(i) != True):
            addNewNumber(i)


with open('Cocorna_phone_numbers_enlaces.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(data_filtered)):
        writer.writerow([data_filtered[i].get('label'), '* myContacts', 'Mobile', data_filtered[i].get('number')])

