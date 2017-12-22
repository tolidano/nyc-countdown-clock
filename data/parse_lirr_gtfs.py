import json


def main():
    """
    Note that agency and calendar are not present here but show up in the transit folder parser
    Components to this file:
    Stops - all stops in the LIRR network
        {'stop': {'stop_id': '138', 'stop_name': 'Montauk', 'stop_lat': '41.0471', 'stop_lon': '-71.95388'}}
    Routes - all the chains of stops in the LIRR network
        Always appears to have route_type = 2
        {'route': {'route_id': '1', 'route_short_name': 'Babylon', 'route_long_name': 'Babylon', 'route_type': '2',
        'route_color': '00985F', 'route_text_color': 'FFFFFF'}}
    Trips - a container for a route for a train
        trip_headsign is what is written on the train itself
        direction_id is 0 for east and 1 for west (no such thing as northbound/southbound)
        {'trip': {'route_id': '1', 'service_id': 'GO303_1765', 'trip_id': 'GO303_172',
        'trip_headsign': 'Babylon', 'trip_short_name': '2', 'direction_id': '0', 'shape_id': 0}}
    Shapes - the shapes of the routes
        There appears to be some sort of data duplication here and there is another copy of the trips as well
        {'shape_id': 1, 'shape_pt_lat': 79, 'shape_pt_lon': 45, 'shape_pt_sequence': 1}
    Times - arrival and departure times at each stop
        {'trip_id': 1, 'arrival_time': 'time', 'departure_time': 'time', 'stop_id': 1, 'stop_sequence': 1}
    Dates - service date exceptions
        {'service_id': 'ID', 'service_date': 'date', 'exception_type': 1}
    """
    lirr = {'stops': {}, 'routes': {}, 'trips': {}, 'shapes': {}, 'times': {}, 'dates': {}}
    try:
        with open('lirr_gtfs.json', 'r') as data:
            contents = json.load(data)
            gtfs = contents['gtfs']
            for stop in gtfs['stops']:
                data = stop['stop']
                lirr['stops'][data['stop_id']] = {
                    'stop_id': data['stop_id'],
                    'name': data['stop_name'],
                    'latitude': data['stop_lat'],
                    'longitude': data['stop_lon'],
                }
            for route in gtfs['routes']:
                data = route['route']
                lirr['routes'][data['route_id']] = {
                    'route_id': data['route_id'],
                    'short_name': data['route_short_name'],
                    'name': data['route_long_name'],
                    'type': data['route_type'], # appears to always be 2
                    'color': data['route_color'],
                    'text_color': data['route_text_color'],
                }
            for trip in gtfs['trips']:
                data = trip['trip']
                direction = 'E'
                if data['direction_id'] == '1':
                    direction = 'W'
                lirr['trips'][data['trip_id']] = {
                    'trip_id': data['trip_id'],
                    'route_id': data['route_id'],
                    'service_id': data['service_id'],
                    'sign': data['trip_headsign'],
                    'short_name': data['trip_short_name'],
                    'direction': direction,
                    'shape_id': data['shape_id'],
                }
            if not len(lirr['trips']) > 0:
                for shape in gtfs['shapes']:
                    if 'trip' in shape:
                        data = shape['trip']
                        direction = 'E'
                        if data['direction_id'] == '1':
                            direction = 'W'
                        lirr['trips'][data['trip_id']] = {
                            'trip_id': data['trip_id'],
                            'route_id': data['route_id'],
                            'service_id': data['service_id'],
                            'sign': data['trip_headsign'],
                            'short_name': data['trip_short_name'],
                            'direction': direction,
                            'shape_id': data['shape_id'],
                        }
            for shape in gtfs['shapes']:
                if 'shape' in shape:
                    data = shape['shape']
                    oid = data['shape_id']
                    if oid not in lirr['shapes']:
                        lirr['shapes'][oid] = []
                    lirr['shapes'][oid].append({
                        'shape_id': oid,
                        'latitude': data['shape_pt_lat'],
                        'longitude': data['shape_pt_lon'],
                        'sequence': data['shape_pt_sequence'],
                    })
            for times in gtfs['stop_times']:
                data = times['stop_time']
                oid = data['trip_id']
                if oid not in lirr['times']:
                    lirr['times'][oid] = []
                lirr['times'][oid].append({
                    'trip_id': oid,
                    'arrival_time': data['arrival_time'],
                    'departure_time': data['departure_time'],
                    'stop_id': data['stop_id'],
                    'sequence': data['stop_sequence'],
                })
            for dates in gtfs['calendar_dates']:
                data = dates['calendar_date']
                oid = data['service_id']
                if oid not in lirr['dates']:
                    lirr['dates'][oid] = []
                lirr['dates'][oid].append({
                    'service_id': oid,
                    'service_date': data['service_date'],
                    'exception_type': data['exception_type'],
                })
    except IOError:
        print('lirr_gtfs.json not found.')
    print(json.dumps(lirr, indent=1))


if __name__ == '__main__':
    main()
