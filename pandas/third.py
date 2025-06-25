import pandas as pd
'''
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
    "Age" : [28,32,47,57,17,27,77,25],
    "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
    "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}') #returns shape , arey wahi jo pehle numpy me sikha tha , notes dekh copy ka
## will return "Shape:Rows,Columns"
print(f'Column Names: {df.columns}') #coloumns ke nam bata ta hai , basically keys ke nam
'''

 # # problem statements
'''
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
    "Age" : [28,32,47,57,17,27,77,25],
    "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
    "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
}

df = pd.DataFrame(data)
# print("Sample Piece\n")
# print(df)
print("Accessing Single column \n")
nam=df["Name"]
print(nam)
print("\n\nAccessing Multiple column \n")
anek=df[["Name","Age"]]
print(anek)
# heyi chatgpt , do add a comment or markdown , which shows the general expression for the syntax of 'nam' and 'anek'
'''

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish','Raj', 'Simran'],
    "Age" : [28,32,47,57,17,27,77,25],
    "Salary": [5000, 6000, 45000, 5200, 4900, 7000, 9000, 17000],
    "Performance Score": [43, 71, 26, 59, 84, 38, 67, 22]  
}

df = pd.DataFrame(data)
# print(df)
print("Accessing column with Single conditions \n")
shabji=df[df['Salary']>6000] 
print(shabji)

print("\n Accessing column with two conditions \n")
sahab=df[df['Salary']>6000 & (df['Age']>27)]
print(sahab)
# heyi chatgpt , do add a comment or markdown , which shows the general expression for the syntax of 'sahab'

# Or use karna "|"
print("Accessing column using multiple conditions \n")
bare_sahab=df[df['Salary']>6000 | (df["Performance Score"]>43)]
print(bare_sahab)
# heyi chatgpt , do add a comment or markdown , which shows the general expression for the syntax of 'bare_sahab'