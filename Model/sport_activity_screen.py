from Model import database
from Model.base_model import BaseScreenModel

class SportActivityScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SportActivityScreen.sport_activity_screen.SportActivityScreenView` class.
    """

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.SportActivityScreen.sport_activity_screen.SportActivityScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("sport activity screen")

    def get_sport_activity_data(self):
        return database.db_read_sport_activities()

