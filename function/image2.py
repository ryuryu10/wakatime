import math
from datetime import time, date, timedelta
import datetime

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
