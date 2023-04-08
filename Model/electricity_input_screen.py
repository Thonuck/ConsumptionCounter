from Model.base_model import BaseScreenModel
import logging

logger = logging.getLogger()


class ElectricityInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.electricity_input_screen.ElectricityInputScreen.ElectricityInputScreenView` class.
    """
    
    def add(self, new_data):
        logger.info('ElectricityInputScreenModel: {}'.format(new_data))
        data = self.data_base.read_strom()
        data.append(new_data)
        self.data_base.write_strom(data)
        self.notify_observers('electricity overview screen')
        
    def update(self, old_item, new_data):
        data = self.data_base.read_strom()
        try:
            old_index = data.index(old_item)
        except ValueError:
            logger.error("ElectricityInputScreenModel: data not found in database: {}".format(old_item))
        data[old_index] = new_data
        self.data_base.write_strom(data)
        self.notify_observers('electricity overview screen')

    def get_last_stand(self):
        data = self.data_base.read_strom()
        if data:
            try:
                return data[-1]['stand']
            except KeyError:
                return ''
            except IndexError:
                return ''

        return ''
        
