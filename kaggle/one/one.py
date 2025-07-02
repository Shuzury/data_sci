from os import dup
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


