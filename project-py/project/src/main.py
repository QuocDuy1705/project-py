import pandas as pd
import math
import csv
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Bai tap 1: Ma va To Chuc du lieu
df = pd.read_csv('E:/project/data/dataset.csv')
# Them du lieu vao
data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age' : [25, 30, 35,],
        'Salary' : [50000, 60000, 70000]}
# Tao file CSV
df = pd.DataFrame(data)
# Luu tru file
df.to_csv('E:/project/output/result.csv', index=False)
# Bai tap 3: Luu tru va sap xep du lieu
my_list = [ 3, 1, 2, 5, 4]
my_list.sort()
print("Danh sach da duoc sap xep: ", my_list)

data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age' : [25, 30, 35],
        'Salary' : [50000, 60000, 70000]}



# Bai tap 4: Khoa hoc du lieu voi Python
df = pd.read_csv('E:/project/data/dataset.csv')


# Ve bieu do phan phoi tuoi
plt.hist(data['Age'], bins = 10)
plt.title('Phan phoi tuoi')
plt.xlabel('Tuoi')
plt.ylabel('Tan suat')
plt.show()
