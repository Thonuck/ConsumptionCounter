
import datetime

from Controller.base_table_controller import BaseTableController
from View.ElectricityInputScreen.electricity_input_screen import ElectricityInputScreenView
import logging

logger = logging.getLogger()


class ElectricityInputScreenController(BaseTableController):
    """
    The `ElectricityInputScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        super().__init__(model)
        self.view = ElectricityInputScreenView(controller=self, model=self.model)

    def get_view(self) -> ElectricityInputScreenView:
        return self.view
    
    def get_current_data(self):
        return self.view.get_data()

