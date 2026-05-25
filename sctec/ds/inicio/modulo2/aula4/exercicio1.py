#1. Faça o download desta base de dados e leia com pandas:
# https://www.kaggle.com/datasets/raphaelmanayon/temperature-and-ice-cream-sales

#2. Em seguida, mostre na tela os valores ordenados da coluna de temperatura.

import pandas as pd

df = pd.read_csv('ice_cream_sales.csv')

sorted_df = df.sort_values(by='Temperature', ascending=True)

print(sorted_df['Temperature'])
