"""
Day 09 - Handling Missing Data: Replace Method

Dataset: food_db.csv
Description:
Peter Pandey owns a hotel in Bangalore and keeps a food database.
This dataset contains food_id, name, discount, price, and rating.
We perform replacement operations on categorical and numerical data.
"""

import pandas as pd
# Question 1
# Read the CSV file
df = pd.read_csv("food_db.csv")

# Show the number of rows and columns
rows, columns = df.shape
print("Number of rows:", rows)
print("Number of columns:", columns)

# Show the dataframe
print(df)


# Question 2
# Replace the 5% and 10% discounts with 13% to attract more customers
new_df = df.replace(["10%", "5%"], "13%")

# Show the dataframe
print(new_df)


# Question 3
#Replace the categorical column 'rating' with corresponding numerical values.
#Criteria: ['Excellent': 4, 'very Good': 3, 'Good': 2, 'Average': 1]
#store the results in a variable 'new_df'
#show the dataframe 'new_df'
new_df = df.replace({
    "Excellent" : 4,
    "Very Good" : 3,
    "Good"      : 2,
    "Average"   : 1
})

# Show the new dataframe
print(new_df)