import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('titanic.csv')

# print(df.head())

# print(df.info())

# print(df.describe())

# # Datatypes
# print(df.dtypes)

# # Filtro
# print(df[df['Age'] <= 10].head())

# duplicatesRows = df[df.duplicated()]
# print(len(duplicatesRows))


# print(len(df))

# df.drop_duplicates(keep='last', inplace=True)

# print(len(df))

# Substituindo NaN por 0
# df.replace(np.nan, '0', inplace=True)
# print(df)

# Renomear colunas
# df = df.rename(columns={'sex': 'Gender'})
# print(df.head(5))

# sorted_df = df.sort_values(by='Age', ascending=True)

# print(sorted_df)


# groupby
grouped_by = df.groupby('Age')

print(grouped_by.head())
