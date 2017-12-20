import argparse
import os
import requests
import yaml
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

    subway_feed_url = 'http://datamine.mta.info/mta_esi.php?key={}&feed_id={}'
    feed_ids = [1, 26, 16, 21, 2, 11, 31]
    lines = []
    for feed_id in feed_ids:
        lines.append({
            'name': 'Feed {}'.format(feed_id),
            'local': 'feed{}.gtfs'.format(feed_id),
            'remote': subway_feed_url.format(_MTA_FEED_API_KEY, feed_id)
        })
    lines.append({
        'name': 'LIRR',
        'local': 'lirr_status.json',
        'remote': 'https://mnorth.prod.acquia-sites.com/wse/LIRR/gtfsrt/realtime/{}/json'.format(_MTA_FEED_API_KEY)
    })
    lines.append({
        'name': 'MNR',
        'local': 'mnr_status.gtfs',
        'remote': 'https://mnorth.prod.acquia-sites.com/wse/gtfsrtwebapi/v1/gtfsrt/{}/getfeed'.format(_MTA_FEED_API_KEY)
    })
    lines.append({
        'name': 'MTA Bus Trip Updates',
        'local': 'mta_bus_trip_updates.gtfs',
        'remote': 'http://gtfsrt.prod.obanyc.com/tripUpdates?key={}'.format(_MTA_BUS_TIME_API_KEY)
    })
    lines.append({
        'name': 'MTA Bus Vehicle Positions',
        'local': 'mta_bus_vehicle_positions.gtfs',
        'remote': 'http://gtfsrt.prod.obanyc.com/vehiclePositions?key={}'.format(_MTA_BUS_TIME_API_KEY)
    })
    lines.append({
        'name': 'MTA Bus Alerts',
        'local': 'mta_bus_alerts.gtfs',
        'remote': 'http://gtfsrt.prod.obanyc.com/alerts?key={}'.format(_MTA_BUS_TIME_API_KEY)
    })
    for line in lines:
        download(line['name'], line['local'], line['remote'])


def download(name, local_path, server_path):
    print('File: ' + name + ' URL: ' + server_path)
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
