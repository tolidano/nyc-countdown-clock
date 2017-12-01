import json


def main():
    """
    {
        "type":"Feature",
        "properties": {
            "name":"Astor Pl",
            "url":"http://web.mta.info/nyct/service/",
            "line":"4-6-6 Express",
            "objectid":"1",
            "notes":"4 nights, 6-all times, 6 Express-weekdays AM southbound, PM northbound"
        },
        "geometry": {
            "type":"Point",
            "coordinates": [-73.99106999861966,40.73005400028978]
        }
    }
    """
    stations = []
    try:
        with open('stations.geojson', 'r') as data:
            contents = json.load(data)
            for station in contents['features']:
                name = station['properties']['name']
                url = station['properties']['url']
                object_id = station['properties']['objectid']
                notes = station['properties']['notes']
                latitude = station['geometry']['coordinates'][0]
                longitude = station['geometry']['coordinates'][1]
                lines = []
                for line in station['properties']['line'].split('-'):
                    lines.append(line)
                stations.append({
                    'name': name,
                    'url': url,
                    'object_id': object_id,
                    'notes': notes,
                    'latitude': latitude,
                    'longitude': longitude,
                    'lines': lines,
                })
    except IOError:
        print('stations.geojson not found.')
    print(json.dumps(stations, indent=1))


if __name__ == '__main__':
    main()
