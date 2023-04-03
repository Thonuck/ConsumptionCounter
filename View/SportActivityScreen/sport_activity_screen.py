"""
This module contains the sport activity screen.
It shall give an overview of the latest activities done, sorted in reverse order,
so the user sees the latest done activity on top.
"""
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.toolbar import MDTopAppBar

from View.base_screen import BaseScreenView
from View.base_table_screen import BaseTableScreen


class SportActivityScreenView(BaseTableScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        column_data = [("Datum", dp(20)),
                       ("Aktivität", dp(18))]

        row_data = [("15.12.2022", "Taekwondo"),
                    ("13.12.2022", "Laufen"),
                    ("10.12.2022", "Gymnastik")]

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar(title="Sport Activity Overview"))
        layout.add_widget(self.create_data_table(column_data=column_data,
                                                 row_data=row_data))
        layout.add_widget(self.create_button_frame())

        self.add_widget(layout)
