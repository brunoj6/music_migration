import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic


# Function:
#   Takes in client id and secret credentials to act as user and uses playlist to grab data for YTMusic.
# Inputs:
#   id: client id number from spotify for developers
#   secret: client secret value from spotify for developers
#   playlist: the name or url of the playlist to be copied from spotify. NOTE: this cannot refer to a collection.

def grab_playlist(id, secret, playlist):

  # Start spotipy client
    spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(id, secret))

  # grab the url for the spotify playlist to transfer
    repo = spotify_client.playlist_items(playlist)

    # generate empty arrays
    titles = []
    artists = []
    albums = []

    # create a list of the titles, albums, and artists
    for ind, obj in enumerate(repo['items']):
        titles.append(repo['items'][ind]['track']['name'])
        artists.append("".join(a['name'] for a in repo['items'][ind]['track']['artists'] if a['type'] == 'artist'))
        albums.append(repo['items'][ind]['track']['album']['name'])

    # Function:
    #   Creates a playlist on Youtube Music
    # Inputs:
    #   name: the desired name of the playlist
    #   desc: a description of the

def send_to_YT(name="From Spotify", desc="Music Migration"):
    # This file must be in the same folder as headers_auth.json
    ytmusic = YTMusic('headers_auth.json')

    # create the playlist
    yt_playlist_id = ytmusic.create_playlist(name, desc)

    video_ids = []

    # fill video_ids for songs
    for index, obj in enumerate(titles):
        # search for the queried song
        query = f'{titles[index]} {albums[index]} {artists[index]}'
        # grab possible search results
        results = ytmusic.search(query)
        # fill
        for item in results:
            if item['resultType'] == 'song' and item['title'] == titles[index]:
                video_ids.append(item['videoId'])
                break
        else:
            print(f'Could not find result for {query}')

    # add items to playlist
    ytmusic.add_playlist_items(yt_playlist_id, video_ids)
