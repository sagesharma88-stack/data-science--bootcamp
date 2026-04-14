# Day 10 Practice
# Topic: Pandas GroupBy

import pandas as pd



# Task 1: Read the dataset
# Read the CSV file
df = pd.read_csv("movies_data.csv")

print("First 5 rows of dataset:")
print(df.head(5))


# Task 2: Group by 'industry'
g = df.groupby("industry")

print("\nSize of each industry group:")
print(g.size())

print("\nBollywood movies:")
bollywood_data = g.get_group("Bollywood")
print(bollywood_data)


# Task 3: Custom Grouping Function
def grouper(df, idx, col):
    rating = df[col].loc[idx]

    if 1 <= rating <= 3.9:
        return "Poor"
    elif 4 <= rating <= 7.9:
        return "Average"
    elif 8 <= rating <= 10:
        return "Good"
    else:
        return "Others"


# Apply custom grouping
g = df.groupby(lambda idx: grouper(df, idx, "imdb_rating"))

print("\nCustom Grouping based on IMDb rating:")

for key, group in g:
    print(f"\nGroup: {key}")
    print(group)