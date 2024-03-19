import pandas as pd
#this is a testing code
data = pd.read_csv('bdtest.csv', usecols=['Display Name'], encoding='utf-8')

for i in data['Display Name']:
    print(i) 