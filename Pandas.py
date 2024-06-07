import pandas as pd

df1= pd.read_csv('D:\Data Engineer - Alkemy\TP1\Sql\Resultados csv\7. Calcula el tiempo promedio de entrega de los pedidos por.csv')

df1.set_index('x', inplace=True)

