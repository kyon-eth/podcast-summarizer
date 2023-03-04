# Podcast Summarizer

![Podcast Summarizer](https://user-images.githubusercontent.com/99987044/222886120-bc389e06-16bf-45e3-90a4-e7f62fd3b15b.png)

This is a python script that can download the audio for a given podcast source from either YouTube or Spotify, convert the speech to text via OpenAI's Whisper API, summarize the text via OpenAI's GPT3 API (using either the GPT3 chat model or GPT3 Davinci text model), and chunk everything to fit within the limits of Whisper and GPT3 APIs.

## Installation

To use this script, you will need to install the necessary requirements. You can do this by running the following command in your terminal:

`pip install -r requirements.txt`

## Usage

To use this script, you will need to add your YouTube / Spotify URL to the summarizer.py file. Then, you can run the script by running the following command in your terminal:

`python summarizer.py`

The script will download the audio for your podcast source, convert the speech to text via OpenAI's Whisper API, summarize the text via OpenAI's GPT3 API, and chunk everything to fit within the limits of Whisper and GPT3 APIs. The script will also display the costs for both Whisper and GPT3 API usage.

## Optional Usage

For YouTube sources, you can skip the Whisper API for transcription and use the YouTube video's subtitles if they're available. To do this, you will need to modify the code in the summarizer.py file.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.