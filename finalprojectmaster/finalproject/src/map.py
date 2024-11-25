import pygame
import googlemaps

class Map:
    gmaps = googlemaps.Client(key="AIzaSyCYQ0SQNE5JmptRL-T4LipxdTiKsUTm_zs")

    geocode_result = gmaps.geocode('Binghamton University, New York')

    print(geocode_result)
    def __init__(self):
        pass