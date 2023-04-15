from Model.base_model import BaseScreenModel



class SettingsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SettingsScreen.settings_screen.SettingsScreenView` class.
    """

    @property
    def notification_time(self):
        return self.data_base.read_settings_value('notification_time')

    @notification_time.setter
    def notification_time(self, notification_time):
        self.data_base.write_settings_value('notification_time', notification_time)
