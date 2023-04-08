import json
import os


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

    def read_sport_activities(self):
        data = self.read()
        if 'sport_activity' in data:
            return data['sport_activity']

        return []

    def write_sport_activity(self, current_sport_activity):
        data = self.read()
        data['sport_activity'] = current_sport_activity
        self.write(data)
