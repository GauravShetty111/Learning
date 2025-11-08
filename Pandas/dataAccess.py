import pandas as pd
import numpy as np

# Creating Series with custom index
series = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(series)

# Creating DataFrame from dictionary
dataFrames = pd.DataFrame({
    "Name":["Alice","Gaurav","Gautham"],
    "Age":[20,26,20],
    "Sex":["female","male","male"],
    "Salary":[30000,60000,90000]
})

print(dataFrames)
print(dataFrames["Age"])  # Accessing single column

agesSeries = pd.Series([20,26,27],index = ['a','b','c'])
print(agesSeries)

# Basic statistical operations on column
print(dataFrames["Age"].mean())  # Average age
print(dataFrames["Age"].max())   # Maximum age
print(dataFrames["Age"].min())   # Minimum age

print(dataFrames.describe())  # Summary statistics for all numeric columns

# Reading CSV file
titanicData = pd.read_csv("Data/titanic.csv")

# titanicData.to_excel("Data/titanic.xlsx",sheet_name="titanic",index=False)  # Export to Excel

print(titanicData.head())  # First 5 rows
print(titanicData.info())  # DataFrame info and data types

print(type(titanicData["Parch"]))  # Column type (Series)
print(titanicData["Parch"].shape)   # Column dimensions

# Boolean filtering with multiple conditions
ageAndSex = titanicData[(titanicData["Age"]>20) & (titanicData["Sex"]=="female")]
print(ageAndSex.shape)  # Shape of filtered data

# Filtering out null values and specific value matching
age_not_na = titanicData[titanicData["Age"].notna()]  # Remove null ages
print(age_not_na[age_not_na["Age"].isin([25,30])].head())  # Ages exactly 25 or 30

# Label-based selection with loc
print(titanicData.loc[titanicData["Survived"]== 1,["Name","Sex"]])  # Survivors' names and sex

df = titanicData.loc[:,["Sex","Survived"]]  # Select specific columns


# Position-based selection with iloc
ilocVar = titanicData[titanicData["Age"]>20].iloc[0:10,:6]  # First 10 rows, first 6 columns
ilocVar.iloc[:,5] = ilocVar["Age"].mean()  # Replace 6th column with mean age
print(ilocVar)

print(df)  # Display selected columns