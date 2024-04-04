# music_sentiment.py
A Python program that plots the NLTK sentiment analysis of a selection of music, given the song name(s) and album title(s)

The main script is found in ```main.py``` (makes sense)

Simply create a CSV file with columns labeled "Song" and "Album" to read in. You'll also need a client token from Genius API (https://docs.genius.com/#/authentication-h1).
Paste your client token into the variable within api_key.py, or add it straight into the ```GENIUS_API_TOKEN``` variable. Reading the CSV file into the Genius API will automatically search and add the lyrics to the list.

Using the ```textblob``` package, the lyrics will be fed into the NLTK sentiment analyzer and each song will be evaluated for its sentiment on a scale from -1 to +1, where a more positive value represents positive sentiment.
More info on the ```textblob``` sentiment analysis can be found at https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.sentiment.

### Input data
The expected input is a CSV file with columns ```Song``` and ```Album```. I've provided an example CSV file that features most of Mac Miller's discography, ```MacMillersdiscography.csv```.

### Plotting the data
By default, the ```seaborn``` package is utilized to plot the sentiment values as a box plot, categorized by album. However, this can be changed as desired.

### TODO
Add a Streamlit GUI to enable drag-and-drop functionality for the input file
