import json
import os
from contextlib import contextmanager


class DataBase():
    
    def __init__(self, user_data_dir):
        self.user_data_dir = user_data_dir

        self.db_path = os.path.join(self.user_data_dir, 'consumption_counter')

        if not os.path.exists(self.db_path):
            os.mkdir(self.db_path)
        
        self.db_filename = os.path.join(self.db_path, 'counter_data.json')


    def read(self):
        if os.path.exists(self.db_filename):
            try:
                with open(self.db_filename, "r") as json_read:
                    data = json.load(json_read)
            except:
                os.remove(self.db_filename)
                data = {}
        else:
            data = {}
        return data


    def write(self, data):
        if data is None:
            return
            
        with open(self.db_filename, "w") as json_write:
            json.dump(data, json_write)
    
    def read_strom(self):
        data = self.read()
        if 'strom' in data:
            return data['strom']

        return []

    def write_strom(self, current_strom_data):
        data = self.read()
        data['strom'] = current_strom_data
        self.write(data)

    @contextmanager
    def strom(self):
        data = self.read_strom()
        yield data
        self.write_strom(data)

    def read_sport_activities(self):
        data = self.read()
        if 'sport_activity' in data:
            return data['sport_activity']

        return []

    def write_sport_activity(self, current_sport_activity):
        data = self.read()
        data['sport_activity'] = current_sport_activity
        self.write(data)

    @contextmanager
    def sport_activities(self):
        data = self.read_sport_activities()
        yield data
        self.write_sport_activity(data)

    def read_water(self):
        data = self.read()
        if 'water_data' in data:
            return data['water_data']

        return []

    def write_water(self, current_sport_activity):
        data = self.read()
        data['water_data'] = current_sport_activity
        self.write(data)

    @contextmanager
    def water(self):
        data = self.read_water()
        yield data
        self.write_water(data)

    def read_warmth(self):
        data = self.read()
        if 'warmth_data' in data:
            return data['warmth_data']

        return []

    def write_warmth(self, current_sport_activity):
        data = self.read()
        data['warmth_data'] = current_sport_activity
        self.write(data)

    @contextmanager
    def warmth(self):
        data = self.read_warmth()
        yield data
        self.write_warmth(data)

    def read_settings_value(self, key):
        data = self.read()
        if 'settings' in data:
            if key in data['settings']:
                return data['settings'][key]

    def write_settings_value(self, key, value):
        data = self.read()
        if 'settings' in data:
            data['settings'][key] = value
        else:
            data['settings'] = {key: value}
        self.write(data)

            

        
        

