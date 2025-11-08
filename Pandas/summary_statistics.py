import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and clean air quality data
data = pd.read_csv("Data/air_quality_no2.csv")
print(data.head())
data.plot()
data = data.dropna()  # Remove missing values

print(data.head())


# Rename columns for better readability
data_columns_renamed = data.rename(
    columns={  # Reanmeing Each columns name explicitly
        "station_antwerp": "Antwerp",
        "station_paris": "Paris",
        "station_london": "London",
    }
)

# Convert all column names to lowercase
data_columns_renamed = data_columns_renamed.rename(
    columns=str.lower
)  # Convert all column names to lowercase
print(data_columns_renamed.head(10))


# Basic statistics
print(
    data_columns_renamed.describe()
)  # gives you count mean max  std Deviation 25% 50% 75% max

# Individual statistics for Antwerp column
print(data_columns_renamed["antwerp"].mean())  # gives mean
print(data_columns_renamed["antwerp"].min())  # gives minimum
print(data_columns_renamed["antwerp"].max())  # gives maximum
print(data_columns_renamed["antwerp"].median())  # gives median


# Aggregation functions - apply multiple stats to specific columns
AggregatedData = data_columns_renamed.agg(
    {"antwerp": ["min", "max", "median"], "london": ["min", "max", "median"]}
)

# Load additional datasets
titanicData = pd.read_csv("Data/titanic.csv")
airno2data = pd.read_csv("Data/air_quality_long.csv")

# Group by embarkation port and calculate mean
groupedDataonSpecificColumn = (
    titanicData[["Embarked", "Age", "Fare"]].groupby("Embarked").mean()
)

# Group by gender and calculate mean for numeric columns
groupedData = titanicData.groupby("Sex").mean(numeric_only=True)

# Count unique values in columns
print(titanicData["Age"].value_counts())  # Value
print(titanicData["Embarked"].value_counts())

# Sort by age and get top/bottom 10 records
print(
    titanicData.sort_values(by="Age", ascending=False).head(10)
)  # Sorting values based on Age column in descending order and getting top 10 records
print(
    titanicData.sort_values(by="Age", ascending=True).head(10)
)  # Sorting values based on Age column in ascending order and getting top 10 records

# Filter and group air quality data
# filter for no2 data only
subData = airno2data[airno2data["parameter"] == "no2"]
# Sort by country then group by location
subsetData = subData.sort_values(by=["country"]).groupby(["location"])
print("Sorting the Values After Grouping By location")
print(subsetData.head())

# Create pivot table with mean aggregation
pivotedData = airno2data.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)

# Pivot data by location
pivotedData = airno2data.pivot(columns="location", values="value").reset_index()

print(pivotedData.head())


# Melt data from wide to long format
meltedData = pivotedData.melt(
    id_vars="index", value_vars=["BETR801", "FR04014", "London Westminster"], value_name="NO2 Levels",var_name="id_location"
)

print(meltedData.head())