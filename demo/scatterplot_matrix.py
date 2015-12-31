import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import pandas as pd
df = pd.read_csv("../seaborn-data-master/iris.csv")
#dff = df.to_records()
#print len(dff)
#print len(dff[0])
#print dff[0][2]
#print dff[0][4]

sns.pairplot(df, hue="species")
plt.show()



# df = pd.read_csv("../data/ppg2008.csv")
# sns.pairplot(df, hue="Name")
# plt.show()
