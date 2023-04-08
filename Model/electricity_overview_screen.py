from Model.base_model import BaseScreenModel
import logging

logger = logging.getLogger()

class ElectricityOverviewScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.electricity_overview_screen.ElectricityOverviewScreen.ElectricityOverviewScreenView` class.
    """

    def get_strom_data(self):
        return self.data_base.read_strom()

    def log(self, log_string):
        logger.info('ElectricityOverviewScreenModel: {}'.format(log_string))

    def delete_item(self, item_data):
        strom_data = self.data_base.read_strom()
        self.log('current data: {}'.format(strom_data))
        self.log('delete row {}'.format(item_data))
        if item_data in strom_data:
            self.log('deleting item!')
            strom_data.remove(item_data)
        else:
            self.log('item not found!')
        
        self.data_base.write_strom(strom_data)
            
        self.notify_observers('electricity overview screen')
        

        

        
        
