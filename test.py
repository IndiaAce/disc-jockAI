from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from a .env file
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# We're going to test fetching dettails of a song by name

def get_track_details(track_name):
    results = sp.search(q=track_name, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'id': track['id'],
            'url': track['external_urls']['spotify']
        }
    else:
        return None

if __name__ == "__main__":
    track_name = input("Enter a track name to search: ")
    track_details = get_track_details(track_name)
    if track_details:
        print(f"Track found: {track_details}")
    else:
        print("Track not found")