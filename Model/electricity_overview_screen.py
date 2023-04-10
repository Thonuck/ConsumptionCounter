from Model.base_model import BaseScreenModel
import logging

logger = logging.getLogger()

class ElectricityOverviewScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.electricity_overview_screen.ElectricityOverviewScreen.ElectricityOverviewScreenView` class.
    """

    def get(self):
        with self.data_base.strom() as strom:
            return strom

    def delete_item(self, item_data):
        with self.data_base.strom() as strom:
            if item_data in strom:
                strom.remove(item_data)
            
        self.notify_observers('electricity overview screen')
        

        

        
        
