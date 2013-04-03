import json
from copy import deepcopy
from collections import defaultdict
a = json.load(open('agencies_by_time.json'))
g = deepcopy(a)

for day, b in a.items():
    for time, agencies in b.items():
        group_count  = defaultdict(int)
        for agency in agencies.values():
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
        #print group_count
        g[day][time] = group_count

chartdata = {}
for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
    chartdata[day] =  []
    chartdata[day] .append (['Time', 'First', 'Stagecoach', 'Other', 'Arriva'])
    for time in [ str(i).zfill(2)+':00:00' for i in range(0,24) ]:
        row = [ time ]
        for group in ['F', 'S', 'O', 'A']:
            row.append(g[day][time][group])
        chartdata[day].append(row)
json.dump(chartdata, open('chartdata.json', 'w'))
