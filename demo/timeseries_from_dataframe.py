"""
Timeseries from DataFrame
=========================

"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="darkgrid")

# Load the long-form example gammas dataset
# gammas = sns.load_dataset("gammas")

gammas = pd.read_csv("../seaborn-data-master/gammas.csv")
print gammas
# Plot the response with standard error
sns.tsplot(data=gammas, time="timepoint", unit="subject",
           condition="ROI", value="BOLD signal")

plt.show()



