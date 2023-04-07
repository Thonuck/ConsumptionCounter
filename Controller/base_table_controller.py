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

    def delete_row_data(self, row_data):
        self.log_info('Deleting row with data {}'.format(row_data))
        # self.model.delete_row(row_data)

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
