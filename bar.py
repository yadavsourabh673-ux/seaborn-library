import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

order_1=["female","male"]

df=sns.load_dataset("tips")
sns.barplot(x="day",y="tip",color="red",data=df,hue="sex",ci=90 )
plt.show()