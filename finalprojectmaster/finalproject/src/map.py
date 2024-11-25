import pygame
import googlemaps

class Map:
    gmaps = googlemaps.Client(key="YOUR_API_KEY")

    geocode_result = gmaps.geocode('Binghamton University, New York')

    print(geocode_result)
    def __init__(self):
        pass