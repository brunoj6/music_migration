# Transfer Playlists to Youtube Music


## Dependencies

This package depends on the following API:

__spotipy__: access to Spotify web platform <br />
https://spotipy.readthedocs.io/en/2.22.0/

__ytmusicapi__: connects to YT Music <br />
https://ytmusicapi.readthedocs.io/en/latest/index.html


## Spotify Setup

Spotipy requires a client id and secret to access the account. These values can be accessed by making a new app on Spotify for Developers. 

https://developer.spotify.com/dashboard/applications


##  Youtube Setup

This is a bit tedious, but is required to allow access to the api. There is a more detailed explanation for different browsers in the documentation found above. 

1. Sign into YTMusic
2. Open Dev Settings (ctrl+^+i)
3. Go to YTMusic Home
4. Open the _Network_ tab in Dev Settings
5. Find a request labelled _browse?_ and open to show requests
6. Copy the relevant _cookies_ value into the _headers_auth.json_ file





