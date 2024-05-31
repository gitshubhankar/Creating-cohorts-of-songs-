import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
spotify_data = pd.read_csv('Desktop/rolling_stones_spotify.csv')
spotify_data['release_date'] = pd.to_datetime(spotify_data['release_date'])

# 1. Histograms of song attributes
fig, axes = plt.subplots(3, 1, figsize=(8, 12))
sns.histplot(data=spotify_data, x='danceability', bins=30, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Danceability')

sns.histplot(data=spotify_data, x='energy', bins=30, ax=axes[1], color='olive')
axes[1].set_title('Distribution of Energy')

sns.histplot(data=spotify_data, x='loudness', bins=30, ax=axes[2], color='gold')
axes[2].set_title('Distribution of Loudness')

plt.tight_layout()
plt.show()

# 2. Scatter plot: Popularity vs Energy
plt.figure(figsize=(10, 6))
sns.scatterplot(data=spotify_data, x='energy', y='popularity', alpha=0.6)
plt.title('Relationship between Energy and Popularity')
plt.xlabel('Energy')
plt.ylabel('Popularity')
plt.grid(True)
plt.show()

# 3. Bar chart of average popularity by album
album_popularity = spotify_data.groupby('album')['popularity'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
album_popularity.plot(kind='bar', color='teal')
plt.title('Average Popularity of Songs by Album')
plt.xlabel('Album')
plt.ylabel('Average Popularity')
plt.xticks(rotation=90)
plt.show()

