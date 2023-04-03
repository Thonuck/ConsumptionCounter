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


class SportActivityScreenView(BaseScreenView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar())
        layout.add_widget(self.create_data_table())
        layout.add_widget(self.create_button_frame())

        self.add_widget(layout)

    def create_top_bar(self):
        return MDTopAppBar(
            title="Sport Activities Overviews",
            right_action_items=[['dots-vertical', lambda x: self.on_settings_pressed()]])

    def create_data_table(self):
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.9),
            check=False,  # draw checkbox for each row
            column_data=[("Datum", dp(20)),
                         ("Aktivität", dp(18))],
            row_data=[("15.12.2022", "Taekwondo"),
                      ("13.12.2022", "Laufen"),
                      ("10.12.2022", "Gymnastik")]

        )
        table.bind(on_check_press=self.on_press_checkbox)
        table.bind(on_row_press=self.on_select_row)
        return table


    def create_button_frame(self):
        btn_frame = MDBoxLayout(orientation="horizontal",
                                spacing=5,
                                padding=5,
                                size_hint=(0.9, 0.1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                )

        btn_frame.add_widget(self.create_back_button())
        btn_frame.add_widget(self.create_input_button())
        return btn_frame

    def create_input_button(self):
        return MDRaisedButton(text="Eingabe",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_entry_button)

    def create_back_button(self):
        return MDRaisedButton(text="Zurueck",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_back_button)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_back_button(self):
        self.manager_screens.current = "main screen"

    def on_settings_pressed(self):
        pass

    def on_press_checkbox(self):
        pass

    def on_select_row(self):
        pass

    def on_entry_button(self):
        pass
