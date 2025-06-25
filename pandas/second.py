import pandas as pd
df=pd.read_json("pract/sample_Data.json")

# print('Pehle 7 rows')
# print(df.head(7))

# print('Last ke 7 rows')
# print(df.tail(7))

# print('starting aur ending ke 5 values')
# print(df.head())
# print(df.tail())

# print("Yeh lo info of data set \n")
# print(df.info())




# data = {
#     "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
#     "Age" : [28,32,47,57,17,27,77,25],
#     "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
#     "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
# }

# df = pd.DataFrame(data)

# print("Created Dataset:")
# print(df)
# print(df.describe())