import datetime

from Controller.base_table_controller import BaseTableController
from View.SportActivityInputScreen.sport_activity_input_screen import SportActivityInputScreenView
from Model import database


class SportActivityInputScreenController(BaseTableController):
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

    def get_current_data(self):
        return {'datum': self.view.datum_text_field.text,
                'activity': self.view.activity_text_field.text}

    def add(self, new_data):
        self.log_info("Add new data {}".format(new_data))
        data = database.db_read_sport_activities()
        data.append(new_data)
        database.db_write_sport_activity(data)
        self.notify_observers('sport activity screen')
