import requests
from bs4 import BeautifulSoup
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

date = input("What year you would like to travel to in YYYY-MM-DD format.")
URL = f'https://www.billboard.com/charts/hot-100/{date}'
response = requests.get(url=URL)
top_100_songs_website = response.text

# Web scraping
soup = BeautifulSoup(top_100_songs_website, 'html.parser')
article_songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in article_songs]

Client_ID = os.environ.get('Spotify_Client_ID')
Client_Secret = os.environ.get('Spotify_Client_Secret')
Redirect_URI = os.environ.get('Spotify_redirect_URI')
print(Client_ID, Client_Secret, Redirect_URI)

# Spotify Authentication
# Replace YOUR_CLIENT_ID, YOUR_CLIENT_SECRET, and YOUR_REDIRECT_URI with your actual credentials
sp_oauth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                                     client_secret=Client_Secret,
                                                     redirect_uri=Redirect_URI,
                                                     scope='playlist-modify-private',
                                                     show_dialog=True,
                                                     cache_path="./top-100-songs-web-scraping-day-46/token.txt",
                                                     username='Mtsmech')
                           )
ID = sp_oauth.current_user()['id']

# To find songs uris
year = date.split('-')[0]
songs_uri_list = []
for song in song_list:
    result = sp_oauth.search(q=f'track: {song} year: {year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri_list.append(uri)
    except IndexError:
        print(f'{song} does not exit, skipped')
print(len(songs_uri_list))

# Create a private play list on spotify app
create_play_list = sp_oauth.user_playlist_create(user=ID, name=f'{date} Billboard 100', public=False)
print(create_play_list)
add_songs = sp_oauth.playlist_add_items(playlist_id=create_play_list['id'], items=songs_uri_list)
print(add_songs)
