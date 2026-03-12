import requests
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

def get_top_tags():
    params = {
        "method": "user.gettoptags",
        "user": USERNAME,
        "api_key": API_KEY,
        "format": "json",
        "limit": 10
    }
    r = requests.get(BASE_URL, params=params)
    return r.json()['toptags']['tag']

# fetch data
tracks = get_top_tracks()
artists = get_top_artists()
tags = get_top_tags()

# top tracks
track_names = []
for t in tracks:
    track_names.append(t['name'])
track_plays = []
for t in tracks:
    track_plays.append(int(t['playcount']))

# top artists
artist_names = []
for a in artists:
    artist_names.append(a['name'])
artist_plays = []
for a in artists:
    artist_plays.append(int(a['playcount']))

# top tags
tag_names = []
for t in tags:
    tag_names.append(t['name'])
tag_counts = []
for t in tags:
    tag_counts.append(int(t['count']))

fig = make_subplots(rows=3, cols=1,
                    subplot_titles=("Your Top Tracks", "Your Top Artists", "Your Top Genres"),
                    specs=[[{"type": "bar"}], [{"type": "bar"}], [{"type": "pie"}]])

fig.add_trace(go.Bar(x=track_names, y=track_plays,
                     marker_color='SteelBlue', name='Tracks'), row=1, col=1)

fig.add_trace(go.Bar(x=artist_names, y=artist_plays,
                     marker_color='MediumSeaGreen', name='Artists'), row=2, col=1)

fig.add_trace(go.Pie(labels=tag_names, values=tag_counts,
                     name='Genres'), row=3, col=1)

fig.update_layout(height=1200, title_text="Your Music Dashboard",
                  title_font_size=28, showlegend=False)

fig.write_html("dashboard.html", include_plotlyjs='cdn')
print("Dashboard saved! Open dashboard.html")