# Music Dashboard

A Python script that fetches your Last.fm listening data and generates an interactive dashboard using Plotly.

## Features

- Top 10 most played tracks
- Top 10 most played artists
- Top genres as a pie chart

## Setup

1. Get a Last.fm API key from https://www.last.fm/api/account/create
2. Create a `.env` file with your credentials:
```
LASTFM_API_KEY=your_api_key
LASTFM_USERNAME=your_username
```

3. Install dependencies:
```
pip install requests plotly python-dotenv
```

4. Run the script:
```
python last-fm_stats.py
```

This generates a `dashboard.html` file — open it in your browser.

## Notes

- Connect Last.fm to Spotify at last.fm/settings/applications to start scrobbling
- Genre chart requires a few days of listening history to populate