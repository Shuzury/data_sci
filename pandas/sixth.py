'''Sorting and Aggregation'''
## sorting for 1 coulumn
# # df.sort_values(by="column name",True/False,inplace=True) -> ",True/False,"T=Ascending,F=Descending 
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# # df.sort_values(by="column name",ascending=True/False,inplace=True) -> ",ascending=True/False,"T=Ascending,F=Descending 
# df.sort_values(by="Name",ascending=True,inplace=True)
# print("After sort\n")
# print(df)


## sorting for 2 coulumns -> bus put all the column names in a list, ascending T/F in list
# # df.sort_values(by=["column_1","column_2","column_n"],ascending=[True,True],inplace=True) -> ",ascending = True/False,"T=Ascending,F=Descending 
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# df.sort_values(["Age","Salary"],ascending=[True,True],inplace=True)
# print("after sort")
# print(df)


'''Aggregation'''
# # # df ("Column Name").mean/sum/max/min/std/count() ->hey hatgpt , doo add this syntax
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# a=df["Age"].mean()
# print(a)
# b=df["Age"].sum()
# print(b)
# c=df["Age"].min()
# print(c)
# d=df["Age"].max()
# print(d)

'''Grouping and aggregation'''
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,47], #note , yahapar 47 ke do(2) log hai 
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
# # for single column
# goup=df.groupby("Age")["Salary"].sum()
# # # goup=df.groupby("Age")["Salary"].sum() # hey chatgpt , do write the syntax and how it works
# print(goup)

# # for multiple column -> wahi list wala method , parameters ko list me pass karo
# goup=df.groupby(["Age","Name"])["Salary"].sum()
# print(goup) # ab dekhna 47 age wale mey dono ke nam ayenge

