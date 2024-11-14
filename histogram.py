import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos (reemplaza 'tu_archivo.csv' con tu archivo)
df = pd.read_csv("covid-19.csv")

df = df[df['Age Group'] == 'All Ages']

df = df[df['State'] != 'United States']

# Definir constantes para las columnas
START_DATE = 'Start Date'
END_DATE = 'End Date'

# Convertir las fechas a formato datetime
df[START_DATE] = pd.to_datetime(df[START_DATE])
df[END_DATE] = pd.to_datetime(df[END_DATE])

# Crear una nueva columna con el trimestre
df['Quarter'] = pd.PeriodIndex(df[START_DATE], freq='Q')

# Agrupar los datos por trimestre y sumar las muertes

deaths_by_quarter = df.groupby('Quarter')['COVID-19 Deaths'].sum()

# Crear el histograma
plt.figure(figsize=(10, 6))
deaths_by_quarter.plot(kind='bar', color='skyblue', edgecolor='black')

# Personalizar el gráfico
plt.xlabel('Trimestre')
plt.ylabel('Número de Muertes por COVID-19')
plt.title('Frecuencia de Muertes por COVID-19 por Trimestre (2020-2023)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()