from kivymd.uix.list import BaseListItem, IRightBodyTouch, OneLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.list import BaseListItem
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker

class BaseListItemWithSwitch(BaseListItem):
    """base class for one line and two line items in the settings list"""
    active = BooleanProperty(False)

class BaseListItemWithLabel(BaseListItem):
    text = StringProperty("00:00")

class BaseListItemWithButton(BaseListItem):
    text = StringProperty("00:00")

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
    time_dialog = ObjectProperty()
    
    def show_time_picker(self):
        if not self.time_dialog:
            self.time_dialog = MDDialog(
                title='Select Time',
                type='custom',
                content_cls=TimePicker(),
                buttons=[
                    MDFlatButton(
                        text='CANCEL', on_release=self.dismiss_dialog),
                    MDFlatButton(
                        text='OK', on_release=self.get_time)
                ]
            )
        self.time_dialog.open()

    def dismiss_dialog(self, *args):
        self.time_dialog.dismiss()

    def on_button_pressed(self):
        self.show_time_picker()
    
    def get_time(self, *args):
        time_picker = self.time_dialog.content_cls
        print(f'Time selected: {time_picker.time}')


class OneLineListItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a one line item of the settings list"""


class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a two line item of the settings list"""


class TwoLineListItemWithLabel(TwoLineRightIconListItem, BaseListItemWithLabel):
    """The class implements a two line item of the settings list with label"""


class TwoLineListItemWithButton(TwoLineRightIconListItem, BaseListItemWithButton):
    """The class implements a two line item of the settings list with label"""
