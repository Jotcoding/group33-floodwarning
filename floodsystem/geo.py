# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

























































def stations_with_river(stations):
    stationRivers = set()
    for i in range(len(stations)):
        if stations[i].river != None:
          stationRivers.add(stations[i].river)
    return stationRivers
def stations_by_river(stations):
    Riverstations = {}
    for i in range(len(stations)): # go through each station and assign variable to river name and station name
        river_name = stations[i].river
        station_name = [stations[i].name] 
        if river_name in Riverstations:
             Riverstations[stations[i].river].append(station_name)
        else:
          a = {river_name:station_name}
          Riverstations.update(a)
     
    return Riverstations

def rivers_by_station_number(stations, N):
    Top_list=[]
    River_dict = stations_by_river(stations)

    station_number = []
    river_key = list(River_dict.keys())
    for river in River_dict:
        station_number.append(len(River_dict[river]))
    
    bob = list(zip(river_key,station_number))
    bob.sort(key=lambda x:x[1])    
    Top_list = bob[len(bob)-N:len(bob)]
    
    return Top_list

        

   









from .utils import sorted_by_key  # noqa
