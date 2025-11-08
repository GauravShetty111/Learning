# Pandas Learning Files

## Files Overview

### DataAccessInPandas.py
Methods for accessing and manipulating data in Pandas DataFrames

**Functions Used:**
- `pd.Series()` - Create indexed data series
- `pd.DataFrame()` - Create structured data table
- `pd.read_csv()` - Load CSV files into DataFrame
- `.head()` - Display first 5 rows
- `.info()` - Show DataFrame structure and data types
- `.describe()` - Generate summary statistics
- `.mean()/.max()/.min()` - Calculate column statistics
- `.shape` - Get DataFrame dimensions
- `.notna()` - Filter out null values
- `.isin()` - Filter rows matching specific values
- `.loc[]` - Label-based data selection
- `.iloc[]` - Position-based data selection

### summary_statistics.py
Statistical analysis and data transformation operations on datasets

**Functions Used:**
- `pd.read_csv()` - Load CSV data files
- `.dropna()` - Remove missing values
- `.rename()` - Rename DataFrame columns
- `.describe()` - Generate descriptive statistics
- `.mean()/.min()/.max()/.median()` - Calculate statistical measures
- `.agg()` - Apply multiple aggregation functions
- `.groupby()` - Group data by column values
- `.value_counts()` - Count unique values
- `.sort_values()` - Sort DataFrame by column
- `.pivot_table()` - Create pivot table with aggregation
- `.pivot()` - Reshape data from long to wide format
- `.melt()` - Transform data from wide to long format