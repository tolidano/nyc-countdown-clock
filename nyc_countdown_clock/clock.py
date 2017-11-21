"""
NYC Countdown Clock module.
"""
from google.transit import gtfs_realtime_pb2
from os import path
import yaml


class Clock(object):
    """
    Countdown clock for upcoming MTA transit arrivals.
    """

    def __init__(self, config_file):
        """
        Initialize a countdown clock.

        :param string config_file: path to YAML config file on disk
        """
        self.subway_feed_url = 'http://datamine.mta.info/mta_esi.php?key=%KEY%&feed_id='
        self.feed_ids = [1, 26, 16, 21, 2, 11, 31]
        self.feeds = {}
        for feed_id in self.feed_ids:
            self.feeds['S' + str(feed_id)] = self.subway_feed_url + str(feed_id)

        # or proto
        self.feeds['LIRR'] = \
            'https://mnorth.prod.acquia-sites.com/wse/LIRR/gtfsrt/realtime/%KEY%/json'
        self.feeds['MNR'] = \
            'https://mnorth.prod.acquia-sites.com/wse/gtfsrtwebapi/v1/gtfsrt/%KEY%/getfeed'

        self.subway_lines = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'L', 'M', 'N', 'Q', 'R', 'S', 'T', 'W', 'Z',
                             '1', '2', '3', '4', '5', '6', '6X', '7', 'SS']
        self.bus_lines = ['Q32', 'Q60', 'Q101', 'Q102', 'M5X', 'BX1', 'BX2']
        self.train_branches = ['Far Rockaway', 'Babylon', 'Port Washington', 'Speonk', 'Long Beach', 'Hempstead',
                               'West Hempstead', 'Stonybrook', ]
        self.lines = {}

        self.mta_feed_api_key = 'Unknown'
        self.mta_bus_time_api_key = 'Unknown'
        if not path.exists(config_file):
            raise FileNotFoundError('Config file ' + config_file + ' not found.')
        with open(config_file, 'rb') as stream:
            try:
                loaded_config = yaml.load(stream)
                self.mta_feed_api_key = loaded_config['mta_feed_api_key']
                self.mta_bus_time_api_key = loaded_config['mta_bus_time_api_key']
            except (yaml.YAMLError, AttributeError):
                print('Specify mta_feed_api_key and mta_bus_time_api_key in YAML config')

    def list(self):
        """
        List all available stops and stations.

        :return dict: all available bus stops and subway/train stations
        """
        return {}

    def get_times_for_stop_on_line(self, stop=None, line=None):
        """
        Get the time for a particular stop on a line.

        :param string stop: a bus stop or subway/train station (or all stops/stations)
        :param string line: a subway/train line or bus route (or all lines/routes)

        :return dict: nearby arrival times for the stop and line requested
        """
        if stop is None and line is None:
            raise ValueError('Must pass stop or line or both')

        return {}
