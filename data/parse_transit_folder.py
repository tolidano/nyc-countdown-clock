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
    - stop_times.txt - times for a vehicle at each stop along each trip
    - stops.txt - all possible stops
    - trips.txt - a trip on a route for a service in a given direction
    """
    print('Folder selected: ' + folder)
    data = {'calendar': {}, 'dates': {}, 'routes': {}}
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
