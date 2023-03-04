import json
import youtube_dl
import subprocess
import os

class YouTubeDownloader:
    def __init__(self, video_url):
        self.video_url = video_url
        self.output_dir = 'downloads/youtube/'
        
    def download_mp3(self):
        path = os.path.abspath(self.output_dir + self.video_url.split('=')[-1] + '.mp3')
        
        if os.path.exists(path):
            return path
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{self.output_dir}%(id)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.video_url])
        return os.path.abspath(self.output_dir + self.video_url.split('=')[-1] + '.mp3')
    
    def download_metadata(self):
        path = os.path.abspath(self.output_dir + self.video_url.split('=')[-1] + '.info.json')
        
        if os.path.exists(path):
            return path
        
        ydl_opts = {
            'outtmpl': f'{self.output_dir}%(id)s.%(ext)s',
            'skip_download': True,
            'writeinfojson': True,
            'writeannotations': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.video_url])
        return path
        
    def download_transcript(self):
        path = os.path.abspath(self.output_dir + self.video_url.split('=')[-1] + '.en.vtt')
        
        if os.path.exists(path):
            return path
        
        ydl_opts = {
            'outtmpl': f'{self.output_dir}%(id)s.%(ext)s',
            'skip_download': True,
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'convertsubtitles': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.video_url])
        return path
            
    def get_metadata(self):
        
        with open(self.output_dir + self.video_url.split('=')[-1] + '.info.json', 'r', encoding='utf8') as f:
            return json.load(f)
        
    def get_transcript(self):
        with open(self.output_dir + self.video_url.split('=')[-1] + '.en.vtt', 'r', encoding='utf8') as f:
            transcript = f.read()
            # transcript = transcript.replace('\n', ' ').replace('\r', '').replace('<br />', '\n')
            transcript = ' '.join([line for line in transcript.split('\n') if '-->' not in line])
            # new lines for each speaker if text contains " -"
            transcript = transcript.replace(' - ', '\n')
                        
            return transcript
        
    def download_all(self):
        mp3_path = self.download_mp3()
        metadata_path = self.download_metadata()
        transcript_path = self.download_transcript()
        
        metadata = self.get_metadata()
        print(f'Video title: {metadata["title"]}')
        print(f'Video length: {metadata["duration"] / 60:.2f} minutes')
        
        return mp3_path, transcript_path, metadata_path
