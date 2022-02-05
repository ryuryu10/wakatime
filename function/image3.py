import json
import pickle
def maker(days, seconds):

    with open('Export/Database/total.json', 'r') as f:
        json_data = json.load(f)

    with open('Export\Database\days.pkl', 'wb') as f:
        pickle.dump(days,f)
    with open('Export\Database\seconds.pkl', 'wb') as f:
        pickle.dump(seconds, f)

    for day in json_data:
        print(day)
