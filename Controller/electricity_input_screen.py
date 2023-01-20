
import datetime
from View.ElectricityInputScreen.electricity_input_screen import ElectricityInputScreenView
import logging

logger = logging.getLogger()


class ElectricityInputScreenController:
    """
    The `ElectricityInputScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.electricity_input_screen.ElectricityInputScreenModel
        self.view = ElectricityInputScreenView(controller=self, model=self.model)

    def get_view(self) -> ElectricityInputScreenView:
        return self.view
    
    def log_info(self, log_line):
        logger.info("ElectricityInputScreenController: {}".format(log_line))


    def get_current_data(self):
        return {'stand': self.view.stand_data.text,
                'datum': self.view.date_data.text,
                'zeit': self.view.time_data.text}

    def on_enter_data(self):
        self.log_info("Enter Data...")
        data = self.get_current_data()
        self.model.add(data)

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
    
