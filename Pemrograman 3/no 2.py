# Jawaban soal no 2

import pandas as pd

data = {'Buah': ['pisang', 'apel', 'rambutan'],
        'Harga/kilo': [15000, 20000, 35000]}
index = ['1', '2', '3']
index = ['1', '2', '3']
df = pd.DataFrame(data, index=index)

print('Perkalian')
df['Harga/kilo'] = df['Harga/kilo'] * 2
print(df)
print('============================')

print('Pembagian')
df['Harga/kilo'] = df['Harga/kilo'] / 2
print(df)
print('============================')

print('Penambahan')
df['Harga/kilo'] = df['Harga/kilo'] + 2000
print(df)
print('============================')

print('Pengurangan')
df['Harga/kilo'] = df['Harga/kilo'] - 1000
print(df)
