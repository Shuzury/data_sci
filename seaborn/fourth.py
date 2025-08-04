'''heat maps - for this , data should be in matrix form , more like functions , where pre image and image where used, more like co relation wala stuff'''
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import col
import seaborn as sns
tip=sns.load_dataset("tips") 
fly=sns.load_dataset("flights") 
'''check if loaded'''
# print(tip.head())
# print(fly.head())
'''Matrix plots''' 
# sns.pairplot(tip)
# print(tip.corr(numeric_only=True))
''' ".corr(numeric_only=True)" is more like the theorytical version of "pairplot" '''
tc=tip.corr(numeric_only=True)
# sns.heatmap(tc)
# sns.heatmap(tc,annot=True,cmap="coolwarm") # "annot" is ntg but basically prints the values in the heatmap, and "cmap=" is more like pallet for heatmaps
'''pivoting -> is basically creating a table using the available rows and cols and data from a df'''
# Syntax it is -> fly.pivot_table(index="",columns="",values="")
pas=fly.pivot_table(index="month",columns="year",values="passengers")
# print(pas)
# sns.heatmap(pas,cmap="magma",linewidths=0.5,linecolor="green") #linewidth -> is ntg but just seperates the boxes from direct contact, more like a border 
sns.clustermap(pas,cmap="coolwarm",linewidths=1,linecolor="white", standard_scale=1) # hey chatgpt , explain clustermap,standar_scale
plt.show()