Spotify Playlist to MP3 Downloader 
Created by Patrick Elliott

This Python script downloads all tracks from a Spotify playlist as MP3 files.
It fetches playlist info using the Spotify API and downloads audio via YouTube using Savify.
Tracks are organized into a folder named after your playlist, and a log file is generated showing which tracks were downloaded or failed.

Features
Interactive: Prompts for playlist URL and output directory

Validation: Checks playlist URL format

Organized: Downloads saved in a folder named after the playlist

Logging: Creates download_report.txt with success/failure info

Error Handling: Gracefully manages common errors

Requirements
Python 3.7+

ffmpeg (must be in your system PATH)
https://ffmpeg.org/download.html


Python packages: savify, spotipy, python-dotenv

Install dependencies with:

bash
pip install savify spotipy python-dotenv


Setup:

1. Create a Spotify Developer App
Go to Spotify Developer Dashboard

Log in and click "Create an App"

Copy your Client ID and Client Secret

2. Create a .env File
Create a file named .env in the same directory as the script:

text
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
Example:

text
CLIENT_ID=1234567890abcdef1234567890abcdef
CLIENT_SECRET=abcdef1234567890abcdef1234567890
Usage
Make sure ffmpeg is installed and available in your system PATH.

Run the script:

bash
python download_spotify_playlist.py
When prompted:

Enter your Spotify playlist URL (e.g., https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M)

Enter an output directory or press Enter to use the default

The script will:

Download each track as an MP3

Save files in a folder named after your playlist

Create a download_report.txt with the results

Notes
Personal use only. Downloading copyrighted music may violate Spotify’s terms of service.

For large playlists, downloading may take some time.

If you have issues, check your .env credentials and ensure ffmpeg is installed.

Example Output
text
Downloaded: Song Title 1 - Artist Name
Downloaded: Song Title 2 - Artist Name
Failed: Song Title 3 - Artist Name (error message)
...
Download complete! Log saved to ./My_Playlist/download_report.txt
Troubleshooting
Invalid playlist URL: Make sure you copy the full Spotify playlist link.

ffmpeg not found: Install ffmpeg and ensure it’s in your system PATH.

Spotify API errors: Double-check your .env credentials.

License
This project is for educational and personal use only.

Let me know if you need anything else!

