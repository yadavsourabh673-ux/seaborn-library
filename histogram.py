import seaborn as sns
import matplotlib.pyplot as plt


data = sns.load_dataset("tips")


sns.histplot(data=data, x="total_bill")

plt.show()