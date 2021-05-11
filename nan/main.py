import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer

'''
    name: Julia Kimura Silva
    ra: 585890
'''

data = pd.DataFrame({
    "Nome": ['Breach', 'Yoru', 'Sage', 'Viper', 'Reyna', 'Raze', 'Jett', 'Killjoy'],
    "Nota_1": [np.nan, 10, 8, 9.4, 7, 5, np.nan, 10],
    "Nota_2": [4, 8, np.nan, 10, 10, 10, 8, np.nan],
    "Idade": [40, 18, np.nan, 26, 25, 21, 20, np.nan],
    "Peso": [80, 60, 52, np.nan, 60, 70, np.nan, 50],
    "Turma": ["Ascent", "Bind", "Ascent", np.nan, "Bind", "Ascent", np.nan, "Ascent"]
})

print('Antes do Tratamento')
print(data)

frequentes = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
media = SimpleImputer(missing_values=np.nan, strategy='mean')
mediana = SimpleImputer(missing_values=np.nan, strategy='median')
constantes = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)

data.Nota_1 = constantes.fit_transform(data[['Nota_1']])
data.Nota_2 = constantes.fit_transform(data[['Nota_2']])
data.Turma = frequentes.fit_transform(data[['Turma']])
data.Idade = mediana.fit_transform(data[['Idade']])
data.Peso = media.fit_transform(data[['Peso']])

print('Depois do Tratamento')
print(data)