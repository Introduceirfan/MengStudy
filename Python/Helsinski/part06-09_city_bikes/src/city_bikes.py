# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(files):
    station = {}
    with open(files) as new_files:
        for line in new_files:
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            station[parts[3]] = (float(parts[0]), float(parts[1]))
    return station

def distance(stations: dict, station1: str, station2: str):

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stey):
    max_distance = 0
    stat1 = ""
    stat2 = ""
    for item in stey:
        

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)