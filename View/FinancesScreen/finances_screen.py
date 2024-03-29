from View.base_screen import BaseScreenView


class FinancesScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def on_cancel_pressed(self):
        self.manager_screens.current = "main screen"

    def on_settings_pressed(self):
        pass
