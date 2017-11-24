import csv


def main():
    """
    Division,Line,Station_Name,Station_Latitude,Station_Longitude,Route_1,Route_2,Route_3,Route_4,Route_5,Route_6,Route_7,Route_8,Route_9,Route_10,Route_11,Entrance_Type,Entry,Exit_Only,Vending,Staffing,Staff_Hours,ADA,ADA_Notes,Free_Crossover,North_South_Street,East_West_Street,Corner,Latitude,Longitude
BMT,Astoria,Ditmars Blvd,40.775036,-73.912034,N,Q,,,,,,,,,,Stair,YES,,YES,FULL,,FALSE,,TRUE,31st St,23rd Ave,NW,40.775149,-73.912074
BMT,Astoria,Ditmars Blvd,40.775036,-73.912034,N,Q,,,,,,,,,,Stair,YES,,YES,FULL,,FALSE,,TRUE,31st St,23rd Ave,NE,40.77481,-73.912151
BMT,Astoria,Ditmars Blvd,40.775036,-73.912034,N,Q,,,,,,,,,,Stair,YES,,YES,FULL,,FALSE,,TRUE,31st St,23rd Ave,NE,40.775025,-73.911891
BMT,
    """
    stations = []
    station_name = 'NEW'
    header = False
    try:
        with open('StationEntrances.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                if header:
                    if station_name != line[2]:
                        if station_name != 'NEW':
                            stations.append(station)
                        station_name = line[2]
                        routes = []
                        for j in range(5,15):
                            if line[j]:
                                routes.append(line[j])
                        station = {
                            'division': line[0],
                            'line': line[1],
                            'station_name': station_name,
                            'station_latitude': line[3],
                            'station_longitude': line[4],
                            'free_crossover': True if line[24] == 'YES' else False,
                            'routes': routes,
                            'entrances': [],
                            }
                    station['entrances'].append({
                        'type': line[16],
                        'entry': True if line[17] == 'YES' else False,
                        'exit_only': True if line[18] == 'YES' else False,
                        'vending': True if line[19] == 'YES' else False,
                        'staffing': line[20],
                        'staff_hours': line[21],
                        'ada': True if line[22] == 'YES' else False,
                        'ada_notes': line[23],
                        'north_south': line[25],
                        'east_west': line[26],
                        'corner': line[27],
                        'latitude': line[28],
                        'longitude': line[29],
                        })
                header = True
    except IOError:
        print('StationEntrances.csv not found.')
    print(stations)


if __name__ == '__main__':
    main()
