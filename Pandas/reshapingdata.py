import pandas as pd
import numpy as np

# Load air quality datasets
air_pm5 = pd.read_csv("Data/air_quality_pm25_long.csv")
print(air_pm5.shape)

air_no2 = pd.read_csv("Data/air_quality_no2_long.csv")

# Select relevant columns from both datasets
air_pm5_subset = air_pm5[["date.utc", "location","parameter", "value"]]
air_no2_subset = air_no2[["date.utc", "location","parameter", "value"]]

# Combine datasets vertically
air_quality = pd.concat([air_pm5_subset,air_no2_subset],axis=0)
# print(air_quality.iloc[:1115,])
print(air_quality.tail())

# Sort by date
print(air_quality.sort_values(["date.utc"]))



# Load coordinates data
coordinatesData  = pd.read_csv("Data/air_quality_no2_Coordinates.csv")
print(coordinatesData.groupby("location").head())

print(air_quality.groupby("location").head())

# Merge air quality data with coordinates
air_quatlitywith_coordinates = pd.merge(air_quality, coordinatesData, how="left", on="location")
print(air_quatlitywith_coordinates.head())

# Group merged data by location and show counts
grouped_by_location = air_quatlitywith_coordinates.groupby("location")
print(grouped_by_location.size())