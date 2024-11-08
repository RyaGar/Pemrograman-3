# Jawaban soal no 3

import numpy as np
import pandas as pd


data = {
        'Nama': ['Juned', 'Fikri', 'Adam', 'Tansyah', 'Egi', 'Nisa', 'Nenden', 'Aas', 'Fitri', 'Yulia'],
        'Alamat': ['Palintang', 'Langen Sari', 'kosambi','Batu Lonceng', 'Babakan', 'Babakan', 'Dago', 'Batu Asih', 'Cijerokaso', 'Cibeunying'],
        'Penghasilan/bulan': [2000000, 3000000, 8000000, 10000000, 6000000, 5000000, 1000000, 9000000, 12000000, 15000000]
        }

index = ['1', '2', '3','4','5','6','7','8','9','10']
df = pd.DataFrame(data, index=index)

# Menampilkan semua data
print("Semua data:")
print(df)
print('=============================================')

# Mengurutkan data
df_sorted = df.sort_values(by='Penghasilan/bulan')

# Menampilkan 5 data teratas
print("5 data teratas:")
print(df_sorted.head())
print('=============================================')

# Menampilkan 5 data terbawah
print("5 data terbawah:")
print(df_sorted.tail())