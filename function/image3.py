from ast import Pass
import json
import pickle

def maker(days, seconds):

    for number in range(0, len(days)):
        f = open(f'Export\Database\Archive\{days[int(number)]}.data', "w")
        f.write(str(seconds[int(number)]))
        f.close()

    with open('Export\Database\days.pkl', 'wb') as f:
        pickle.dump(days,f)
    with open('Export\Database\seconds.pkl', 'wb') as f:
        pickle.dump(seconds, f)