'''
You shall have 2 DataFrames
• DataFrame 1: Customer profile
• DataFrame 2: Transaction histories

Goal: Use merge method to do the following -
Step 1 - Combine all customers based on Customer ID
Step 2 - Use concat() to make a new customer record and save it.

Use your knowledge about "cross", "inner", "outer", "left" and "right" merge.
concat() - axis=0/1, ignore_index=True
'''

import pandas as pd
df1=pd.DataFrame({
    "id":[1,2,3,4,5,6,7],
    "nam":["ram","sham","binod","sachiv","banrakas","rinki","pradhan"]
})
df2=pd.DataFrame({
    "id":[1,2,3,4,5,6,7],
    "maal":[101,202,7000,605,12,65,1000000]
})
print("Grahak suchi")
print(df1)
print("\nBikri suchi")
print(df2)
jor=pd.merge(df1,df2,on="id",how="inner")
print("\n combined \n",jor)
antim = pd.concat([df1, df2], axis=1, ignore_index=True)
print(" \n antim suchi",antim)
 ## or , below is a gpt code for just more sundarta 
'''
import pandas as pd

# ग्राहक सूची
df1 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7],
    "nam": ["ram", "sham", "binod", "sachiv", "banrakas", "rinki", "pradhan"]
})

# बिक्री सूची
df2 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7],
    "maal": [101, 202, 7000, 605, 12, 65, 1000000]
})

print("📋 ग्राहक सूची (df1)")
print(df1)

print("\n💰 बिक्री सूची (df2)")
print(df2)

# ✅ Step 1: Merge using 'id'
jor = pd.merge(df1, df2, on="id", how="inner")
print("\n🔗 संयुक्त सूची (Merge by 'id')")
print(jor)

# ✅ Step 2: Concat both DataFrames (not by id, just side-by-side)
antim = pd.concat([df1, df2], axis=1)
print("\n📚 अंतिम सूची (Concat by index, not 'id')")
print(antim)

''' 