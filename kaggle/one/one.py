import numpy as np
import pandas as pd 

df=pd.read_csv("kaggle/one/one.csv")
'''1. Basic Data Exploration'''
# print(df.info())
# print(df.head())
# print(df.tail())
# print(df["Age"].mean())
# print(df["Avg_Daily_Usage_Hours"].max())
# print(df["Avg_Daily_Usage_Hours"].min())
# print(df["Mental_Health_Score"].mean())

'''2. Missing Data Investigation'''
# print(df.isnull().sum())

'''3. DUPLICATE CHECK'''
# duplicate_ids = df['Student_ID'].duplicated().sum()
# print(duplicate_ids)
# duplicate_rows = df.duplicated().sum()
# print(duplicate_rows)

'''4. DATA VALIDATION'''
# na = (df['Age'] < 0).sum()
# print(na)
# eu = (df['Avg_Daily_Usage_Hours'] > 24).sum()
# print(eu)
# ns = (df['Sleep_Hours_Per_Night'] < 0).sum()
# es = (df['Sleep_Hours_Per_Night'] > 24).sum()
# print(ns)
# print(es)

'''5. DESCRIPTIVE STATISTICS'''
# print(df["Age"].mean())
# print(df["Age"].mode()[0])
# print(df["Gender"].value_counts())
# print(df["Avg_Daily_Usage_Hours"].mean())
# print(df["Avg_Daily_Usage_Hours"].mode()[0])
# print(df["Mental_Health_Score"].mean())

'''6. Platform Stats'''
# pf = df['Most_Used_Platform'].value_counts()
# print(pf)
# print(pf.idxmax(), pf.max())
# print(pd.crosstab(df['Most_Used_Platform'], df['Gender']))

''' 7. Usage Patterns '''
# print(df.groupby('Academic_Level')["Avg_Daily_Usage_Hours"].mean())
# print(df.groupby('Gender')["Avg_Daily_Usage_Hours"].mean())
# df["Age_Group"] = pd.cut(df["Age"], bins=[17, 19, 21, 24, 100], labels=["18-19", "20-21", "22-24", "25+"])
# print(df.groupby("Age_Group")["Avg_Daily_Usage_Hours"].mean())

'''8. Academic Impact'''
# print(df['Affects_Academic_Performance'].value_counts())
# print(df.groupby('Affects_Academic_Performance')['Avg_Daily_Usage_Hours'].mean())

'''9. Sleep & Mental Health'''
# print(df["Avg_Daily_Usage_Hours"].corr(df["Sleep_Hours_Per_Night"]))
# print(df["Avg_Daily_Usage_Hours"].corr(df["Mental_Health_Score"]))
# df["Sleep_Group"] = pd.cut(df["Sleep_Hours_Per_Night"], bins=[0, 6, 8, 24], labels=["<6", "6-8", "8+"])
# print(df.groupby("Sleep_Group")["Mental_Health_Score"].mean())

'''10. Country Analysis'''
# ct = df["Country"].value_counts()
# print(ct.head())
# top = ct.head().index
# print(df[df["Country"].isin(top)].groupby("Country")["Avg_Daily_Usage_Hours"].mean())

'''11. Relationship Status'''
# rs = df["Relationship_Status"].value_counts()
# print(rs)
# print(df.groupby("Relationship_Status")["Avg_Daily_Usage_Hours"].mean())
# print(df.groupby("Relationship_Status")["Addicted_Score"].mean())

'''12. New Categories'''
# df["Usage_Category"] = pd.cut(df["Avg_Daily_Usage_Hours"], bins=[0,3,6,float("inf")], labels=["Light","Moderate","Heavy"])
# print(df["Usage_Category"].value_counts())
# print(df["Age_Group"].value_counts())

