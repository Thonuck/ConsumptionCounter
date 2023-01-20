from Model.base_model import BaseScreenModel
from Model import database
import logging

logger = logging.getLogger()


class ElectricityInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.electricity_input_screen.ElectricityInputScreen.ElectricityInputScreenView` class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def add(self, new_data):
        logger.info('ElectricityInputScreenModel: {}'.format(new_data))
        data = database.db_read_strom()
        data.append(new_data)
        database.db_write_strom(data)
        self.notify_observers('electricity overview screen')
        
    def update(self, old_item, new_data):
        data = database.db_read_strom()
        try:
            old_index = data.index(old_item)
        except ValueError:
            logger.error("ElectricityInputScreenModel: data not found in database: {}".format(old_item))
        data[old_index] = new_data
        database.db_write_strom(data)
        self.notify_observers('electricity overview screen')
