from kivymd.uix.list import BaseListItem, IRightBodyTouch, OneLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.list import BaseListItem
from kivy.properties import BooleanProperty
from kivymd.uix.selectioncontrol import MDSwitch


class BaseListItemWithSwitch(BaseListItem):
    """base class for one line and two line items in the settings list"""
    active = BooleanProperty(False)



class RightSwitchContainer(IRightBodyTouch, MDSwitch):
    """The class implements a container for placing the switch on the right
    side of the settings screen
    """


class OneLineListItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a one line item of the settings list"""


class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a two line item of the settings list"""
