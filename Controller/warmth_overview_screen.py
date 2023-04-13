
from Controller.base_table_controller import BaseTableController
from View.WarmthOverviewScreen.warmth_overview_screen import WarmthOverviewScreenView


class WarmthOverviewScreenController(BaseTableController):
    """
    The `WarmthOverviewScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.warmth_overview_screen.WarmthOverviewScreenModel
        self.view = WarmthOverviewScreenView(controller=self, model=self.model)
        self.update_table_from_database()

    def get_view(self) -> WarmthOverviewScreenView:
        return self.view

    def get_current_data(self):
        return self.view.get_data()

    def update_table_from_database(self):
        warmth_data = self.model.get()
        self.log_info('Waerme: {}'.format(warmth_data))

        item_list = []
        for entry in warmth_data:
            item_data = (entry['datum'], entry['time'], entry['stand'])
            item_list.append(item_data)

        self.view.table.row_data = item_list
        self.view.table.table_data.refresh_from_data()
