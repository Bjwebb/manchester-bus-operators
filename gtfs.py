import csv, json
from collections import defaultdict

def csv_to_dict(f, key_field):
    dictreader = csv.DictReader(f)
    out = {}
    for row in dictreader:
        out[row[key_field].strip()] = row
    return out


if True:
    agencies = csv_to_dict(open('gtdf-out/agency.txt'), 'agency_id') 
    routes = csv_to_dict(open('gtdf-out/routes.txt'), 'route_id') 
    services = csv_to_dict(open('gtdf-out/calendar.txt'), 'service_id') 
    #trips = csv.DictReader(open('gtdf-out/trips.txt'))
    trips = csv.DictReader(open('gtdf-out/trips__join_headered.txt'))

    for v in agencies.values():
        v['count'] = 0
    for v in routes.values():
        v['count'] = 0

    date = '20130323'
    for trip in trips:
        #print times_by_trip[trip['trip_id']]
        route = routes[trip['route_id']]
        agency = agencies[route['agency_id']]
        service = services[trip['service_id']]
        if service['start_date'] < date and service['end_date'] > date: 
            c = int(service['monday']) + int(service['tuesday']) + int(service['wednesday']) + int(service['thursday']) + int(service['friday']) + int(service['saturday']) + int(service['sunday'])
            agency['count'] += c
            route['count'] += c
            pass

group_count  = defaultdict(int)
if __name__ == '__main__':
    json.dump(agencies, open('agencies.json', 'w'))
    for agency in agencies.values():
        print agency['count'], '\t', agency['agency_id'], '\t', agency['agency_name']
        if agency['agency_id'] in ['GMS', 'RMS', 'SWI']:
            group = 'S'
        elif agency['agency_id'] in ['CAL', 'FPR', 'GMN']:
            group = 'F'
        elif agency['agency_id'] in ['NOR', 'MTL']:
            group = 'A'
        elif agency['agency_id'] == 'MET':
            continue
        else:
            group = 'O'
        group_count[group] += agency['count']
print group_count


print routes

