from Controller.base_table_controller import BaseTableController
from View.ElectricityOverviewScreen.electricity_overview_screen import ElectricityOverviewScreenView
import logging

logger = logging.getLogger()


class ElectricityOverviewScreenController(BaseTableController):
    """
    The `ElectricityOverviewScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.electricity_overview_screen.ElectricityOverviewScreenModel
        self.view = ElectricityOverviewScreenView(controller=self, model=self.model)
        self.update_table_from_database()

    def get_view(self) -> ElectricityOverviewScreenView:
        return self.view

    def update_table_from_database(self):
        electricity_data = self.model.get()
        self.log_info("Electricity Data: {}".format(electricity_data))

        item_list = []
        for entry in electricity_data:
            item_data = (entry['datum'], entry['time'], entry['stand'])
            item_list.append(item_data)

        self.view.table.row_data = item_list
        self.view.table.table_data.refresh_from_data()
