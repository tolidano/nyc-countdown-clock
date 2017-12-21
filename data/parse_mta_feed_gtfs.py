import argparse
import os
import sys
from google.transit import gtfs_realtime_pb2


def main(file):
    """
    Parse the various GTFS status entities.
    """
    info = {'trip_updates': [], 'vehicles': [], 'alerts': []}
    try:
        with open(file, 'rb') as gtfs:
            data = gtfs.read()
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(data)
            for entity in feed.entity:
                if entity.HasField('trip_update'):
                    updates = []
                    stop_time_updates = len(entity.trip_update.stop_time_update)
                    if stop_time_updates:
                        for update in entity.trip_update.stop_time_update:
                            stop = {
                                'stop_sequence': update.stop_sequence,
                                'stop_id': update.stop_id,
                            }
                            if update.HasField('arrival'):
                                stop['arrival'] = update.arrival.time
                            if update.HasField('departure'):
                                stop['departure'] = update.departure.time
                            updates.append(stop)
                    info['trip_updates'].append({
                        'timestamp': entity.trip_update.timestamp,
                        'delay': entity.trip_update.delay,
                        'vehicle_id': entity.trip_update.vehicle.id,
                        'trip_id': entity.trip_update.trip.trip_id,
                        'start_date': entity.trip_update.trip.start_date,
                        'route_id': entity.trip_update.trip.route_id,
                        'direction_id': entity.trip_update.trip.direction_id,
                        'updates': updates,
                    })
                elif entity.HasField('vehicle'):
                    info['vehicles'].append({
                        'id': entity.vehicle.vehicle.id,
                        'stop_id': entity.vehicle.stop_id,
                        'timestamp': entity.vehicle.timestamp,
                        'latitude': entity.vehicle.position.latitude,
                        'longitude': entity.vehicle.position.longitude,
                        'bearing': entity.vehicle.position.bearing,
                        'trip_id': entity.vehicle.trip.trip_id,
                        'start_date': entity.vehicle.trip.start_date,
                        'route_id': entity.vehicle.trip.route_id,
                        'direction_id': entity.vehicle.trip.direction_id,
                    })
                elif entity.HasField('alert'):
                    times = []
                    active_periods = len(entity.alert.active_period)
                    if active_periods:
                        for period in entity.alert.active_period:
                            time = {
                                'start': period.start,
                            }
                            if period.HasField('end'):
                                time['end'] = period.end
                            times.append(time)
                    entities = []
                    informed_entities = len(entity.alert.informed_entity)
                    if informed_entities:
                        for informed in entity.alert.informed_entity:
                            entities.append({
                                'agency_id': informed.agency_id,
                                'route_id': informed.trip.route_id,
                                'direction_id': informed.trip.direction_id,
                            })
                    cause = 'NONE'
                    if entity.alert.HasField('cause'):
                        cause = entity.alert.cause
                    effect = 'NONE'
                    if entity.alert.HasField('effect'):
                        effect = entity.alert.effect
                    header = 'NONE'
                    if entity.alert.HasField('header_text'):
                        header = entity.alert.header_text.translation[0].text
                    description = 'NONE'
                    if entity.alert.HasField('description_text'):
                        description = entity.alert.description_text.translation[0].text
                    info['alerts'].append({
                        'times': times,
                        'entities': entities,
                        'cause': cause,
                        'effect': effect,
                        'header': header,
                        'description': description,
                    })
        print(info['vehicles'])
        print(info['alerts'])
        print(info['trip_updates'])
    except IOError:
        print('{} not found.'.format(file))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('feed', help='Feed to parse')
    ARGS = PARSER.parse_args()
    if not ARGS.feed or not os.path.exists(ARGS.feed):
        print('Must supply a valid feed file.')
        sys.exit()
    main(ARGS.feed)
