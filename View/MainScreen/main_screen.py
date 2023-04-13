from View.base_screen import BaseScreenView


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
    def on_strom_pressed(self):
        self.manager_screens.current = "electricity overview screen"

    def on_sport_pressed(self):
        self.manager_screens.current = "sport activity screen"

    def on_water_pressed(self):
        self.manager_screens.current = "water overview screen"

    def on_warmth_pressed(self):
        self.manager_screens.current = "warmth overview screen"

    def on_finances_pressed(self):
        self.manager_screens.current = "finance overview screen"

    def on_settings_pressed(self):
        self.manager_screens.current = "settings screen"
