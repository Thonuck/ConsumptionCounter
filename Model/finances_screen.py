from Model.base_model import BaseScreenModel


class FinancesScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.FinancesScreen.finances_screen.FinancesScreenView` class.
    """

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.FinancesScreen.finances_screen.FinancesScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("finances screen")
