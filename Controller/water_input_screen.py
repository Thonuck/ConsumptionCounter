
from Controller.base_table_controller import BaseTableController
from View.WaterInputScreen.water_input_screen import WaterInputScreenView


class WaterInputScreenController(BaseTableController):
    """
    The `WaterInputScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.water_input_screen.WaterInputScreenModel
        self.view = WaterInputScreenView(controller=self, model=self.model)

    def get_view(self) -> WaterInputScreenView:
        return self.view

    def get_current_data(self):
        return self.view.get_data()
