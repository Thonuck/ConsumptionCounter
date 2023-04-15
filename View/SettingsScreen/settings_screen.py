from View.base_screen import BaseScreenView
from View.SettingsScreen.components import OneLineListItemWithSwitch, TwoLineListItemWithSwitch, Header, TwoLineListItemWithLabel, TwoLineListItemWithButton
from kivy.properties import StringProperty, ObjectProperty
import logging

logger = logging.getLogger()

class SettingsScreenView(BaseScreenView):
    noty_time = StringProperty("11:11")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.noty_time = self.controller.get_notification_time()

    def on_pre_enter(self):
        self.noty_time = self.controller.get_notification_time()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_noty_time(self, instance, current_time):
        logger.info("on_notification_time: {}".format(current_time))
        self.controller.set_notification_time(current_time)
    
    def set_current_time(self, time):
        logger.info("set_current_time: {}".format(time))
        self.controller.set_notification_time(time)



    
