import pandas as pd
import numpy as np

series = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(series)

dataFrames = pd.DataFrame({
    "Name":["Alice","Gaurav","Gautham"],
    "Age":[20,26,20],
    "Sex":["female","male","male"],
    "Salary":[30000,60000,90000]
})

print(dataFrames)
print(dataFrames["Age"])

agesSeries = pd.Series([20,26,27],index = ['a','b','c'])
print(agesSeries)


print(dataFrames["Age"].mean())
print(dataFrames["Age"].max())
print(dataFrames["Age"].min())

print(dataFrames.describe())

titanicData = pd.read_csv("Data/titanic.csv")

# titanicData.to_excel("Data/titanic.xlsx",sheet_name="titanic",index=False)

print(titanicData.head())

print(titanicData.info())

print(type(titanicData["Parch"]))
print(titanicData["Parch"].shape)


ageAndSex = titanicData[(titanicData["Age"]>20) &(titanicData["Sex"]=="female")]
print(ageAndSex.shape)

age_not_na = titanicData[titanicData["Age"].notna()]
print(age_not_na[age_not_na["Age"].isin([25,30])].head())

print(titanicData.loc[titanicData["Survived"]== 1,["Name","Sex"]])

df = titanicData.loc[:,["Sex","Survived"]]


ilocVar = titanicData[titanicData["Age"]>20].iloc[0:10,:6]
ilocVar.iloc[:,5] = ilocVar["Age"].mean()
print(ilocVar)

print(df)