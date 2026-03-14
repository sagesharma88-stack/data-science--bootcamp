# Day 07 - Pandas Read/Write CSV & Excel Exercise

import pandas as pd

# Question 1: Read CSV & show top 5 rows
df = pd.read_csv("movies_data.csv")
print(df.head(5))

# Question 2: Add a new column "year_classify"
df["year_classify"] = df["release_year"].apply(lambda x: "Before 2000" if x < 2000 else "From 2000")
print(df.head(10))

# Question 3: Save filtered dataframe to CSV
df[["movie_id", "title", "budget", "revenue", "year_classify"]].to_csv("final_movie_data.csv", index=False)