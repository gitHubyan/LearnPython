import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from sklearn import preprocessing

dataframe = pd.read_csv("../data/ppg2008.csv")
index = list(dataframe['Name  '])
columns = list(dataframe.columns.values)
df = dataframe.set_index('Name  ')
columns = columns[1:]

columMin = df.min(axis = 0)
cloumnMax = df.max(axis= 0)

df2 = df.sub(columMin, axis = 1)
df3 = df2.divide(cloumnMax, axis=1)

#df = pd.DataFrame(df, columns= columns[1:])
#columns = columns[1:]
#df = pd.DataFrame(dataframe, columns= columns)

print df3
yticks = df.columns
xticks = df.index;
#axx = plt.axes()
#print axx
ax = sns.heatmap(df3, yticklabels=xticks, xticklabels=yticks, linewidths= .3, cbar= False)
#ax.set_title("title")
plt.yticks(rotation=0)
plt.xticks(rotation=0)
plt.show()
