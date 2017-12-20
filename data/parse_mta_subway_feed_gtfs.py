import argparse
import os
import sys
from google.transit import gtfs_realtime_pb2


def main(file):
    """

    """
    try:
        with open(file, 'rb') as gtfs:
            data = gtfs.read()
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(data)
            for entity in feed.entity:
                if entity.HasField('trip_update'):
                    print('----TRIP_UPDATE----')
                    print(entity)
                elif entity.HasField('vehicle'):
                    print('----VEHICLE----')
                    print(entity)
                elif entity.HasField('alert'):
                    print('----ALERT----')
                    print(entity)
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
