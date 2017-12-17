import argparse
import csv
import json
import os
import sys


def main(folder):
    """
    There are 8 files in the folder which resemble the LIRR GTFS JSON output.
    - agency.txt - the name and number of the MTA, single line after header, ignored here
    - calendar.txt - service IDs and their dates of operation
        service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date
    - calendar_dates.txt - dates where alternate service IDs are in effect
        service_id,date,exception_type
    - routes.txt - all possible routes
        route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color
    - shapes.txt - geographic points defining a route
        shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled (busco does not have this)
    - stop_times.txt - times for a vehicle at each stop along each trip
        trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type
    - stops.txt - all possible stops
        stop_id,stop_name,stop_desc,stop_lat,stop_lon
    - trips.txt - a trip on a route for a service in a given direction
        route_id,service_id,trip_id,trip_headsign,direction_id,block_id,shape_id
    """
    print('Folder selected: ' + folder)
    data = {'calendar': {}, 'dates': {}, 'routes': {}, 'shapes': {}, 'stop_times': {}, 'stops': {}, 'trips': {}}
    header = False
    # service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date
    with open(folder + '/calendar.txt', 'r') as calendar:
        contents = csv.reader(calendar)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                entry = {
                    'service_id': oid,
                    'monday': line[1],
                    'tuesday': line[2],
                    'wednesday': line[3],
                    'thursday': line[4],
                    'friday': line[5],
                    'saturday': line[6],
                    'sunday': line[7],
                    'start_date': line[8],
                    'end_date': line[9],
                }
                data['calendar'][oid] = entry
    header = False
    # service_id,date,exception_type
    with open(folder + '/calendar_dates.txt', 'r') as dates:
        contents = csv.reader(dates)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                if oid not in data['dates']:
                    data['dates'][oid] = []
                data['dates'][oid].append({
                    'service_id': oid,
                    'date': line[1],
                    'exception_type': line[2],
                })
    header = False
    # route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color
    with open(folder + '/routes.txt', 'r') as dates:
        contents = csv.reader(dates)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                data['routes'][oid] = {
                    'route_id': oid,
                    'agency_id': line[1],
                    'short_name': line[2],
                    'name': line[3],
                    'description': line[4],
                    'url': line[5],
                    'color': line[6],
                    'text_color': line[7],
                }
    header = False
    # shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled
    with open(folder + '/shapes.txt', 'r') as shapes:
        contents = csv.reader(shapes)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                if oid not in data['shapes']:
                    data['shapes'][oid] = []
                distance = 0
                if len(line) > 4:
                    distance = line[4]
                data['shapes'][oid].append({
                    'shape_id': oid,
                    'latitude': line[1],
                    'longitude': line[2],
                    'sequence': line[3],
                    'distance': distance,
                })
    header = False
    # trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type
    with open(folder + '/stop_times.txt', 'r') as times:
        contents = csv.reader(times)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                if oid not in data['stop_times']:
                    data['stop_times'][oid] = []
                data['stop_times'][oid].append({
                    'trip_id': oid,
                    'arrival_time': line[1],
                    'departure_time': line[2],
                    'stop_id': line[3],
                    'sequence': line[4],
                    'pickup_type': line[5],
                    'drop_off_type': line[6],
                })
    header = False
    # stop_id,stop_name,stop_desc,stop_lat,stop_lon
    with open(folder + '/stops.txt', 'r') as times:
        contents = csv.reader(times)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                if oid not in data['stops']:
                    data['stops'][oid] = []
                data['stops'][oid].append({
                    'stop_id': oid,
                    'name': line[1],
                    'description': line[2],
                    'latitude': line[3],
                    'longitude': line[4],
                })
    header = False
    # route_id,service_id,trip_id,trip_headsign,direction_id,block_id,shape_id
    with open(folder + '/trips.txt', 'r') as times:
        contents = csv.reader(times)
        for line in contents:
            if not header:
                header = True
            else:
                oid = line[0]
                if oid not in data['trips']:
                    data['trips'][oid] = []
                direction = 'E'
                if line[4] == '1':
                    direction = 'W'
                shape_id = ''
                if len(line) > 6:
                    shape_id = line[6]
                data['trips'][oid].append({
                    'route_id': oid,
                    'service_id': line[1],
                    'trip_id': line[2],
                    'trip_headsign': line[3],
                    'direction': direction,
                    'block_id': line[5],
                    'shape_id': shape_id,
                })

    print(json.dumps(data, indent=1))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('folder', help='Folder to parse')
    ARGS = PARSER.parse_args()
    if not ARGS.folder or not os.path.exists(ARGS.folder):
        print('Must supply a valid directory.')
        sys.exit()
    expected_text_files = ['agency', 'calendar', 'calendar_dates', 'routes', 'shapes', 'stop_times', 'stops', 'trips']
    files_missing = []
    for file in expected_text_files:
        if not os.path.exists(ARGS.folder + '/' + file + '.txt'):
            print('File missing in folder: ' + file)
            files_missing.append(file)
    if files_missing:
        print('Missing files: ', files_missing)
        sys.exit()
    main(ARGS.folder)
