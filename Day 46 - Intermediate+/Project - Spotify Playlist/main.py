from sf_credentials import sf_client_id, sf_client_secret

import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
endpoint = URL + date

year = date.split("-")[0]

soup = BeautifulSoup(requests.get(endpoint).text, "html.parser")

# all_songs = soup.find_all(name="li", class_="o-chart-results-list__item")
all_songs = soup.select("li ul li h3")
for song in all_songs:
    print(song.text.strip())

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=sf_client_id,
#                                                            client_secret=sf_client_secret))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_id=sf_client_id,
                                               client_secret=sf_client_secret,
                                               show_dialog=False,
                                               redirect_uri="http://localhost:8888/callback",
                                               cache_path="token.txt")
                     )

user_id = sp.current_user()["id"]

song_uris = []
for song in all_songs:
    search_result = sp.search(q=f"track:{song.text.strip()} year:{year}", type='track')
    # print(search_result)
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
