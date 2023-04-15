from Model.base_model import BaseScreenModel



class SettingsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SettingsScreen.settings_screen.SettingsScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

    def write_notification_time(self, notification_time):
        pass
