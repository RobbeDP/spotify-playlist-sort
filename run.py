import configparser
import sys

from sort import sort_by_most_dominant_color
from spotify import get_playlist_name, get_playlist_tracks, create_playlist

import spotipy

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 run.py [playlist_id]')

    playlist_id = sys.argv[1]

    config = configparser.ConfigParser()
    config.read('secrets.ini')

    auth_manager = spotipy.SpotifyOAuth(
        config['spotify']['CLIENT_ID'],
        config['spotify']['CLIENT_SECRET'],
        config['spotify']['REDIRECT_URI'],
        scope='playlist-modify-public'
    )
    client = spotipy.Spotify(auth_manager=auth_manager)

    name = get_playlist_name(client, playlist_id)
    tracks = get_playlist_tracks(client, playlist_id)
    tracks = sort_by_most_dominant_color(tracks)

    track_ids = [track.id for track in tracks]
    create_playlist(client, f'{name} - SORTED', track_ids)
