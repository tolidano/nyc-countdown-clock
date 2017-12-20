import json
from google.transit import gtfs_realtime_pb2


def main():
    """

    """
    lirr = {'status': []}
    try:
        with open('lirr_gtfs.json', 'r') as data:
            print(data)
    except IOError:
        print('lirr_gtfs.json not found.')
    print(json.dumps(lirr, indent=1))


if __name__ == '__main__':
    main()
