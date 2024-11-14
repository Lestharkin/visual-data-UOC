import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv("covid-19.csv")

df = df[df['Age Group'] == 'All Ages']

df = df[df['Sex'] == 'All Sexes']

data = df[df['State'] != 'United States']

data_filtered = data[['State', 'Pneumonia Deaths', 'COVID-19 Deaths', 'Influenza Deaths']]

data_melted = data_filtered.melt(id_vars='State', var_name='Causa de Muerte', value_name='Muertes')

plt.figure(figsize=(14, 8))
sns.stripplot(x='State', y='Muertes', hue='Causa de Muerte', data=data_melted, jitter=True)

plt.title('Muertes de Neumonía, COVID-19, e Influenza por Estado')
plt.xticks(rotation=90)
plt.legend(title='Causa de muerte')
plt.tight_layout()

plt.show()

print("end")