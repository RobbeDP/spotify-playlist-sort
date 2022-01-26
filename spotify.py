class Track:
    def __init__(self, id_, name_, album_name_, cover_url_):
        self.id = id_
        self.name = name_
        self.album_name = album_name_
        self.cover_url = cover_url_

    def __repr__(self):
        return f'Track({self.id}, {self.name}, {self.album_name}, {self.cover_url})'

    def __str__(self):
        return f'Track({self.id}, {self.name}, {self.album_name}, {self.cover_url})'


def get_playlist(client, playlist_id):
    tracks = []
    response = client.playlist_items(playlist_id)
    stop = False

    while not stop:
        for item in response['items']:
            track = item['track']

            tracks.append(Track(
                track['id'],
                track['name'],
                track['album']['name'],
                track['album']['images'][-1]['url']
            ))

        if response['next'] is None:
            stop = True
        else:
            response = client.playlist_items(playlist_id, offset=response['offset'] + response['limit'])

    return tracks
