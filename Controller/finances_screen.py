
from View.FinancesScreen.finances_screen import FinancesScreenView


class FinancesScreenController:
    """
    The `FinancesScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.finances_screen.FinancesScreenModel
        self.view = FinancesScreenView(controller=self, model=self.model)

    def get_view(self) -> FinancesScreenView:
        return self.view
