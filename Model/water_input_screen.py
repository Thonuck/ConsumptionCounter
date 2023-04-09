from Model.base_model import BaseScreenModel


class WaterInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.WaterInputScreen.water_input_screen.WaterInputScreenView` class.
    """

    def add(self, new_data):
        with self.data_base.water() as water:
            water.append(new_data)

        self.notify_observers('water overview screen')

