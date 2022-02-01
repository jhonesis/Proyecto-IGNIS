from parse import Parse
import pandas as pd
import seaborn as sns

parser1 = Parse(1000, "datos.txt")
csv_file1 = parser1.parse_file()
dataset1 = pd.read_csv(csv_file1, skiprows=1, header=0, index_col=0)
dataset1 = dataset1.drop(dataset1[(dataset1['Time (mS)']>400000) & (dataset1['Time (mS)']<450000) ].index)

parser2 = Parse(1000, "datos2.txt")
csv_file2 = parser2.parse_file()
dataset2 = pd.read_csv(csv_file2, skiprows=1, header=0, index_col=0)
dataset2 = dataset2.drop(dataset2[(dataset2['Time (mS)']>70000) & (dataset2['Time (mS)']<110000) ].index)

parser3 = Parse(1000, "datos3.txt")
csv_file3 = parser3.parse_file()
dataset3 = pd.read_csv(csv_file3, skiprows=1, header=0, index_col=0)

'''
promediomw=dataset1["Average POM_5V_IN Power Consumption (mW)"].mean()
promedioram=dataset1["Used RAM (MB)"].mean()
promedioc=dataset1["thermal Temperature (C)"].mean()
promediogpu=dataset1["Used GR3D (%)"].mean()

print(promediomw,promedioram,promedioc,promediogpu)

promedio=dataset1["thermal Temperature (C)"].mean()
maximo=dataset1["thermal Temperature (C)"].max()
minimo=dataset1["thermal Temperature (C)"].min()

print(promedio,maximo,minimo)'''

#sns.set(style="whitegrid", context="paper")
#sns.lineplot(x = 'Time (mS)', y = 'thermal Temperature (C)',data = dataset1, color = "y", Label ='Inception')
#sns.lineplot(x = 'Time (mS)', y = 'thermal Temperature (C)',data = dataset2, color = "c", Label ='Mobilenet')
#sns.lineplot(x = 'Time (mS)', y = 'thermal Temperature (C)',data = dataset3, color = "g", Label ='Ignis')


#dataset1.info()

