# 📊 Social Media Usage Analysis: Student Dataset

A comprehensive data analysis project examining social media usage patterns among students using Python's Pandas and NumPy libraries. This project provides insights into how social media consumption affects academic performance, mental health, and sleep patterns across different demographics.

## 📖 Project Overview

This analysis explores a student dataset containing information about social media usage habits, academic performance, mental health indicators, and demographic details. The project demonstrates practical data science skills including data cleaning, exploratory data analysis, statistical correlation analysis, and categorical data binning.

## 🎯 Analysis Sections

### 1. 📌 Basic Data Exploration
- **Dataset overview** with shape, data types, and structure
- **Initial inspection** using head(), tail(), and info() methods
- **Key metrics** including mean age, usage hours range, and mental health scores

### 2. 🔍 Data Quality Assessment
- **Missing value detection** across all columns
- **Duplicate record identification** for both Student_IDs and complete rows
- **Data validation** for unrealistic values (negative ages, >24 hour usage, invalid sleep hours)

### 3. 📊 Descriptive Statistics
- **Demographic analysis** including age and gender distributions
- **Usage patterns** with mean and mode calculations
- **Mental health score** statistical summaries

### 4. 📱 Platform Usage Analysis
- **Most popular social media platforms** ranking
- **Cross-tabulation analysis** between gender and platform preferences
- **Usage distribution** across different platforms

### 5. 📈 Usage Pattern Insights
- **Academic level impact** on daily usage hours
- **Gender-based usage differences**
- **Age group categorization** (18-19, 20-21, 22-24, 25+) with usage analysis

### 6. 🎓 Academic Performance Impact
- **Academic performance correlation** with social media usage
- **Usage comparison** between students with affected vs unaffected academic performance

### 7. 💤 Health & Wellness Analysis
- **Sleep correlation** with social media usage hours
- **Mental health score correlation** with usage patterns
- **Sleep categorization** (<6, 6-8, 8+ hours) and mental health impact

### 8. 🌍 Geographic Analysis
- **Country-wise usage patterns** identification
- **Top countries** by student representation
- **Regional usage differences** analysis

### 9. 💑 Relationship Status Impact
- **Relationship status distribution** analysis
- **Usage patterns** across different relationship statuses
- **Addiction scores** by relationship status

### 10. 🏷️ Data Categorization
- **Usage intensity categories** (Light: 0-3hrs, Moderate: 3-6hrs, Heavy: 6+hrs)
- **Age group binning** for demographic analysis
- **Custom category creation** for enhanced insights

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Pandas** - Data manipulation, analysis, and CSV handling
- **NumPy** - Numerical operations and statistical calculations

## 📁 Project Structure

```
panda_numpy_pract/one/
├── one.ipynb           # Main analysis notebook
├── one.csv            # Student dataset
└── README.md          # Project documentation
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy
```

### Running the Analysis
1. **Clone or download** the project files
2. **Update the CSV path** in the notebook to match your local directory:
   ```python
   df = pd.read_csv("path/to/your/one.csv")
   ```
3. **Execute the notebook** cell by cell to see the analysis results

### Dataset Requirements
The CSV file should contain the following columns:
- `Student_ID` - Unique identifier
- `Age` - Student age
- `Gender` - Gender information
- `Avg_Daily_Usage_Hours` - Daily social media usage in hours
- `Most_Used_Platform` - Primary social media platform
- `Academic_Level` - Academic year/level
- `Affects_Academic_Performance` - Boolean/categorical impact indicator
- `Sleep_Hours_Per_Night` - Nightly sleep duration
- `Mental_Health_Score` - Mental health assessment score
- `Country` - Student's country
- `Relationship_Status` - Current relationship status
- `Addicted_Score` - Social media addiction assessment

## 📈 Key Findings Expected

### Usage Patterns
- **Age correlation** with social media consumption
- **Gender differences** in platform preferences and usage intensity
- **Academic level impact** on usage patterns

### Health Implications
- **Sleep-usage correlation** revealing potential sleep disruption
- **Mental health relationships** with excessive usage
- **Academic performance impacts** from social media consumption

### Demographic Insights
- **Country-specific usage trends** and cultural differences
- **Relationship status influences** on social media habits
- **Platform preferences** across different demographics

## 🔧 Technical Features

### Data Processing
- **Robust data validation** with outlier detection
- **Missing value assessment** for data quality
- **Duplicate detection** ensuring data integrity

### Statistical Analysis
- **Correlation calculations** between key variables
- **Groupby operations** for categorical analysis
- **Cross-tabulation** for relationship exploration

### Data Transformation
- **Categorical binning** using `pd.cut()` for age and usage groups
- **Custom category creation** for enhanced analysis
- **Data type optimization** for efficient processing

## 📊 Visualization Potential

While this project focuses on data analysis, the processed data is ready for visualization including:
- **Usage distribution histograms**
- **Platform preference pie charts**
- **Correlation heatmaps**
- **Academic impact scatter plots**
- **Geographic usage maps**

## 💡 Usage Notes

> **Important**: Update the CSV file path in the notebook before running:
> ```python
> df = pd.read_csv(r"C:\path\to\your\one.csv")
> ```

## 🎓 Learning Outcomes

This project demonstrates:
- **Data exploration techniques** using Pandas
- **Statistical analysis methods** with NumPy
- **Data quality assessment** procedures
- **Categorical data handling** and binning
- **Correlation analysis** for relationship discovery
- **Practical data science workflow** implementation

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- Additional analysis techniques
- Enhanced data validation methods
- New categorical insights
- Performance optimizations

## 📄 License

This project is open source and available under the MIT License.

---

*This project provides a comprehensive introduction to data analysis using Python, demonstrating practical skills essential for data science and analytics roles.*