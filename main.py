import pandas as pd
import lyricsgenius
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Replace 'YOUR_API_KEY' with your actual Genius API access token
GENIUS_API_TOKEN = 'YOUR_API_KEY'

# Read CSV file containing song names and album names
def read_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Fetch lyrics for a given song using LyricsGenius
def fetch_lyrics(song_name):
    genius = lyricsgenius.Genius(GENIUS_API_TOKEN)
    song = genius.search_song(song_name)
    if song:
        lyrics = song.lyrics
        return lyrics
    else:
        return None

# Perform sentiment analysis using TextBlob
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

if __name__ == '__main__':
    csv_file = "your/file/path/to/CSV" # Replace with your CSV file path
    df = read_csv(csv_file)

    sentiment_scores = []

    # Assumes you have a CSV file that contains the "Song" and corresponding "Album" in separate columns
    for index, row in df.iterrows():
        song_name = row['Song']
        album_name = row['Album']

        lyrics = fetch_lyrics(song_name)

        if lyrics:
            sentiment_score = perform_sentiment_analysis(lyrics)
        else:
            sentiment_score = None

        sentiment_scores.append({'song_name': song_name, 'album_name': album_name, 'sentiment_score': sentiment_score})

    sentiment_df = pd.DataFrame(sentiment_scores)

plt.figure(figsize=(10,6), facecolor='lightgrey')
sns.boxplot(x='album_name', y='sentiment_score', hue = 'album_name', data=sentiment_df, palette='flare')
sns.stripplot(x='album_name', y='sentiment_score', data=sentiment_df, color='black')
sns.set_theme(style='darkgrid')

# Add labels and title
plt.xlabel('Album Name')
plt.ylabel('Sentiment Score')
plt.tight_layout()

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

plt.subplots_adjust(bottom=0.38)
# unhash the line below to save the figure in your current directory
#plt.savefig('Mac_boxplot.pdf')
plt.show()
