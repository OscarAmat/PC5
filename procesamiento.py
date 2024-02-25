import pandas as pd

data=pd.read_excel('data/reactiva.xlsx',sheet_name="TRANSFERENCIAS 2020",header=0)

from unidecode import unidecode

def eliminar_tildes(texto):
    return unidecode(texto)

def clean_column_name(name):
    # Remove spaces and tildes
    cleaned_name = name.replace(' ', '').lower()
    return cleaned_name

data.rename(columns=eliminar_tildes, inplace=True)
data.rename(columns=clean_column_name, inplace=True)


del data['id']
del data['tipomoneda']


data['dispositivolegal']=data['dispositivolegal'].replace({'0m':''},regex=True)

import requests
url="https://api.apis.net.pe/v1/tipo-cambio-sunat"
response=requests.get(url)


respuesta = response.json()
respuesta['compra']
data['montodeinversion_usd']=data['montodeinversion'].apply(lambda x:x/respuesta['compra'])
data['montodetransferencia_usd']=data['montodetransferencia2020'].apply(lambda x:x/respuesta['compra'])



data['estado'].value_counts()
data['puntuacion_estado']=data['estado'].apply(lambda x: 1 if x=='Actos Previos' else ( 2 if x=='En Ejecución' else ( 3 if x=='Concluido' else 0)) )

data['puntuacion_estado'].value_counts()
 
print(data.head())


