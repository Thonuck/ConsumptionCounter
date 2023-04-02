
from View.SportActivityScreen.sport_activity_screen import SportActivityScreenView


class SportActivityScreenController:
    """
    The `SportActivityScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.sport_activity_screen.SportActivityScreenModel
        self.view = SportActivityScreenView(controller=self, model=self.model)

    def get_view(self) -> SportActivityScreenView:
        return self.view
