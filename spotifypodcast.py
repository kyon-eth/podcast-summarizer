import spotipy
import requests
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyPodcast:
    def __init__(self, client_id, client_secret):
        # Authenticate with Spotify API using client credentials flow
        # auth_manager = spotipy.oauth2.SpotifyClientCredentials(
        #     client_id=client_id,
        #     client_secret=client_secret
        # )
        # self.sp = spotipy.Spotify(auth_manager=auth_manager)
        
        print(f'client_id: {client_id}')
        print(f'client_secret: {client_secret}')
        
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
        

    def download_episode(self, podcast_url):
        # Parse the podcast ID from the URL
        parsed_url = urllib.parse.urlparse(podcast_url)
        podcast_id = parsed_url.path.split("/")[-1]
        print(f'Podcast ID: {podcast_id}')
        
        # Retrieve the podcast data using the Spotify API
        # podcast = self.sp.show(podcast_id)
        # print(podcast)

        # Get the first episode of the podcast
        # episode = self.sp.episode(podcast["episodes"]["items"][0]["id"])
        episode = self.sp.episode(podcast_id, market="US")

        # Download the audio file
        audio_url = episode["audio_preview_url"]
        response = requests.get(audio_url)
        filename = f"{podcast_id}.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Episode downloaded: {filename}")
        
        return filename
