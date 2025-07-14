# 🎬 OTT Data Analysis with Matplotlib

A comprehensive data visualization project analyzing OTT (Over-The-Top) platform content using Python's Matplotlib library. This project explores various aspects of streaming platform data through multiple visualization techniques.

## 📊 Project Overview

This analysis examines an OTT platform dataset to uncover insights about content distribution, ratings, duration patterns, release trends, and geographical content production. The project demonstrates proficiency in data manipulation with Pandas and data visualization with Matplotlib.

## 🎯 Key Visualizations

### 1. TV Shows vs Movies (Bar Chart)
- **Analysis**: Content type distribution comparison
- **Insight**: Movies significantly outnumber TV shows by more than double
- **File**: [`figures/first.png`](figures/first.png)

### 2. Content Rating Distribution (Pie Chart)
- **Analysis**: Distribution of content ratings across the platform
- **Insight**: TV-MA is the most common rating, followed by TV-14 and R, indicating focus on mature audiences
- **File**: [`figures/second.png`](figures/second.png)

### 3. Movie Duration Distribution (Histogram)
- **Analysis**: Distribution of movie runtime lengths
- **Insight**: Most movies cluster around 90-110 minutes with near-normal distribution
- **File**: [`figures/third.png`](figures/third.png)

### 4. Shows Released Per Year (Scatter Plot)
- **Analysis**: Number of shows released per year over time
- **Insight**: Significant growth from 2010 onwards, peaking before 2020
- **File**: [`figures/fourth.png`](figures/fourth.png)

### 5. Top 10 Content-Producing Countries (Horizontal Bar Chart)
- **Analysis**: Top 10 countries by content volume
- **Insight**: United States leads, followed by India and United Kingdom
- **File**: [`figures/fifth.png`](figures/fifth.png)

### 6. Movies vs TV Shows Timeline (Subplot)
- **Analysis**: Year-wise comparison of content types
- **Insight**: Movies consistently outnumber TV shows across all years with parallel growth patterns
- **File**: [`figures/sixth.png`](figures/sixth.png)

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization and plotting
- **CSV** - Data source format

## 📁 Project Structure

```
mat_practice/
├── pract.ipynb          # Main analysis notebook
├── ott.csv              # Dataset file
├── figures/             # Generated visualizations
│   ├── first.png        # TV Shows vs Movies
│   ├── second.png       # Rating distribution
│   ├── third.png        # Movie duration histogram
│   ├── fourth.png       # Release trends scatter plot
│   ├── fifth.png        # Top countries bar chart
│   └── sixth.png        # Movies vs Shows timeline
└── README.md            # Project documentation
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib
```

### Running the Analysis
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mat_practice
   ```

2. **Update file paths** in `pract.ipynb` to match your local directory structure

3. **Execute the notebook**
   ```bash
   jupyter notebook pract.ipynb
   ```

### Data Requirements
- Ensure your dataset has the following columns:
  - `type` (Movie/TV Show)
  - `rating` (Content rating)
  - `duration` (Runtime information)
  - `release_year` (Year of release)
  - `country` (Country of production)

## 📈 Key Findings

### Content Distribution
- **Movies dominate** the platform with over twice the number of TV shows
- **Mature content focus** with TV-MA being the most prevalent rating

### Temporal Patterns
- **Modern content surge** starting from 2010
- **Peak production** in the late 2010s
- **Consistent movie preference** across all time periods

### Geographic Insights
- **US leadership** in content production
- **International diversity** with India and UK as major contributors
- **Top 10 countries** represent the majority of platform content

### Duration Preferences
- **Standard movie length** concentrated around 90-110 minutes
- **Normal distribution pattern** with few outliers

## 🎨 Visualization Techniques Demonstrated

- **Bar Charts** - Categorical comparisons
- **Pie Charts** - Proportion analysis with percentage labels
- **Histograms** - Distribution analysis with binning
- **Scatter Plots** - Trend visualization over time
- **Horizontal Bar Charts** - Ranked categorical data
- **Subplots** - Multiple related visualizations
- **Custom styling** - Colors, grids, labels, and formatting

## 🔧 Technical Features

- **Data cleaning** - Handling missing values with `dropna()`
- **String manipulation** - Extracting numeric values from duration text
- **Grouping and aggregation** - Multi-dimensional data analysis
- **High-quality exports** - 300 DPI PNG files with tight bounding boxes
- **Professional styling** - Grid lines, legends, and color schemes

## 📝 Usage Notes

> **Important**: When cloning this project, update the CSV file path and figure saving paths in the notebook to match your local directory structure.

### Current Paths in Code:
- **Dataset**: `C:\Users\wwwsh\OneDrive\Desktop\proj_1\data_sci\mat_practice\ott.csv`
- **Figures**: `C:\Users\wwwsh\OneDrive\Desktop\proj_1\data_sci\mat_practice\figures\`

## 💡 Code Highlights

### Data Processing
```python
# Remove rows with missing critical data
df = df.dropna(subset=['type','release_year','rating','country','duration'])

# Extract numeric duration from text
cinema['duration_int'] = cinema['duration'].str.replace(' min', '').astype(int)
```

### Visualization Examples
```python
# Pie chart with percentage labels
plt.pie(rate_count, labels=rate_count.index, autopct='%1.1f%%', startangle=90)

# High-quality figure export
plt.savefig('figures/chart.png', dpi=300, bbox_inches='tight')
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements. Suggestions for additional visualizations or analysis techniques are welcome!

## 📄 License

This project is open source and available under the MIT License.

---

*This project demonstrates practical data analysis skills using Python's data science ecosystem, focusing on storytelling through visualization and deriving actionable insights from streaming platform data.*

**Thank you for checking my project 😊**