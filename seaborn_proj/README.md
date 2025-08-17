# 🏏 IPL Data Analysis with Seaborn

A comprehensive cricket data analysis project examining IPL (Indian Premier League) match statistics using Python's Seaborn and Matplotlib libraries. This project provides insights into team performance, player achievements, toss decisions, and venue statistics across IPL seasons.

## 📊 Project Overview

This analysis explores an IPL dataset containing detailed match information including team performances, player statistics, toss decisions, and venue data. The project demonstrates practical data science skills including exploratory data analysis, statistical visualization, and sports analytics using modern Python libraries.

## 🎯 Key Analysis Areas

### 1. 🏆 Team Performance Analysis
- **Most successful teams** by total wins
- **Win distribution** across all IPL teams
- **Team performance visualization** using horizontal bar plots

### 2. 🪙 Toss Impact Analysis
- **Toss decision trends** (Bat first vs Field first preferences)
- **Toss vs Match correlation** - percentage of teams winning after winning toss
- **Statistical significance** of toss decisions on match outcomes

### 3. 🎯 Victory Patterns
- **Winning methods analysis** - Runs vs Wickets victories
- **Margin analysis** for different victory types
- **Team strategy insights** based on winning patterns

### 4. 🌟 Player Performance Analysis

#### Individual Achievements
- **Player of the Match awards** - Most frequent award winners
- **Top scorers analysis** - Highest run contributors across matches
- **Best bowling figures** - Top wicket-takers and their performances

#### Statistical Breakdowns
- **Cumulative runs** by top scorers
- **Bowling performance metrics** with wicket analysis
- **Player consistency** across multiple matches

### 5. 🏟️ Venue Analysis
- **Most frequent venues** for IPL matches
- **Venue-wise match distribution**
- **Home ground advantages** and patterns

### 6. 📈 Advanced Insights
- **Highest victory margins** by runs
- **Individual record holders** (highest scores, best bowling figures)
- **Performance extremes** and statistical outliers

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **Seaborn** - Statistical data visualization
- **Matplotlib** - Additional plotting capabilities
- **NumPy** - Numerical operations

## 📁 Project Structure

```
seaborn_proj/
├── ipl.ipynb           # Main analysis notebook
├── IPL.csv            # IPL dataset
└── README.md          # Project documentation
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas seaborn matplotlib numpy
```

### Running the Analysis
1. **Update the CSV path** in the notebook:
   ```python
   df = pd.read_csv(r"path/to/your/IPL.csv")
   ```

2. **Execute the notebook** cell by cell to explore the analysis

### Dataset Requirements
The CSV file should contain columns such as:
- `match_winner` - Team that won the match
- `toss_winner` - Team that won the toss
- `toss_decision` - Bat/Field decision
- `player_of_the_match` - Match award winner
- `top_scorer` - Highest scorer in the match
- `highscore` - Highest individual score
- `best_bowling` - Best bowler name
- `best_bowling_figure` - Bowling figures (wickets--runs)
- `venue` - Match venue
- `won_by` - Victory method (Runs/Wickets)
- `margin` - Victory margin

## 📈 Key Findings

### Team Performance
- **Gujarat** emerged as the most successful team with maximum wins
- Clear performance hierarchy visible across IPL teams
- Significant performance gaps between top and bottom teams

### Toss Impact
- **48.65%** of matches were won by teams that also won the toss
- Toss decisions show clear strategic preferences
- Moderate correlation between toss and match outcomes

### Player Excellence
- Identification of most consistent **Player of the Match** award winners
- **Top scorers** with highest cumulative runs across seasons
- **Best bowling performances** with detailed wicket analysis

### Venue Insights
- Certain venues host significantly more matches than others
- Venue distribution reflects IPL's geographical spread
- Clear preference for established cricket stadiums

## 🎨 Visualization Techniques

### Chart Types Used
- **Horizontal Bar Plots** - Team wins and player performance
- **Count Plots** - Categorical distributions (toss decisions, victory methods)
- **Bar Plots** - Venue analysis and award distributions
- **Custom Pandas Plots** - Specialized performance metrics

### Styling Features
- **Color palettes** - "colorblind", "rainbow", "husl", "Set1" for accessibility
- **Professional labeling** - Clear titles, axis labels, and legends
- **Data-driven insights** - Statistical annotations and percentages

## 🔧 Technical Features

### Data Processing
- **String manipulation** using lambda functions for bowling figures
- **Data type conversions** for numerical analysis
- **Groupby operations** for aggregated statistics
- **Sorting and filtering** for top performers

### Advanced Analytics
- **Percentage calculations** for toss correlation analysis
- **Conditional filtering** for specific performance metrics
- **Multi-column analysis** for comprehensive insights
- **Statistical aggregations** using sum, count, and max functions

## 💡 Code Highlights

### Data Transformation
```python
# Extract wickets from bowling figures
df['Max_wickets'] = df['best_bowling_figure'].apply(lambda x: x.split('--')[0])
df['Max_wickets'] = df['Max_wickets'].astype(int)
```

### Statistical Analysis
```python
# Calculate toss vs match win correlation
ganit = df[df["toss_winner"] == df["match_winner"]]['match_id'].count()
percentage = (ganit * 100) / df.shape[0]
```

### Performance Aggregation
```python
# Top scorers with cumulative runs
ankh = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False)
```

## 📊 Dataset Information

- **Size**: 74 rows × 20 columns
- **Data Quality**: No null values detected
- **Coverage**: Complete IPL match data with comprehensive statistics

## 🎓 Learning Outcomes

This project demonstrates:
- **Sports analytics** using real IPL data
- **Statistical visualization** with Seaborn
- **Data manipulation** techniques with Pandas
- **String processing** for cricket-specific data formats
- **Aggregation and grouping** for performance metrics
- **Correlation analysis** for strategic insights

## 📝 Usage Notes

> **Important**: Update the CSV file path in the notebook before running:
> ```python
> df = pd.read_csv(r"C:\path\to\your\IPL.csv")
> ```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- Additional statistical analyses
- Enhanced visualizations
- Performance optimization
- New insights and metrics

## 📄 License

This project is open source and available under the MIT License.

---

*This IPL analysis provides comprehensive insights into cricket performance metrics, demonstrating practical applications of data science in sports analytics.*
