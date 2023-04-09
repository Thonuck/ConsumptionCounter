"""
This module contains the sport activity screen.
It shall give an overview of the latest activities done, sorted in reverse order,
so the user sees the latest done activity on top.
"""
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from View.base_table_screen import BaseTableScreen


class SportActivityScreenView(BaseTableScreen):
    
    def __init__(self, **kwargs):
        column_data = [("Datum", dp(20)),
                       ("Aktivität", dp(40))]

        super().__init__(title='Sport Activity Overview',
                         new_item_screen='sport activity input screen',
                         back_screen='main screen',
                         column_data=column_data,
                         row_data=[],
                         columns=['datum', 'activity'],
                         **kwargs)    

