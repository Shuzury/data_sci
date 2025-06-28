# '''Merging and Joining'''
# # # pd.merge(df1,df2,on="comon col name",how="type of join") 
# ''' "common col name" is basically the key which will be used to merge
#     "how" has 4 types -> inner ,outer ,left ,right
# '''
# import pandas as pd
# df1 = pd.DataFrame({
#     'id': [1, 2, 3, 4, 5, 6, 7],
#     'name': ['Ram', 'Shyam', 'Geeta', 'Sita', 'Ravi', 'Neha', 'Amit']
# })
# df2 = pd.DataFrame({
#     'id': [1, 2, 3, 4, 6, 7],
#     'amount': [250, 400, 150, 600, 500, 450]
# }) #"5" number ko ura diya "df2" sey
# print("DataFrame 1:")
# print(df1)
# print("\nDataFrame 2:")
# print(df2)
# jor=pd.merge(df1,df2,on="id",how="inner")
# # inner -> ommits which doesnt match / missing 
# jor=pd.merge(df1,df2,on="id",how="outer")
# # outer -> fills with "NaN" which doesnt match / mmissing
# jor=pd.merge(df1,df2,on="id",how="left")
# # left  -> keeps values which mathcing left col
# jor=pd.merge(df1,df2,on="id",how="right")
# # right -> chatgpt please ake it
# jor=pd.merge(df1,df2,on="id",how="right")
# print("\nafter merging")
# print(jor)
'''cross join'''
# # comibnes 2 data sets and makes a cartisian product -> df1= m rows df2= n rows , cross join = m x n rows 


''' concatination '''
## verti -> row wise 
## horiz -> col wise 
## pd.concat([df1,df2],axis=0,ignore_index=True) #axis ->0 = row wise stack, 1 = col wise

import pandas as pd
df1=pd.DataFrame({
    "id":[1,2],
    "nam":["Raju","Rajiv"]    
})
df2=pd.DataFrame({
    "id":[3,4],
    "nam":["Isha","Ishan"]    
})
jora=pd.concat([df1,df2],axis=0,ignore_index=True)
print(jora)












