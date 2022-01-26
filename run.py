import configparser
import sys

from most_dominant_color import find_most_dominant_color_per_track
from spotify import get_playlist

import spotipy

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 run.py [playlist_id]')

    playlist_id = sys.argv[1]

    config = configparser.ConfigParser()
    config.read('secrets.ini')

    auth_manager = spotipy.SpotifyClientCredentials(
        config['spotify']['CLIENT_ID'],
        config['spotify']['CLIENT_SECRET']
    )
    client = spotipy.Spotify(auth_manager=auth_manager)

    tracks = get_playlist(client, playlist_id)
    most_dominant_colors = find_most_dominant_color_per_track(tracks)

    # TODO: Sort zip(tracks, most_dominant_colors) according to the color value.

    # TODO: Create new Spotify playlist.
