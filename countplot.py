import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")


sns.countplot(data=data, x="day")

plt.show()