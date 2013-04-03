import json, re, csv
from gtfs import routes
from collections import defaultdict
from copy import deepcopy

routes_by_shortname = defaultdict(dict)
for route in routes.values():
    sn = route['route_short_name'].strip()
    aid = route['agency_id']
    if aid in routes_by_shortname[sn]:
        routes_by_shortname[sn][aid]['count'] += route['count']
    else:
        routes_by_shortname[sn][aid] = route

print routes_by_shortname
json.dump(routes_by_shortname, open('routes.json', 'w'))

data = json.load(open('OpenData_BusRoutes.json'))
features = data['features']
new_features = []

feature_dict = {}
sno = re.compile('Service_no</td><td>([^<]*)</td>')
for feature in features:
    service = sno.search(feature['properties']['description']).group(1)
    print service
    try:
        routes = routes_by_shortname[service.lstrip('0')]
    except KeyError:
        continue
    if service in feature_dict:
        f2 = feature_dict[service]
        for coords in feature['geometry']['coordinates']:
            if not coords in f2['geometry']['coordinates']:
                f2['geometry']['coordinates'].append(coords)
    else:
        feature_dict[service] = feature
        for route in routes.values():
            route['offset'] = 0

            new_feature = deepcopy(feature)
            new_feature['properties'].update(route)
            new_features.append(new_feature)

agency_features = defaultdict(list)
for feature in new_features:
    coordss = feature['geometry']['coordinates']
    feature['geometry']['coordinates'] = None
    feature['geometry']['type'] = 'LineString'
    for coords in coordss:
        new_feature = deepcopy(feature)
        new_feature['geometry']['coordinates'] = coords
        agency_features[feature['properties']['agency_id']].append(new_feature)

new_agency_features = defaultdict(list)
new_new_features = []
for agency_id, features in agency_features.items():
    for feature in features:
        for f2 in new_agency_features[agency_id]:
            if feature['geometry']['coordinates'] == f2['geometry']['coordinates']:
                f2['properties']['count'] += feature['properties']['count']
                f2['properties']['route_short_name'] += ',' + feature['properties']['route_short_name']
                break
        else:
            for f2 in new_new_features:
                if feature['geometry']['coordinates'] == f2['geometry']['coordinates']:
                    #f2['properties']['offset'] += (feature['properties']['count'] / 1000) + 1
                    c = feature['properties']['count']
                    offset = 0
                    if c>=10: offset = 0.5
                    if c>=250: offset = 1
                    if c>=500: offset = 2
                    if c>=1000: offset = 3
                    if c>=2000: offset = 4
                    if c>=4000: offset = 5
                    f2['properties']['offset'] += offset

            else:
                new_agency_features[agency_id].append(feature)
                new_new_features.append(feature)

data['features'] = new_new_features
json.dump(data, open('collapsed2.json.new', 'w'))

