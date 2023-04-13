
from Controller.base_table_controller import BaseTableController
from View.WarmthInputScreen.warmth_input_screen import WarmthInputScreenView


class WarmthInputScreenController(BaseTableController):
    """
    The `WarmthInputScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.warmth_input_screen.WarmthInputScreenModel
        self.view = WarmthInputScreenView(controller=self, model=self.model)

    def get_view(self) -> WarmthInputScreenView:
        return self.view

    def get_current_data(self):
        return self.view.get_data()
