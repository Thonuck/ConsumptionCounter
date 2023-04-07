from Model import database
from Model.base_model import BaseScreenModel


class SportActivityInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SportActivityInputScreen.sport_activity_input_screen.SportActivityInputScreenView` class.
    """

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.SportActivityInputScreen.sport_activity_input_screen.SportActivityInputScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("sport activity input screen")

    def add(self, new_data):
        data = database.db_read_sport_activities()
        data.append(new_data)
        database.db_write_sport_activity(data)
        self.notify_observers('sport activity screen')