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
    def __init__(self):
        """
        Initialize a countdown clock.

        :param string config_file: path to YAML config file on disk
        """
        self.clock = None

    def list(self):
        """
        List all available stops and stations.

        :return dict: all available bus stops and subway/train stations
        """
        return self.clock

    def get_times_for_stop_on_line(self, stop=None, line=None):
        """
        Get the time for a particular stop on a line.

        :param string stop: a bus stop or subway/train station (or all stops/stations)
        :param string line: a subway/train line or bus route (or all lines/routes)

        :return dict: nearby arrival times for the stop and line requested
        """
        if stop is None and line is None:
            raise ValueError('Must pass stop or line or both')

        return self.clock
