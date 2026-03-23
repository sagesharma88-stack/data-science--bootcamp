"""
Day 08 - Handling Missing Data (fillna, interpolate, dropna)

Dataset: fruits_data.csv
Description:
This dataset contains monthly fruit prices with missing values.
We perform different techniques to handle missing data.
"""

import pandas as pd

# Question 1
# read the csv file
df = pd.read_csv("fruits_data.csv")

# show the number of rows and columns
rows, columns  = df.shape 
print("Number of rows",rows)
print("Number of columns",columns)

# list all the columns
print(df.columns)

# show the dataframe
print(df)


# Question 2
# fill null values with -1 and store it to 'new_df'
new_df = df.fillna(-1)

# show the dataframe 'new_df'
print(new_df)


# Question 3
# print mean and median values
print(df["apple(1kg)"].mean())
print(df["banana(1 dozen)"].mean())
print(df["grapes(1kg)"].median())
print(df["mango(1kg)"].median())
print(df["Water Melons(1)"].median())

# store the result to 'new_df' variable
new_df = df.fillna({
    "apple(1kg)": df["apple(1kg)"].mean(),
    "banana(1 dozen)": df["banana(1 dozen)"].mean(),
    "grapes(1kg)": df["grapes(1kg)"].median(),
    "mango(1kg)": df["mango(1kg)"].median(),
    "Water Melons(1)": "Not Available"
})

# show the dataframe 'new_df'
print(new_df)


# Question 4
# fill null values using 'ffill'
new_df = df.ffill()

# show the dataframe 'new_df'
print(new_df)


# Question 5
# drop rows with at least 4 non-null values
new_df = df.dropna(thresh=4)

# show the dataframe 'new_df'
print(new_df)


# Question 6
# remove rows containing null values
new_df = df.dropna()

# show the dataframe 'new_df'
print(new_df)

# save the dataframe to 'final_data.csv'
new_df.to_csv("final_data.csv", index=False)