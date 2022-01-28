import colorsys
import math

from most_dominant_color import find_most_dominant_color_per_track


def step(color, repetitions=1):
    r, g, b = color

    lum = math.sqrt(.241 * r + .691 * g + .068 * b)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum

    return h2, lum, v2


def sort_by_most_dominant_color(tracks):
    sorted_by_color = sorted(zip(find_most_dominant_color_per_track(tracks), tracks), key=lambda tup: step(tup[0], 8))
    print(sorted_by_color)

    return [track for _, track in sorted_by_color]
