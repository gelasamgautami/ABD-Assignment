import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv('E:/POOJA/ABD/DataFiles/Batting.csv')
df1=dataset.groupby('yearID')['playerID'].count()

df1.head(5)
plt.figure(figsize=(15,10),dpi=100)
plt.plot(df1,linestyle='dotted',marker='*',color='blue',label='Players')
plt.xlabel('Year')
plt.ylabel('Players included')
plt.show()
