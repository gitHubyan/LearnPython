"""
Plotting a diagonal correlation matrix
======================================

_thumb: .3, .6
"""
from string import letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")

# Generate a large random dataset
rs = np.random.RandomState(33)
data = rs.normal(size=(100, 26))
columns =  list(letters[:26])
dataframe = pd.read_csv("data/ppg2008.csv")
print dataframe.to_records()

data = dataframe.to_records()
columns = list(dataframe.columns.values)

d = pd.DataFrame(data=data,
                 columns=columns)


print data

ax = sns.heatmap(data)
plt.show()

