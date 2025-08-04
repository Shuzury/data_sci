from string import whitespace
from numpy import size
import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset('iris')
tip=sns.load_dataset("tips")
# print(tip.head()) #->total_bill     tip   sex   smoker  day    time  size
# print(iris.head()) #->sepal_length  sepal_width  petal_length  petal_width    species
# print(iris['species'].unique())
# sns.pairplot(iris)
'''PairGrid -> creates an empty frid where mo data is stored , its lie a pairplot with blank grids '''
# g=sns.PairGrid(iris)
# g.map(plt.scatter) # pura grid mey scatter plot laga deta hai 
# #for different graph types in diff regions , check below
# g.map_diag(sns.distplot)
# g.map_lower(sns.kdeplot)
# g.map_upper(plt.scatter)
## syntax-> g=sns.FacetGrid(data=,rows=,col=)
'''FacetGrid'''
# g=sns.FacetGrid(data=tip,col='time',row='smoker')
# g.map(sns.distplot,'total_bill')
'''Yes and No are the smokers and non smokers for 1st and 2nd row
    left col is lunch , right col are dinner
'''
## for doing the same thing with scatter , we need 2 arguements
# g=sns.FacetGrid(data=tip,col='time',row='smoker')
# g.map(plt.scatter,'total_bill','tip')

'''REGRESSION PLOTS'''
##linear model plot
#syntax-> hey chatgpt , yk , like the earlier syntaxes from your memory , make one for this too
# sns.lmplot(x='total_bill',y='tip',data=tip,hue='sex',markers=['o','v'],scatter_kws={'s':70})
#NOTE heyi chatgpt , explain markers and scatterkws 
''' segretaing by diff coloumns instead of hue '''
# sns.lmplot(x='total_bill',y='tip',data=tip,col='sex',row='time')
## combining col segregation with hue
# sns.lmplot(x='total_bill',y='tip',data=tip,col='day',hue='sex')
## using aspect and size ratio (NOTE-> size has been replaced with the word height)
# sns.lmplot(x='total_bill',y='tip',data=tip,col='day',hue='sex',aspect=0.6,height=7)
'''Style and colour'''
# sns.countplot(x='sex', data=tip) #plain simple grid
# syntax -> sns.set_style(style_name)
# sns.set_style('white')
# sns.set_style('ticks')
# sns.set_style('darkgrid')
# sns.set_style('whitegrid')
# NOTE- hey chatgpt , do add all the functions for each of these set_style
# sns.despine()# -> removes top and outer most sticks
# sns.despine(left=True,bottom=True) #-> removes mentioned sticks , here in this line , removes all sticks as top and right are treu bydefault
# plt.figure(figsize=(12,4)) #NOTE hey chatgpt , explain this one too
# sns.set_context('poster')  #preset sizing for posters , there are many other style names
# sns.set_context('poster',font_scale=3)  #NOTE hey chatgpt explain fontsize
# sns.countplot(x='sex', data=tip)

sns.lmplot(x='total_bill',y='tip',data=tip,hue='sex',palette='seismic') #NOTE hey chatgpt , name all the colourmaps and palletes in a markdown
plt.show()
