import os
from dotenv import load_dotenv
from spotifypodcast import SpotifyPodcast
from youtubedownloader import YouTubeDownloader
from whipertranscriber import WhisperTranscriber
from gpt3summarizer import GPT3Summarizer

# Load API credentials from .env file
load_dotenv()

SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")

OUTPUT = ['downloads/youtube', 'downloads/spotify', 'downloads/whisper',  'downloads/gpt3']
# create output directories if they don't exist
for dir in OUTPUT:
    if not os.path.exists(dir):
        os.makedirs(dir)

def summarize(podcast_url, source, max_sentences=10):
    
    print('Initializing summarizer...')
    print(f'podcast_url: {podcast_url}')
    print(f'source: {source}')
    print(f'max_sentences: {max_sentences}')
    
    file_id = None
    
    if source == "youtube":
        downloader = YouTubeDownloader(podcast_url)
        audio_path, transcript_path, metadata_path = downloader.download_all()
        metadata = downloader.get_metadata()
        transcript = downloader.get_transcript()
        chapters = metadata['chapters']

        file_id = metadata['id']
        
    elif source == "spotify":
    
        podcast = SpotifyPodcast(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
        file_id = podcast.get_episode_id(podcast_url)
        audio_path = podcast.download_episode(podcast_url)
    
    transcriber = WhisperTranscriber(OPENAI_API_KEY)
    transcript = transcriber.transcribe(audio_path)
    
    summarizer = GPT3Summarizer(OPENAI_API_KEY, model_engine="gpt-3.5-turbo")
    summarizer.summarize(file_id, transcript, max_sentences)
    
    print(f'Completed summarization for ({podcast_url})')
    
# summarize("https://open.spotify.com/episode/0YqflJb8Wco8IDdGHPNTu8", "spotify", 12)
summarize("https://www.youtube.com/watch?v=GkZz2I6sK08", "youtube", 12)

