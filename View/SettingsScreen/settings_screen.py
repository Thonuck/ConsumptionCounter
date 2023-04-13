from View.base_screen import BaseScreenView
from View.SettingsScreen.components import OneLineListItemWithSwitch, TwoLineListItemWithSwitch, Header, TwoLineListItemWithLabel


class SettingsScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
