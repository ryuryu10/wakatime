import math

def maker(seconds_data, date):
    
    sidebar = [0,max(seconds_data)/3,(max(seconds_data)/3)*2,(max(seconds_data)/3)*3]
    graphs = []
    down_bar = []

    for b in date:
        down_bar.append(b[-5:])
    for a in seconds_data:
        temp = 600 * a
        print(temp/ max(seconds_data))
        graphs.append(math.trunc(temp / max(seconds_data)))
    pass