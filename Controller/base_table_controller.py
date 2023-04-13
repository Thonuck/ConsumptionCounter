import datetime
import logging
from abc import abstractmethod

logger = logging.getLogger()


class BaseTableController():
    def __init__(self, model):
        self.pre_data = None
        self.model = model

    def log_info(self, log_line):
        logger.info('{}:{}'.format(self.__class__.__name__, log_line))

    def delete_item(self, row_data):
        self.log_info('Deleting row with data {}'.format(row_data))
        self.model.delete_item(row_data)

    def on_enter_data(self):
        self.log_info('Enter Data ')
        data = self.get_current_data()
        self.log_info('Data to add: {}'.format(data))
        self.model.add(data)

    @abstractmethod
    def get_current_data(self):
        pass

    def on_pre_update_data(self):
        self.pre_data = self.get_current_data()

    def on_update_data(self):
        self.log_info("on_update_data not yet implemented!!!")
        self.model.update(self.pre_data, self.get_current_data())
        self.pre_data = None

    def get_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def get_last(self, element):
        last_element = self.model.get_last_element()
        
        if last_element:
            return last_element[element]
        else:
            return '0'
