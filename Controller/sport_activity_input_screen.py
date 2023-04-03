
from View.SportActivityInputScreen.sport_activity_input_screen import SportActivityInputScreenView


class SportActivityInputScreenController():
    """
    The `SportActivityInputScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.sport_activity_input_screen.SportActivityInputScreenModel
        self.view = SportActivityInputScreenView(controller=self, model=self.model)

    def get_view(self) -> SportActivityInputScreenView:
        return self.view
