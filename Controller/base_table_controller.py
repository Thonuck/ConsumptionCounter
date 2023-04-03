import logging

logger = logging.getLogger()


class BaseTableController():
    def log_info(self, log_line):
        logger.info('{}:{}'.format(self.__class__.__name__, log_line))

    def delete_row_data(self, row_data):
        self.log_info('Deleting row with data {}'.format(row_data))
        # self.model.delete_row(row_data)

