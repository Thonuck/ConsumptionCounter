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
        self.back_screen = 'main screen'
        super().__init__(**kwargs)

        self.new_item_screen = 'sport activity input screen'
        column_data = [("Datum", dp(20)),
                       ("Aktivität", dp(18))]

        row_data = []

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar(title="Sport Activity Overview"))
        layout.add_widget(self.create_data_table(column_data=column_data,
                                                 row_data=row_data))
        layout.add_widget(self.create_button_frame())

        self.add_widget(layout)
