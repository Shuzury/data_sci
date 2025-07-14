from re import sub
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'mat_practice\ott.csv', encoding='latin1')
# #print(df.head())
df=df.dropna(subset=['type','release_year','rating','country','duration']) # removing duplicates

# # number of TV shows and movies
'''
jat=df['type'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(jat.index, jat.values, color=['skyblue', 'lightgreen'])
plt.title('TV Show VS Movie ')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.grid(True)
plt.show()
plt.savefig('mat_practice/figures/first.png', dpi=300, bbox_inches='tight')  
'''
## rating distributions
''' 
rate_count=df['rating'].value_counts()
plt.figure(figsize=(10, 5))
plt.pie(rate_count,labels=rate_count.index, autopct='%1.1f%%', startangle=90)
plt.title('Content rating distribution')
plt.tight_layout()
plt.savefig('mat_practice/figures/second.png', dpi=300, bbox_inches='tight')  
plt.show()
'''

## movie distribution using histogram
'''
cinema=df[df['type']=='Movie'].copy()
cinema['duration_int'] = cinema['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 5))
plt.hist(cinema['duration_int'], bins=30, color='lightcoral', edgecolor='black')
plt.title('Movie Duration Distribution')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of movies')
plt.tight_layout()
plt.grid(True)
plt.savefig('mat_practice/figures/third.png', dpi=300, bbox_inches='tight')
plt.show()
'''

 ## release year vs number of shows
'''
rel_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 5))
plt.scatter(rel_count.index, rel_count.values, color='purple')
plt.title('Number of Shows Released Each Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.grid(True)
plt.savefig('mat_practice/figures/fourth.png', dpi=300, bbox_inches='tight')
plt.show()
'''

### top 10 countries with most content
'''
desh_ginti = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 5))
plt.barh(desh_ginti.index, desh_ginti.values, color='orange')
plt.title('Top 10 Desh with Most Content')
plt.xlabel('Number of Shows')
plt.ylabel('Desh')
plt.tight_layout()
plt.grid(axis='x')
plt.savefig('mat_practice/figures/fifth.png', dpi=300, bbox_inches='tight')
plt.show()
'''

### Movies vs TV shows by release year

year= df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2,figsize=(14, 6))
# pratham subplot :cinemaaa
ax[0].plot(year.index, year['Movie'], color='lightblue')
ax[0].set_title('Movies per Year')
ax[0].set_xlabel('Saal')
ax[0].set_ylabel('Number of Movies')
# dusra subplot : Showssss
ax[0].plot(year.index, year['TV Show'], color='lightgreen')
ax[0].set_title('TV Shows per Year')
ax[0].set_xlabel('Saal')
ax[0].set_ylabel('Number of TV Shows')
# Optional: Leave second subplot blank or hide it
ax[1].axis('off')  # Hides the second subplot

fig.suptitle('Movies and TV Shows Released Each Year')
plt.tight_layout()
plt.savefig('mat_practice/figures/sixth.png', dpi=300, bbox_inches='tight')
plt.show()




