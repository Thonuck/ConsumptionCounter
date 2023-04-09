from Model.base_model import BaseScreenModel


class WaterOverviewScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.WaterOverviewScreen.water_overview_screen.WaterOverviewScreenView` class.
    """

    def get(self):
        with self.data_base.water() as water:
            return water

    def delete_item(self, item_data):

        with self.data_base.water() as water:
            if item_data in water:
                water.remove(item_data)

        self.notify_observers('water overview screen')
