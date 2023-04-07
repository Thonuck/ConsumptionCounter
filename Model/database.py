import json
import os

def get_db_filename():
    """
    Construct 
    """
    this_file = os.path.realpath(__file__)
    base_dir = os.path.dirname(this_file)
    return os.path.join(base_dir, 'counter_data.json')

def db_read():
    if os.path.exists(get_db_filename()):
        try:
            with open(get_db_filename(), "r") as json_read:
                data = json.load(json_read)
        except:
            os.remove(get_db_filename())
            data = {}
    else:
        data = {}
    return data


def db_write(data):
    if data is None:
        return
        
    with open(get_db_filename(), "w") as json_write:
        json.dump(data, json_write)

def db_read_strom():
    data = db_read()
    if 'strom' in data:
        return data['strom']

    return []

def db_write_strom(current_strom_data):
    data = db_read()
    data['strom'] = current_strom_data
    db_write(data)


def db_read_sport_activities():
    data = db_read()
    if 'sport_activity' in data:
        return data['sport_activity']

    return []

def db_write_sport_activity(current_sport_activity):
    data = db_read()
    data['sport_activity'] = current_sport_activity
    db_write(data)