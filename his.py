import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

df=sns.load_dataset("penguins")
sns.displot(df["bill_length_mm"],bins=[35,38,40,42,45],kde=True,color="red",rug=True)
plt.show()