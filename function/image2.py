from encodings import utf_8
import math
import datetime
import json

from datetime import time, date, timedelta
from collections import OrderedDict
from turtle import down

def maker(seconds_data, date):

    sidebar_seocnds = [0,max(seconds_data)/3,(max(seconds_data)/3)*2,(max(seconds_data)/3)*3]
    sidebar = []
    graphs = []
    down_bar = []

    for c in sidebar_seocnds:
        temp = datetime.timedelta(seconds=int(c))
        sidebar.append(f'{temp}')

    for b in date:
        temp = f'{b}'
        down_bar.append(temp[-5:])

    for a in seconds_data:
        temp = 600 * a
        print(temp/ max(seconds_data))
        graphs.append(math.trunc(temp / max(seconds_data)))
    
    json_dump = OrderedDict()
    json_dump['DUMP_version'] == "1"
    json_dump['DATAS'] = {
        'sidebar' : sidebar,
        'graphs' : graphs,
        'down_bar' : down_bar
    }
    with open('Export\dump.json','w', encoding="utf-8") as make_file:
        json.dump(json_dump, make_file, ensure_ascii=False, indent='\t')
