import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-top-read user-read-recently-played",
    redirect_uri="http://127.0.0.1:8888/callback"
))

user = sp.current_user()
print(f"Logged in as: {user['display_name']}")