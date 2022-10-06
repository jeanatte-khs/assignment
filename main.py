import os
import pandas as pd
from openpyxl import load_workbook
import os, glob

path = r'C:\\Users\\jeana\\PycharmProjects\\testtask'
directory = []
filename = []

for (root, dirs, file) in os.walk(path):
    for f in file:
        directory.append(root)
        filename.append(f)
        print(f)

df = pd.DataFrame(list(zip(directory, filename)), columns=['Directory', 'filename'])
df.to_excel('result.xlsx')
