# Data Science Learning Repository 📊

A comprehensive collection of Python data science practice notebooks and learning materials, featuring hands-on exercises across multiple domains including data analysis, visualization, and machine learning.

## 📁 Repository Structure

### Core Libraries Practice
- **[`numpy`](numpy )** - NumPy arrays, mathematical operations, and numerical computing
- **[`pandas`](pandas )** - Data manipulation, analysis, and file I/O operations  
- **[`matplotlib`](matplotlib )** - Data visualization and plotting fundamentals
- **[`panda_numpy_pract`](panda_numpy_pract )** - Combined practice exercises

### Practice Directories
- **[`mat_practice`](mat_practice )** - Matrix operations and mathematical computations
- **[`pract`](pract )** - General practice exercises and datasets
- **[`practice`](practice )** - Additional coding practice materials
- **[`saving`](saving )** - File output and data persistence examples

### Learning Resources
- **[`Refactored_Py_DS_ML_Bootcamp-master`](Refactored_Py_DS_ML_Bootcamp-master )** - Complete Python Data Science and Machine Learning Bootcamp materials including:
  - NumPy fundamentals and advanced operations
  - Pandas data analysis and manipulation
  - Data visualization with Matplotlib and Seaborn
  - Plotly and Cufflinks for interactive plots
  - Geographical plotting and choropleth maps
  - Linear regression and machine learning
  - Natural language processing
  - Recommender systems
  - Big Data with Spark

## 🛠️ Technologies & Libraries

- **Python** - Primary programming language
- **Pandas** - Data manipulation and analysis (pandas/0pandas.ipynb, pandas/first.ipynb)
- **NumPy** - Numerical computing (numpy/check.py)
- **Matplotlib** - Data visualization (matplotlib/one_to_eight.ipynb)
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive plotting
- **Jupyter Notebooks** - Interactive development environment

## 📚 Key Learning Areas

### Data Analysis & Manipulation
- Reading various file formats (CSV, Excel, JSON)
- Data cleaning and preprocessing
- Statistical analysis and aggregations
- DataFrame operations and transformations

### Data Visualization
- Basic plotting with Matplotlib
- Statistical plots with Seaborn
- Interactive visualizations with Plotly
- Geographical mapping and choropleth plots

### Machine Learning
- Linear regression models
- Data preprocessing for ML
- Model evaluation and validation
- Feature engineering

### Advanced Topics
- Natural Language Processing
- Recommender Systems
- Big Data processing with Spark
- Lambda expressions and functional programming

## 🚀 Getting Started

1. **Installation**: Ensure you have Python and required libraries installed:
   ```bash
   conda install numpy pandas matplotlib seaborn plotly
   # or
   pip install numpy pandas matplotlib seaborn plotly
   ```

2. **Jupyter Notebooks**: Start with the basic notebooks in the [`pandas`](pandas ) and [`numpy`](numpy ) directories
3. **Practice Files**: Explore the various practice directories for hands-on exercises
4. **Bootcamp Materials**: Dive into the comprehensive bootcamp materials for structured learning

## 📋 Example Usage

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading data (from pandas/first.ipynb)
df = pd.read_csv("data.csv", encoding="latin1")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")

# Saving data (from pandas/0pandas.ipynb)
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", orient='records')
```

## 🎯 Learning Objectives

- Master Python libraries essential for data science
- Develop proficiency in data manipulation and analysis
- Create compelling data visualizations
- Build and evaluate machine learning models
- Handle real-world datasets and projects
- Apply best practices in data science workflows

---

*This repository serves as a comprehensive learning resource for aspiring data scientists and anyone looking to strengthen their Python data analysis skills.*