from re import sub
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'mat_practice\ott.csv', encoding='latin1')
# #print(df.head())
# df=df.dropna(subset=['type','release_year','rating','country','duration']) # removing duplicates

# # number of TV shows and movies
'''
jat=df['type'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(jat.index, jat.values, color=['skyblue', 'lightgreen'])
plt.title('TV Show VS Movie ')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('mat_practice/figures/first.png', dpi=300, bbox_inches='tight')  # .show()
'''
