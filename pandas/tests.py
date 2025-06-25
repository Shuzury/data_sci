# 🔃 Step 1: Import required library
import pandas as pd
# Sample data
data = {
    "Name": ['Shaunak', 'Sarthak', 'Ronit'],
    "Age": [10, 20, 30],
    "City": ['Shillong', 'Silchar', 'Hailakandi']
}

# Creating DataFrame
df = pd.DataFrame(data)
print(df)

# Save as CSV
df.to_csv("saving/pratham.csv", index=False)

# Save as Excel
df.to_excel("saving/pratham.xlsx", index=False)

# Save as JSON
df.to_json("saving/pratham.json", orient='records', lines=False)

print("✅ All files saved successfully!")
