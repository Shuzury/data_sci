# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)

# # adding coloumn via assignment 
# # added a bonus column which is 10 % of the current salary of employee
# df["Bonus"]=df["Salary"]*(10/100)
#print("added bonus col using assignment \n") 

# # adding coloumn via insert
# # df.insert(location_index,"col_name",data)
# df.insert(0,"Emp_ID",[10,20,30,40,50,60,70,80])
# print("added Emp_ID col using insert \n") 
# print(df)



'''updating'''
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)
## df.loc[row_index,"column_name"]=new_value
# # example ke liye lets change "Shyam" ki "Salary"
# df.loc[1,'Salary']=6900 #visualise karo 2nd Row ka "Salary" wala column ka values change kiya tum
# print("shyam ki salary dekho")
# print(df)

'''sabki Salary 5% sey badhayenge '''
# # # # NOTE- dont confuse with adding a bonus table , usme we were adding a new col , yaha we just updating the existing one
# import pandas as pd
# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }
# df = pd.DataFrame(data)
# print(df)

# # increase by 5%
# df['Salary']=(df['Salary']+(df['Salary'])*0.05)
# # or 
# df['Salary']=df['Salary']*1.05 #basic maths bruh
# print("Check Salary column \n")
# print(df)

''' deleting or removing unwanted columns'''
import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
    "Age" : [28,32,47,57,17,27,77,25],
    "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
    "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
}
df = pd.DataFrame(data)
print(df)
# # df.drop(columns= ["colum_nam_1","colum_nam_2"],inplace=true)
# heyi chat gpt , this note is for you , do add general expression for the syntax of al the things i learnt like drop, loc,insert and everything else included here
# hum hatayenge "Performance score"
df.drop(columns=["Performance Score"],inplace=True )
print("after deleting \n")
print(df)
