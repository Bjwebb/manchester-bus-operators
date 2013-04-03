import json,re
from gtfs import csv_to_dict
routes = csv_to_dict(open('gtdf-out/routes.txt'), 'route_short_name') 

data = json.load(open('OpenData_BusRoutes.json'))
features = data['features']
new_features = []

feature_dict = {}
sno = re.compile('Service_no</td><td>([^<]*)</td>')
for feature in features:
    service = sno.search(feature['properties']['description']).group(1)
    print service
    try:
        route = routes[service.lstrip('0')]
    except KeyError:
        continue
    if service in feature_dict:
        f2 = feature_dict[service]
        for coords in feature['geometry']['coordinates']:
            if not coords in f2['geometry']['coordinates']:
                f2['geometry']['coordinates'].append(coords)
    else:
        feature_dict[service] = feature
        feature['properties'].update(route)
        new_features.append(feature)
    

data['features'] = new_features
json.dump(data, open('collapsed.json', 'w'))

