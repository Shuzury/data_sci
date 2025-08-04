import seaborn as sns
import matplotlib.pyplot as plt
# syntax ->sns.load_dataset("name_of_dataset") -> loads a dataset from seaborn's github repository
a=sns.load_dataset("tips")
# print(a.head())
# a['size'].unique()  # returns unique values in the 'size' column
#  here we see that only "total bill" and "tip" is quantitative , so we will use this 2 to prepare distribution plot 
# sns.displot(a['total_bill'])  
# sns.distplot(a["total_bill"])
#NOTE heyi chatgpr , explain distplot and displot and if needed , write more codes for clarification
## NOTE - KDE stands for Kernel Density Estimate , also known as bell curve -> adds a free hand line for estimate
# sns.displot(a['total_bill'], kde=True)  # kde=True adds a free hand line for estimate
# # sns.displot(a['total_bill'],bins=5)  # note-> bins are the number of bars in the graph, by default it is 10 or 20
# plt.subplot(1, 2, 1)  
# sns.histplot(a['total_bill'], kde=True)
# plt.subplot(1, 2, 2)  
# sns.histplot(a['tip'], kde=True)
## NOTE subplot is same as matlab wala
## joint plot ->2 graph ke maal ko ek he graph me plot karna
#syntax -> sns.jointplot(x='column1', y='column2', data=dataset, kind='type of graph', color='red')
# sns.jointplot(x='total_bill', y='tip', data=a, kind='scatter', color='red')  # kind can be 'scatter', 'kde', 'hist', 'reg' etc.
# sns.jointplot(x='total_bill', y='tip', data=a, kind='hist', color='red')  
# sns.jointplot(x='total_bill', y='tip', data=a, kind='kde', color='red')  
# sns.jointplot(x='total_bill', y='tip', data=a, kind='reg', color='red')  
## pairplot -> scatter plot of all the columns with respect to each other using bar and continued free hand line
# sns.pairplot(a) 
# sns.pairplot(a,hue='sex') #hue is basically used to differentiate the plots based on some key
# sns.pairplot(a,hue='size',palette='rainbow') #pallette is used to set hue coloure from default gradient to rainbow or any other gradient
## NOTE scatter plot -> 2 variables ke beech ka relation dekhne ke liye
sns.rugplot(a) 


plt.show()
