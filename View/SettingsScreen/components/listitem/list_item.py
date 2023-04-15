from kivymd.uix.list import BaseListItem, IRightBodyTouch, OneLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.list import BaseListItem
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker
from datetime import datetime
import logging


logger = logging.getLogger()


class BaseListItemWithSwitch(BaseListItem):
    """base class for one line and two line items in the settings list"""
    active = BooleanProperty(False)

class BaseListItemWithLabel(BaseListItem):
    text = StringProperty("00:00")

class BaseListItemWithButton(BaseListItem):
    current_time = StringProperty("00:00")

class RightSwitchContainer(IRightBodyTouch, MDSwitch):
    """The class implements a container for placing the switch on the right
    side of the settings screen
    """

class RightLabelContainer(IRightBodyTouch, MDLabel):
    """ This class implements a container for placing a label to the right
    side of the settings screen """


class TimePicker(MDTimePicker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_clock = '24'

class RightButtonContainer(IRightBodyTouch, MDFlatButton):
    """ This class implements a container for placing a label to the right
    side of the settings screen """

    def show_time_picker(self, *args):
        '''Open time picker dialog.'''
        time_dialog = TimePicker()
        current_time = datetime.strptime(self.text, '%H:%M').time()
        time_dialog.set_time(current_time)
        time_dialog.bind(time=self.get_time, on_cancel=self.on_cancel, on_save=self.on_save)
        time_dialog.open()
    
    def get_time(self, instance, time):
        print("get_time. Time is {}".format(time))
        return time

    def on_cancel(self, instance, time):
        print("On Cancel. Time is {}".format(time))

    def on_save(self, instance, time):
        self.text = time.strftime("%H:%M")
        print("On Save. Time is {} - {} - {}".format(time, type(time), time.strftime("%H:%M")))
    
    def on_button_pressed(self):
        self.show_time_picker()


class OneLineListItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a one line item of the settings list"""


class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a two line item of the settings list"""
    notification_enabled = BooleanProperty()


class TwoLineListItemWithLabel(TwoLineRightIconListItem, BaseListItemWithLabel):
    """The class implements a two line item of the settings list with label"""


class TwoLineListItemWithButton(TwoLineRightIconListItem, BaseListItemWithButton):
    """The class implements a two line item of the settings list with label"""
    current_time = StringProperty()
    def set_time(self, time):
        logger.info("setting time...")
        self.current_time = time

