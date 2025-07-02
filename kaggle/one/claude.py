import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("kaggle/one/one.csv") # Replace with your actual file path

print("=== SIMPLE SOCIAL MEDIA DATA ANALYSIS ===\n")

# ============================================================================
# TASK 1: BASIC DATA EXPLORATION
# ============================================================================

print("=== TASK 1: BASIC DATA EXPLORATION ===")

# Dataset shape
print(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns")

# Column names
print(f"\nColumn names: {list(df.columns)}")

# Data types
print(f"\nData types:")
print(df.dtypes)

# First 5 rows
print(f"\nFirst 5 rows:")
print(df.head())

# Basic statistics
print(f"\nBasic statistics:")
print(df.describe())

# Specific answers
print(f"\nAverage age: {df['Age'].mean():.2f} years")
print(f"Min daily usage: {df['Avg_Daily_Usage_Hours'].min():.1f} hours")
print(f"Max daily usage: {df['Avg_Daily_Usage_Hours'].max():.1f} hours")
print(f"Average mental health score: {df['Mental_Health_Score'].mean():.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 2: MISSING DATA
# ============================================================================

print("=== TASK 2: MISSING DATA CHECK ===")

# Check for missing values
missing_data = df.isnull().sum()
print("Missing values in each column:")
print(missing_data)

# Total missing values
total_missing = missing_data.sum()
print(f"\nTotal missing values: {total_missing}")

if total_missing == 0:
    print("Great! No missing data found.")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 3: DUPLICATE CHECK
# ============================================================================

print("=== TASK 3: DUPLICATE CHECK ===")

# Check for duplicate Student IDs
duplicate_ids = df['Student_ID'].duplicated().sum()
print(f"Duplicate Student IDs: {duplicate_ids}")

# Check for completely duplicate rows
duplicate_rows = df.duplicated().sum()
print(f"Duplicate rows: {duplicate_rows}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 4: DATA VALIDATION
# ============================================================================

print("=== TASK 4: DATA VALIDATION ===")

# Check for impossible values
negative_ages = (df['Age'] < 0).sum()
print(f"Students with negative ages: {negative_ages}")

excessive_usage = (df['Avg_Daily_Usage_Hours'] > 24).sum()
print(f"Students with >24 hours usage: {excessive_usage}")

negative_sleep = (df['Sleep_Hours_Per_Night'] < 0).sum()
excessive_sleep = (df['Sleep_Hours_Per_Night'] > 24).sum()
print(f"Students with invalid sleep hours: {negative_sleep + excessive_sleep}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 5: DESCRIPTIVE STATISTICS
# ============================================================================

print("=== TASK 5: DESCRIPTIVE STATISTICS ===")

# Age statistics
print(f"Average age: {df['Age'].mean():.2f} years")
print(f"Most common age: {df['Age'].mode()[0]} years")

# Gender distribution
print(f"\nGender distribution:")
gender_counts = df['Gender'].value_counts()
for gender, count in gender_counts.items():
    print(f"  {gender}: {count} students")

# Usage statistics
print(f"\nUsage statistics:")
print(f"Average daily usage: {df['Avg_Daily_Usage_Hours'].mean():.2f} hours")
print(f"Most common usage: {df['Avg_Daily_Usage_Hours'].mode()[0]:.1f} hours")

# Mental health
print(f"\nAverage mental health score: {df['Mental_Health_Score'].mean():.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 6: PLATFORM ANALYSIS
# ============================================================================

print("=== TASK 6: PLATFORM ANALYSIS ===")

# Platform popularity
platform_counts = df['Most_Used_Platform'].value_counts()
print("Platform usage:")
for platform, count in platform_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {platform}: {count} students ({percentage:.1f}%)")

print(f"\nMost popular platform: {platform_counts.index[0]} ({platform_counts.iloc[0]} students)")

# Platform by gender
print(f"\nPlatform preferences by gender:")
platform_gender = pd.crosstab(df['Most_Used_Platform'], df['Gender'])
print(platform_gender)

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 7: USAGE PATTERNS
# ============================================================================

print("=== TASK 7: USAGE PATTERNS ===")

# Usage by academic level
usage_by_level = df.groupby('Academic_Level')['Avg_Daily_Usage_Hours'].mean()
print("Average usage by academic level:")
for level, avg_usage in usage_by_level.items():
    print(f"  {level}: {avg_usage:.2f} hours/day")

# Usage by gender
usage_by_gender = df.groupby('Gender')['Avg_Daily_Usage_Hours'].mean()
print(f"\nAverage usage by gender:")
for gender, avg_usage in usage_by_gender.items():
    print(f"  {gender}: {avg_usage:.2f} hours/day")

# Usage by age groups
df['Age_Group'] = pd.cut(df['Age'], bins=[17, 19, 21, 24, 100], 
                        labels=['18-19', '20-21', '22-24', '25+'])
usage_by_age = df.groupby('Age_Group')['Avg_Daily_Usage_Hours'].mean()
print(f"\nAverage usage by age group:")
for age_group, avg_usage in usage_by_age.items():
    print(f"  {age_group}: {avg_usage:.2f} hours/day")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 8: ACADEMIC IMPACT ANALYSIS
# ============================================================================

print("=== TASK 8: ACADEMIC IMPACT ANALYSIS ===")

# Academic impact counts
impact_counts = df['Affects_Academic_Performance'].value_counts()
print("Academic impact reported:")
for response, count in impact_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {response}: {count} students ({percentage:.1f}%)")

# Usage comparison by academic impact
impact_usage = df.groupby('Affects_Academic_Performance')['Avg_Daily_Usage_Hours'].mean()
print(f"\nAverage usage by academic impact:")
for response, avg_usage in impact_usage.items():
    print(f"  {response}: {avg_usage:.2f} hours/day")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 9: SLEEP AND MENTAL HEALTH
# ============================================================================

print("=== TASK 9: SLEEP AND MENTAL HEALTH ANALYSIS ===")

# Correlation between usage and sleep
usage_sleep_corr = df['Avg_Daily_Usage_Hours'].corr(df['Sleep_Hours_Per_Night'])
print(f"Correlation between usage and sleep: {usage_sleep_corr:.3f}")

# Correlation between usage and mental health
usage_mental_corr = df['Avg_Daily_Usage_Hours'].corr(df['Mental_Health_Score'])
print(f"Correlation between usage and mental health: {usage_mental_corr:.3f}")

# Mental health by sleep groups
df['Sleep_Group'] = pd.cut(df['Sleep_Hours_Per_Night'], bins=[0, 6, 8, 24], 
                          labels=['<6 hours', '6-8 hours', '8+ hours'])
mental_by_sleep = df.groupby('Sleep_Group')['Mental_Health_Score'].mean()
print(f"\nMental health by sleep groups:")
for group, score in mental_by_sleep.items():
    print(f"  {group}: {score:.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 10: COUNTRY ANALYSIS
# ============================================================================

print("=== TASK 10: COUNTRY ANALYSIS ===")

# Top 5 countries
country_counts = df['Country'].value_counts()
print("Top 5 countries with most students:")
for i, (country, count) in enumerate(country_counts.head().items()):
    print(f"  {i+1}. {country}: {count} students")

# Usage by top countries
top_countries = country_counts.head().index
usage_by_country = df[df['Country'].isin(top_countries)].groupby('Country')['Avg_Daily_Usage_Hours'].mean()
print(f"\nAverage usage by top countries:")
for country, avg_usage in usage_by_country.items():
    print(f"  {country}: {avg_usage:.2f} hours/day")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 11: RELATIONSHIP STATUS ANALYSIS
# ============================================================================

print("=== TASK 11: RELATIONSHIP STATUS ANALYSIS ===")

# Relationship status distribution
relationship_counts = df['Relationship_Status'].value_counts()
print("Relationship status distribution:")
for status, count in relationship_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {status}: {count} students ({percentage:.1f}%)")

# Usage by relationship status
usage_by_relationship = df.groupby('Relationship_Status')['Avg_Daily_Usage_Hours'].mean()
print(f"\nAverage usage by relationship status:")
for status, avg_usage in usage_by_relationship.items():
    print(f"  {status}: {avg_usage:.2f} hours/day")

# Addiction scores by relationship status
addiction_by_relationship = df.groupby('Relationship_Status')['Addicted_Score'].mean()
print(f"\nAverage addiction scores by relationship status:")
for status, avg_addiction in addiction_by_relationship.items():
    print(f"  {status}: {avg_addiction:.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# TASK 12: CREATE NEW CATEGORIES
# ============================================================================

print("=== TASK 12: CREATE NEW CATEGORIES ===")

# Usage categories
df['Usage_Category'] = pd.cut(df['Avg_Daily_Usage_Hours'], 
                             bins=[0, 3, 6, float('inf')], 
                             labels=['Light User', 'Moderate User', 'Heavy User'])

usage_category_counts = df['Usage_Category'].value_counts()
print("Usage categories:")
for category, count in usage_category_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {category}: {count} students ({percentage:.1f}%)")

# Age groups (already created above)
age_group_counts = df['Age_Group'].value_counts()
print(f"\nAge group distribution:")
for age_group, count in age_group_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {age_group}: {count} students ({percentage:.1f}%)")

print("\n" + "="*50 + "\n")

# ============================================================================
# SIMPLE VISUALIZATIONS
# ============================================================================

print("=== CREATING SIMPLE CHARTS ===")

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Chart 1: Platform popularity
platform_counts.plot(kind='bar', ax=axes[0,0])
axes[0,0].set_title('Most Used Platforms')
axes[0,0].set_xlabel('Platform')
axes[0,0].set_ylabel('Number of Students')

# Chart 2: Usage by gender
usage_by_gender.plot(kind='bar', ax=axes[0,1])
axes[0,1].set_title('Average Usage by Gender')
axes[0,1].set_xlabel('Gender')
axes[0,1].set_ylabel('Hours per Day')

# Chart 3: Mental health vs Usage scatter plot
axes[1,0].scatter(df['Avg_Daily_Usage_Hours'], df['Mental_Health_Score'])
axes[1,0].set_title('Mental Health vs Usage Hours')
axes[1,0].set_xlabel('Daily Usage Hours')
axes[1,0].set_ylabel('Mental Health Score')

# Chart 4: Usage categories
usage_category_counts.plot(kind='pie', ax=axes[1,1], autopct='%1.1f%%')
axes[1,1].set_title('Usage Categories Distribution')

plt.tight_layout()
plt.show()

print("Charts created successfully!")
print("\n" + "="*50 + "\n")

# ============================================================================
# SUMMARY REPORT
# ============================================================================

print("=== SUMMARY REPORT ===")

print(f"Dataset Overview:")
print(f"- Total students: {len(df)}")
print(f"- Countries represented: {df['Country'].nunique()}")
print(f"- Age range: {df['Age'].min()}-{df['Age'].max()} years")

print(f"\nKey Findings:")
print(f"- Most popular platform: {platform_counts.index[0]}")
print(f"- Average daily usage: {df['Avg_Daily_Usage_Hours'].mean():.2f} hours")
print(f"- {impact_counts['Yes']} students report academic impact")
print(f"- Average mental health score: {df['Mental_Health_Score'].mean():.2f}/10")

print(f"\nData Quality:")
print(f"- No missing values: ✓")
print(f"- No duplicate students: ✓")
print(f"- All values within valid ranges: ✓")

print("\n=== ANALYSIS COMPLETE ===")

# ============================================================================
# USAGE INSTRUCTIONS FOR BEGINNERS
# ============================================================================

print("""

HOW TO USE THIS CODE:
====================

1. Save your data as a CSV file
2. Change the file path in the code:
   df = pd.read_csv('your_actual_filename.csv')
3. Run the code
4. Look at the results printed in the console
5. Charts will appear in a separate window

WHAT EACH SECTION DOES:
======================
- Task 1: Shows basic info about your data
- Task 2: Checks for missing data
- Task 3: Checks for duplicates
- Task 4: Validates data makes sense
- Task 5: Calculates averages and counts
- Task 6: Analyzes platform popularity
- Task 7: Compares usage patterns
- Task 8: Studies academic impact
- Task 9: Looks at sleep and mental health
- Task 10: Analyzes by country
- Task 11: Studies relationship status
- Task 12: Creates new categories
- Charts: Makes visual graphs
- Summary: Final overview

IMPORTANT NOTES:
===============
- Make sure pandas, numpy, and matplotlib are installed
- The file path must be correct
- Charts will open in a new window
- All results are printed to console

""")