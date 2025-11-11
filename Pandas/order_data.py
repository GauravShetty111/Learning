import re

import pandas as pd
import numpy as np


chipo = pd.read_csv("Data/orderdata.txt",delimiter="\t",header=None)

chipo.columns = ["OrderID", "Quantity", "item_name", "choice_description","item_price"]

chipo = chipo.iloc[1:].reset_index(drop=True)

chipo["item_price"] = chipo["item_price"].str.replace(r"\$","",regex=True).astype(float)

# Step 4. How many products cost more than $10.00?

print(chipo[chipo["item_price"]>10]["item_price"].count())
# print(chipo.loc[chipo["item_price"]>10,"item_price"].count())

# Step 5. What is the price of each item?
print(chipo[["item_name","choice_description","item_price"]])

sorted_chipo = chipo.sort_values(by="item_name")

# Step 7. What was the quantity of the most expensive item ordered?
quantity = chipo[chipo["item_price"] == chipo["item_price"].max()]
print(quantity["Quantity"])

# Step 8. How many times was a Veggie Salad Bowl ordered?
VeggieSaladBowl = chipo[chipo["item_name"] == "Veggie Salad Bowl"]

# Step 9. How many times did someone order more than one Canned Soda?
chipo["item_name"] = chipo["item_name"].str.replace(r"\[", "", regex=True)
chipo["Quantity"] = chipo["Quantity"].astype(int)


cannedSoda = chipo[(chipo["item_name"]=="Canned Soda")&(chipo["Quantity"]>1)]["item_name"].count()


