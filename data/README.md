This is a list of all files used in this project and their URL data source.
Note that these URLs are duplicated into the files.csv file for use with the download.py utility.

These files are kept in the repo because they are small and provide a great sample dataset to work with:

Subway Entrances (Geospatial) - entrances.geojson - https://data.cityofnewyork.us/api/geospatial/drex-xx56?method=export&format=GeoJSON
Subway Entrances - StationEntrances.csv - http://web.mta.info/developers/data/nyct/subway/StationEntrances.csv

Subway Stations (Geospatial) - stations.geojson - https://data.cityofnewyork.us/api/geospatial/arq3-7z49?method=export&format=GeoJSON
Station List - Stations.csv - http://web.mta.info/developers/data/nyct/subway/Stations.csv
Station Complexes - StationComplexes.csv - http://web.mta.info/developers/data/nyct/subway/StationComplexes.csv

Subway Lines (Geospatial) - lines.geojson - https://data.cityofnewyork.us/api/geospatial/3qz8-muuu?method=export&format=GeoJSON

Elevator / Escalator Listing - allequipments.aspx.xml - http://advisory.mtanyct.info/eedevwebsvc/allequipments.aspx

Colors - colors.csv - http://web.mta.info/developers/data/colors.csv

These files change on a regular basis and should be pulled frequently, as opposed to the rest, which can be pulled once per day or less:

Bus Service Status - ServiceStatusBus.xml - http://web.mta.info/status/ServiceStatusBus.xml
Service Status - serviceStatus.txt - http://web.mta.info/status/serviceStatus.txt
Line Service Status - ServiceStatusSubway.xml - http://web.mta.info/status/ServiceStatusSubway.xml
Elevator / Escalator Status - nyct_ene.xml - http://web.mta.info/developers/data/nyct/nyct_ene.xml

These files are added to the .gitignore file because they take up 650 MB of space:

LIRR GTFS JSON - lirr_gtfs.json - http://web.mta.info/developers/data/lirr/lirr_gtfs.json

Subway Schedule - subway - http://web.mta.info/developers/data/nyct/subway/google_transit.zip

Bus Schedule Bronx - bus/bronx - http://web.mta.info/developers/data/nyct/bus/google_transit_bronx.zip
Bus Schedule Brooklyn - bus/brooklyn - http://web.mta.info/developers/data/nyct/bus/google_transit_brooklyn.zip
Bus Schedule Manhattan - bus/manhattan - http://web.mta.info/developers/data/nyct/bus/google_transit_manhattan.zip
Bus Schedule Queens - bus/queens - http://web.mta.info/developers/data/nyct/bus/google_transit_queens.zip
Bus Schedule Staten Island - bus/staten_island - http://web.mta.info/developers/data/nyct/bus/google_transit_staten_island.zip

MNR Schedule - mnr - http://web.mta.info/developers/data/mnr/google_transit.zip

Bus Co Schedule - busco - http://web.mta.info/developers/data/busco/google_transit.zip
