from Model.base_model import BaseScreenModel


class SportActivityInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SportActivityInputScreen.sport_activity_input_screen.SportActivityInputScreenView` class.
    """


    def add(self, new_data):
        data = self.data_base.read_sport_activities()
        data.append(new_data)
        self.data_base.write_sport_activity(data)
        self.notify_observers('sport activity screen')
