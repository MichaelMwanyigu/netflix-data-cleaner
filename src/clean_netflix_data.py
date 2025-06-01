import pandas as pd

df = pd.read_csv("data/netflix_titles.csv")

# Rename 'listed_in' to 'genres'
df = df.rename(columns={"listed_in": "genres"})

# Drop rows with missing important info
df = df.dropna(subset=["title", "genres", "duration"])

# Clean duration (for movies or approximate shows)
def parse_duration(value):
    if "min" in value:
        return int(value.replace("min", "").strip())
    elif "Season" in value:
        return int(value.split()[0]) * 60  # Estimate 1 season ≈ 60 mins
    return None

df["duration_min"] = df["duration"].apply(parse_duration)
df = df.dropna(subset=["duration_min"])

# Save cleaned file
df_clean = df[["title", "genres", "release_year", "duration_min"]]
df_clean.to_csv("data/cleaned_netflix_data.csv", index=False)

print("Cleaned data saved.")



