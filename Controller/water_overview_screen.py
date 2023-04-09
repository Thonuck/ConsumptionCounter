from Controller.base_table_controller import BaseTableController
from View.WaterOverviewScreen.water_overview_screen import WaterOverviewScreenView


class WaterOverviewScreenController(BaseTableController):
    """
    The `WaterOverviewScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.water_overview_screen.WaterOverviewScreenModel
        self.view = WaterOverviewScreenView(controller=self, model=self.model)
        self.update_table_from_database()

    def get_view(self) -> WaterOverviewScreenView:
        return self.view

    def update_table_from_database(self):
        sport_activity_data = self.model.get()

        item_list = []
        for entry in sport_activity_data:
            item_data = (entry['datum'], entry['time'], entry['stand'])
            item_list.append(item_data)

        self.view.table.row_data = item_list
        self.view.table.table_data.refresh_from_data()
