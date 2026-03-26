import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#line plot
x=[1,2,3,4,5,6]
y=[2,4,5,6,7,8]
data_1=pd.DataFrame({"x":x,"y":y})
sns.lineplot(x="x",y="y",data=data_1)
plt.show()

