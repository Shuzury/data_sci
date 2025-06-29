# #Lib load import kiya
import pandas as pd
import numpy as np

## load dataset
df=pd.read_csv('practice/indian_emp.csv')
# print(df.head()) # #helps to understand dataset ka structure i.e -> kya kya hai , col names

##check mising val "NaN"
# print("Gayab hai")
# print(df.isnull().sum()) # konse col mey kitne val missing hai dikhayega

# # gayab values ko bhar rahe hai
df["Salary (INR)"] = df["Salary (INR)"].fillna(df["Salary (INR)"].mean())
df["Performance Rating"] = df["Performance Rating"].fillna(df["Performance Rating"].median())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Experience (Years)"] = df["Experience (Years)"].fillna(df["Experience (Years)"].mean())


# # "inf" values ki bari-> unko humne nan sey replace kar diya so that woh bhi gayab values ban jaye 
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df[df.select_dtypes(include=[np.number]).columns] = df.select_dtypes(include=[np.number]).fillna(df.select_dtypes(include=[np.number]).mean())  #"inf" values to "nan", "nan" to mean of col

# # nakli ko hatayenge
df.drop_duplicates(inplace=True)

# # negative salaries ko thik karenge 
df["Salary (INR)"]=np.where(df["Salary (INR)"]<0,df["Salary (INR)"].mean(),df["Salary (INR)"]) # hey chatgpt do explain the function of this
df.to_csv("practice/saaf_kiya.CSV",index=False)
print("samapti")
