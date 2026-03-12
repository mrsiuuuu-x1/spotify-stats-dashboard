import requests
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LASTFM_API_KEY")
USERNAME = os.getenv("LASTFM_USERNAME")
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_top_tracks():
    params = {
        "method": "user.gettoptracks",
        "user": USERNAME,
        "api_key": API_KEY,
        "format": "json",
        "limit": 10
    }
    r = requests.get(BASE_URL, params=params)
    return r.json()['toptracks']['track']

def get_top_artists():
    params = {
        "method": "user.gettopartists",
        "user": USERNAME,
        "api_key": API_KEY,
        "format": "json",
        "limit": 10
    }
    r = requests.get(BASE_URL, params=params)
    return r.json()['topartists']['artist']

# fetch data
tracks = get_top_tracks()
artists = get_top_artists()

# top tracks chart
track_names = [t['name'] for t in tracks]
track_plays = [int(t['playcount']) for t in tracks]

# top artists chart
artist_names = []
for a in artists:
    artist_names.append(a['name'])
artist_plays = []
for a in artists:
    artist_plays.append(a['playcount'])

fig = make_subplots(rows=2, cols=1, 
                    subplot_titles=("Your Top Tracks", "Your Top Artists"))

fig.add_trace(go.Bar(x=track_names, y=track_plays, 
                     marker_color='SteelBlue', name='Tracks'), row=1, col=1)

fig.add_trace(go.Bar(x=artist_names, y=artist_plays, 
                     marker_color='MediumSeaGreen', name='Artists'), row=2, col=1)

fig.update_layout(height=800, title_text="Your Music Dashboard", 
                  title_font_size=28, showlegend=False)

fig.write_html("dashboard.html", include_plotlyjs='cdn')
print("Dashboard saved! Open dashboard.html")