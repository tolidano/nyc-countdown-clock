import json


def main():
    """
    {
        "type":"Feature",
        "properties":{
            "objectid":"1520",
            "url":"http://web.mta.info/nyct/service/",
            "name":"179th Pl & Hillside Ave at SW corner",
            "line":"F"
            },
        "geometry":{
            "type":"Point",
            "coordinates":[-73.78337700001022,40.71258100132801]
            }
    }
    """
    entrances = []
    try:
        with open('entrances.geojson', 'r') as data:
            contents = json.load(data)
            for entrance in contents['features']:
                object_id = entrance['properties']['objectid']
                name = entrance['properties']['name']
                line = entrance['properties']['line']
                longitude = entrance['geometry']['coordinates'][0]
                latitude = entrance['geometry']['coordinates'][1]
                entrances.append({
                    'object_id': object_id,
                    'name': name,
                    'line': line,
                    'longitude': longitude,
                    'latitude': latitude,
                    })
    except IOError:
        print('entrances.geojson not found.')
    print(entrances)


if __name__ == '__main__':
    main()
