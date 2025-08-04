'''Starts from 1:06:30'''
## Categorical plot
from re import split
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=sns.load_dataset("tips")  
# print(df.head())
'''COUNT PLOT'''
# sns.countplot(df["sex"],hue = df['smoker']) #NOTE-check ipynb file for more details
'''BAR PLOT'''
# sns.barplot(x=df["sex"],y=df["total_bill"])
# sns.barplot(x=df["sex"],y=df["total_bill"],estimator=np.sum) #total bil paid by male and female 
# sns.barplot(x=df["sex"],y=df["total_bill"],estimator=np.std) #total bil paid by male and female 
# NOTE - this shows the comparision between 2 contestents in 1 categories 

'''box plot'''
# sns.boxplot(x='day',y='total_bill',data=df,hue="smoker")
'''violin plot'''
# sns.violinplot(x="day",y="total_bill",data=df,palette='rainbow')
'''Strip plot'''
# sns.stripplot(x='day',y="total_bill",data=df, hue="sex")
'''swarm plot'''
# sns.swarmplot(x='day',y="total_bill",data=df,palette="rainbow") #combination of strip and violin plot
## ploting swarm above violin
# sns.violinplot(x='day',y="total_bill",data=df,palette="rainbow")
# sns.swarmplot(x='day',y="total_bill",data=df,color="black") 
'''Factor plot (name changed to catplot )'''
sns.catplot(x='day',y="total_bill",data=df,kind="bar")
plt.show()  
