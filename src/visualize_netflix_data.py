import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv("data/cleaned_netflix_data.csv")

# Split genre string into list
df["genre_list"] = df["genres"].str.split(",")

# Explode list so each genre gets its own row
genre_df = df.explode("genre_list")
genre_df["genre_list"] = genre_df["genre_list"].str.strip()  # remove spaces

# Count most frequent genres
top_genres = genre_df["genre_list"].value_counts().nlargest(10)

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="muted")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

# Save chart
os.makedirs("output/charts", exist_ok=True)
plt.savefig("output/charts/top_genres.png")
plt.show()
