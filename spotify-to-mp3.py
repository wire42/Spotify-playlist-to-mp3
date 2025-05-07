import os
import re
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from savify import Savify
from savify.types import Format, Quality, SpotifyType

def is_valid_spotify_playlist_url(url):
    pattern = r'^https?://open\.spotify\.com/playlist/[a-zA-Z0-9]+'
    return re.match(pattern, url) is not None

def get_playlist_name(sp, playlist_url):
    try:
        playlist = sp.playlist(playlist_url)
        return playlist['name']
    except Exception as e:
        print(f"Error fetching playlist name: {e}")
        return "downloaded_songs"

def main():
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID", "")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")

    if not CLIENT_ID or not CLIENT_SECRET:
        print("Spotify API credentials not found. Please set CLIENT_ID and CLIENT_SECRET in your .env file.")
        return

    playlist_url = input("Enter Spotify playlist URL: ").strip()
    if not is_valid_spotify_playlist_url(playlist_url):
        print("Invalid Spotify playlist URL.")
        return

    # Auth with Spotipy to get playlist info
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
    playlist_name = get_playlist_name(sp, playlist_url)
    output_dir = input(f"Enter output directory (default: ./{playlist_name}): ").strip() or f"./{playlist_name}"
    os.makedirs(output_dir, exist_ok=True)

    # Prepare Savify
    savify = Savify(
        quality=Quality.BEST,
        download_format=Format.MP3,
        output_path=output_dir,
        skip_cover_art=False
    )

    # Fetch tracks
    success, failed = [], []
    try:
        results = sp.playlist_tracks(playlist_url)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
    except Exception as e:
        print(f"Failed to fetch playlist tracks: {e}")
        return

    print(f"Found {len(tracks)} tracks. Starting download...")

    for item in tracks:
        track = item['track']
        track_name = track['name']
        artists = ', '.join([a['name'] for a in track['artists']])
        track_url = track['external_urls']['spotify']
        try:
            savify.download(track_url, SpotifyType.TRACK)
            print(f"Downloaded: {track_name} - {artists}")
            success.append(f"{track_name} - {artists}")
        except Exception as e:
            print(f"Failed: {track_name} - {artists} ({e})")
            failed.append(f"{track_name} - {artists}: {e}")

    # Write log
    log_path = os.path.join(output_dir, "download_report.txt")
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("Downloaded:\n")
        log.write("\n".join(success))
        log.write("\n\nFailed:\n")
        log.write("\n".join(failed))

    print(f"\nDownload complete! Log saved to {log_path}")

if __name__ == "__main__":
    main()
