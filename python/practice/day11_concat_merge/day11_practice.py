#Concat and Merge Practice

import pandas as pd



# Question 1: Read CSV files
df_movies = pd.read_csv("movies.csv")
df_financials = pd.read_csv("financials.csv")
df_languages = pd.read_csv("languages.csv")

print("\nTop 3 rows of movies:")
print(df_movies.head(3))

print("\nTop 3 rows of financials:")
print(df_financials.head(3))

print("\nTop 3 rows of languages:")
print(df_languages.head(3))


# Question 2: Concat movies
df_new_movies = pd.read_csv("new_movies.csv")

df_movies = pd.concat([df_movies, df_new_movies], ignore_index=True)

print("\nLast 5 rows after concat:")
print(df_movies.tail(5))


# Question 3: Merge with languages (INNER JOIN)
df_movies = pd.merge(df_movies, df_languages, on="language_id", how="inner")

print("\nAfter merging with languages:")
print(df_movies.head(5))


# Question 4: Merge with financials (LEFT JOIN)
df_movies = pd.merge(df_movies, df_financials, on="movie_id", how="left")

print("\nAfter merging with financials:")
print(df_movies.tail(5))


# Question 5: Save final CSV
df_movies.to_csv(
    "final_complete_data.csv",
    columns=["movie_id", "title", "lang_name", "budget", "revenue", "currency"],
    index=False
)

print("\n✅ Final CSV saved successfully!")