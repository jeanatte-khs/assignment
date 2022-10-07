import pandas as pd
import os, glob


path = r'C:\\Users\\jeana\\PycharmProjects\\testtask'
directory = []
filename = []
extensions = []

for (root, dirs, file) in os.walk(path):
    for f in file:
        directory.append(root)
        filename.append(f)
        ext = os.path.splitext(f)
        extensions.append(ext[1][1:])
        print(f)


df = pd.DataFrame(list(zip(directory, filename, extensions)), columns=['Directory', 'filename', 'extensions'])
df.to_excel('result.xlsx')
