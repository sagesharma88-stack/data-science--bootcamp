# Day 06 - DataFrame Basics Exercise
# Task: Analyze Bengaluru house prices

import pandas as pd

# Question 1: Read CSV and basic info
df = pd.read_csv("bengaluru_house_prices.csv")

# Show number of rows and columns
print(df.shape)

# Show top 5 rows
print(df.head(5))


# Question 2: Unique categories in 'area_type' and 'size'
print(df['area_type'].unique())
print(df['size'].unique())


# Question 3: Filter 2 BHK & Super built-up Area
# Filter rows where size is '2 BHK' AND area_type is 'Super built-up  Area'
df_1 = df[(df["size"] == "2 BHK") & (df["area_type"] == "Super built-up  Area")]

# Show first 4 rows of filtered data
print(df_1.head(4))

# Show number of rows in filtered data
print(len(df_1))


# Question 4: Add 'price_category' column
def category(x):
    if x < 80:
        return "Affordable"
    return "High Cost"

df["price_category"] = df["price"].apply(category)

# Show top 5 rows with new column
print(df.head(5))


# Question 5: Filter rows with price > mean price
df_2 = df[df["price"] > df["price"].mean()]

# Show top 5 rows of houses with price above mean
print(df_2.head(5))