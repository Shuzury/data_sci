'''missing data Detection '''
''' deleting or removing unwanted columns'''
# import pandas as pd
# data = {
#     "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,None,47,57,17,27,77,25],
#     "Salary": [5000, None, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, None, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)

# print(df.isnull()) #will return "True" jaha par "None" ya fir koi val nehi hai , jaha val hai waha "False"
# print(df.isnull().sum) #will return total number of missing val


'''Handling missing values by Removing and Filling'''
# #Removing -> dropna()
# import pandas as pd
# data = {
#     "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,None,47,57,17,27,77,25],
#     "Salary": [5000, None, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, None, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# # # df.dropna(axis=0,inplace=True) #axis = 0 -> "Rows" delete, axis = 1 -> "Columns" delete
# # # df.dropna(inplace= True) #will delete irrespective of rows or columns
# df.dropna(inplace=True)
# print(df)

# #Filling -> fillna()
# import pandas as pd
# data = {
#     "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,None,47,57,17,27,77,25],
#     "Salary": [5000, None, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, None, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# # # df.fillna(value,inplace=True) # value is the one which will replace the missing values, it can be any dfata type i.e string/int
# # df.fillna(77,inplace=True) #fills all blanks irrespective of mention
# # # df['Col_name'].fillna(value_eqn,inplace=True) -> filling with logical values
# df['Age'].fillna(df['Age'].mean(),inplace=True) #fills "Age" col with specified values jaise ki yaha par mean of all age
# df['Salary'].fillna(df['Salary'].mean(),inplace=True) #same but for "Salary" here
# print(df) 


'''Interpolation - > heyi chatgpt , do write more about interpolation in pandas  here'''
# from encodings.punycode import T
# import pandas as pd
# data = {
#     "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,None,47,57,17,27,77,25],
#     "Salary": [5000, None, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, None, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# # # heyi chatgpt , do explain all the 3 interpolation methods(Linear,polynomial,time) here
# # #df.interpolate(method="anyout of 3",axis,inplace)
# df.interpolate(method="linear",axis=0,inplace=True)  
# #yeh axis and inplace  hata dena agar pure ke liye apply karna hai toh
# print(df)

''' Better example '''
import pandas as pd
data= {
    "time":[1,2,None,4,None,7,None,10],
    "val":[10,20,30,40,50,60,70,100]
}
df=pd.DataFrame(data)
print(df)
print("After changes\n")
# df["time"]=df["time"].interpolate(method="linear")
df["time"] = df["time"].interpolate(method="polynomial", order=2)
# df["time"] = df["time"].interpolate(method="time") # heyi chatgpt do remeber this doesnt work here , only works in date and time format
print(df)












