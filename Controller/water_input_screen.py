
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
        return {'datum': self.view.datum_text_field.text,
                'time': self.view.time_text_field.text,
                'stand': self.view.stand_text_field.text}

    def add(self, new_data):
        pass
        # self.log_info("Add new data {}".format(new_data))
        # data = database.db_read_sport_activities()
        # data.append(new_data)
        # database.db_write_sport_activity(data)
        # self.notify_observers('sport activity screen')