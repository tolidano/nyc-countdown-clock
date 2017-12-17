import argparse
import os
import requests
import yaml
from google.transit import gtfs_realtime_pb2
from requests.exceptions import ConnectionError


_ONE_MEGABYTE = 1024 * 1024
_MTA_FEED_API_KEY = None
_MTA_BUS_TIME_API_KEY = None


def main(config_file):
    global _MTA_FEED_API_KEY
    global _MTA_BUS_TIME_API_KEY
    if not os.path.exists(config_file):
        print('Config not found.')
        return
    with open(config_file, 'rb') as stream:
        try:
            loaded_config = yaml.load(stream)
            _MTA_FEED_API_KEY = loaded_config['mta_feed_api_key']
            _MTA_BUS_TIME_API_KEY = loaded_config['mta_bus_time_api_key']
        except (yaml.YAMLError, AttributeError):
            print('Specify mta_feed_api_key and mta_bus_time_api_key in YAML config')

    subway_feed_url = 'http://datamine.mta.info/mta_esi.php?key=%KEY%&feed_id='
    feed_ids = [1, 26, 16, 21, 2, 11, 31]
    feeds = {}
    for feed_id in feed_ids:
        feeds['S' + str(feed_id)] = subway_feed_url + str(feed_id)

    feeds['LIRR'] = 'https://mnorth.prod.acquia-sites.com/wse/LIRR/gtfsrt/realtime/%KEY%/json' #or proto
    feeds['MNR'] = 'https://mnorth.prod.acquia-sites.com/wse/gtfsrtwebapi/v1/gtfsrt/%KEY%/getfeed'

    feeds['BUS-TU'] = 'http://gtfsrt.prod.obanyc.com/tripUpdates?key=%KEY%'
    feeds['BUS-POS'] = 'http://gtfsrt.prod.obanyc.com/vehiclePositions?key=%KEY%'
    feeds['BUS-ALERTS'] = 'http://gtfsrt.prod.obanyc.com/alerts?key=%KEY%'

    lines = [
        {},
    ]
    for line in lines:
        download(line['name'], line['local'], line['remote'])


def download(name, local_path, server_path):
    print('File: ' + name)
    try:
        response = requests.get(server_path, stream=True)
    except ConnectionError:
        response = None
        print('Unable to download {}'.format(server_path))
    if response:
        print('Successfully opened streaming connection to {}'.format(server_path))
        final_path = local_path
        print('Writing to local path {}'.format(final_path))
        chunks = 0
        with open(final_path, 'wb') as handle:
            for chunk in response.iter_content(chunk_size=_ONE_MEGABYTE):
                if chunk:
                    handle.write(chunk)
                    chunks += 1
        print('Finished downloading {} to {}'.format(server_path, final_path))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('config', help='Config file location', default='../config.yaml')
    ARGS = PARSER.parse_args()
    main(ARGS.config)
