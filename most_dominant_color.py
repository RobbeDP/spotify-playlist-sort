import colorthief
import os
import requests


# Returns a list that contains the most dominant color on the album cover of each given track.
# Index `i` in `tracks` corresponds to index `i` in `most_dominant_colors`.
def find_most_dominant_color_per_track(tracks):
    most_dominant_colors = []
    temp_file = 'temp.jpg'

    for i, track in enumerate(tracks):
        response = requests.get(track.cover_url)

        with open(temp_file, 'wb') as file:
            file.write(response.content)

        color_thief = colorthief.ColorThief(temp_file)
        most_dominant_colors.append(color_thief.get_color())

    # Remove the temporary file that has been created.
    os.remove(temp_file)

    return most_dominant_colors
