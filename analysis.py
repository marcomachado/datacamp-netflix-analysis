# %%
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# %%
print(netflix_df.columns)
# %%
print(netflix_df['genre'].value_counts())
# %%
print(netflix_df.shape)
# %%
print(netflix_df.head())
# %%
print(netflix_df.info())
# %%
netflix_1990_movies = netflix_df[
        (netflix_df['release_year'] >= 1990) 
        & 
        (netflix_df['release_year'] < 2000)
    ]
# %%
netflix_1990_movies.shape
# %%
netflix_1990_movies['duration'].mean()

plt.hist(netflix_1990_movies['duration'])
# %%
freqs = {}
for dur in netflix_1990_movies['duration']:
    freqs[dur] = freqs.get(dur, 0) + 1

# %%
freqs = dict(sorted(freqs.items(), key=lambda item:item[1], reverse=True))
print(freqs)
duration = next(iter(freqs.keys()))
print(duration)
# %%
netflix_1990_short_action_movies = netflix_1990_movies[(netflix_1990_movies['duration']<90) & (netflix_1990_movies['genre']=='Action')]
short_movie_count = netflix_1990_short_action_movies.shape[0]
print(short_movie_count)
# %%
