from View.base_screen import BaseScreenView
import logging


logger = logging.getLogger()


class BaseAppScreenView(BaseScreenView):

    def log_info(self, log_line):
        logger.info('{}:{}'.format(self.__class__.__name__, log_line))
