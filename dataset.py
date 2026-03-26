import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

pen=sns.load_dataset("penguins")
sns.lineplot(x="species",y="bill_length_mm",data=pen,hue="sex",color="red",style="sex",palette="Accent")
plt.grid()
plt.show()