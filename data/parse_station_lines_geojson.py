import json


def main():
    """
    {
        "type":"Feature",
        "properties":{
            "name":"G",
            "url":"http://web.mta.info/nyct/service/",
            "rt_symbol":"G",
            "objectid":"753",
            "id":"2000393",
            "shape_len":"2438.20024902"
        },
        "geometry":{
            "type":"LineString",
            "coordinates":[
                [-73.99487524803018,40.6802035460625],
                [-73.99427469414127,40.68081016270495],
                [-73.9942168049715,40.68088280879707],
                [-73.9941660725898,40.68094977567929],
                [-73.99411471677327,40.681016234616614],
                [-73.9940635700395,40.68108477012707],
                [-73.99401368539809,40.6811526149855],
                [-73.99396235156854,40.68122105948818],
                [-73.99391126703496,40.681291555351955],
                [-73.99386095364044,40.68136199360065],
                [-73.99381034674546,40.6814328424454],
                [-73.99375975375001,40.68150569581264],
                [-73.99370975453519,40.681577696402535],
                [-73.99365946654771,40.68165011029012],
                [-73.99360890506807,40.68172392984253],
                [-73.99355835994191,40.68179873453544],
                [-73.99350838602531,40.681873696827665],
                [-73.99066967148987,40.68606925530288]
            ]
        }
    },
    {
        "type":"Feature",
        "properties":{
            "name":"G",
            "url":"http://web.mta.info/nyct/service/",
            "rt_symbol":"G",
            "objectid":"754",
            "id":"2000394",
            "shape_len":"3872.83441063"
        },
        "geometry":{
            "type":"LineString",
            "coordinates":[
                [-73.97957543205142,40.65993069553076],
                [-73.97965516869557,40.65981741117469],
                [-73.98019277510113,40.65886613985546],
                [-73.98024660003978,40.658549026771446],
                [-73.98021982320536,40.65825235955759],
                [-73.98009901040854,40.657976135835966],
                [-73.97977670558397,40.65771010569873],
                [-73.97717129293514,40.65618538710448],
                [-73.976781852058,40.65590910620024],
                [-73.97651334328621,40.655520321024085],
                [-73.97633885050956,40.65516224510277],
                [-73.97573559925392,40.65187837176674],
                [-73.97566871827712,40.65112135659427],
                [-73.9756594994904,40.65072922971845]
            ]
        }
    }
    """
    lines = {}
    try:
        with open('lines.geojson', 'r') as data:
            contents = json.load(data)
            for line in contents['features']:
                name = line['properties']['name']
                url = line['properties']['url']
                symbol = line['properties']['rt_symbol']
                object_id = line['properties']['objectid']
                segment_id = line['properties']['id']
                shape_len = line['properties']['shape_len']
                coordinates = []
                for point in line['geometry']['coordinates']:
                    coordinates.extend(point)
                key = name + '|' + symbol
                if not key in lines:
                    lines[key] = {
                        'name': name,
                        'url': url,
                        'symbol': symbol,
                        'segments': []
                        }
                lines[key]['segments'].append({
                    'object_id': object_id,
                    'segment_id': segment_id,
                    'shape_len': shape_len,
                    'coordinates': coordinates,
                    })
    except IOError:
        print('lines.geojson not found.')
    print(json.dumps(lines, indent=1))


if __name__ == '__main__':
    main()
