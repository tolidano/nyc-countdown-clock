import csv
import json


def main():
    """
    Station ID,Complex ID,GTFS Stop ID,Division,Line,Stop Name,Borough,Daytime Routes,Structure,GTFS Latitude,GTFS Longitude
    """
    lines = []
    header = False
    try:
        with open('Stations.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                if header:
                    lines.append({
                        'station_id': line[0],
                        'complex_id': line[1],
                        'gtfs_stop_id': line[2],
                        'division': line[3],
                        'line': line[4],
                        'station_name': line[5],
                        'borough': line[6],
                        'daytime_routes': line[7],
                        'structure': line[8],
                        'latitude': line[9],
                        'longitude': line[10],
                        })
                header = True
    except IOError:
        print('Stations.csv not found.')
    print(json.dumps(lines, indent=1))


if __name__ == '__main__':
    main()
