from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.toolbar import MDTopAppBar

from View.base_screen import BaseScreenView
import logging

logger = logging.getLogger()


class BaseTableScreen(BaseScreenView):
    new_item_screen = ''

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.controller.update_table_from_database()

    def log_info(self, log_line):
        logger.info('{}:{}'.format(self.__class__.__name__, log_line))

    def create_top_bar(self, title):
        """Creates the window top bar
        :param title: The string to display as title"""
        return MDTopAppBar(
            title=title,
            right_action_items=[['dots-vertical', lambda x: self.on_settings_pressed()]])

    def on_settings_pressed(self):
        """Called function, if the dots in the title bar are pressed"""
        self.log_info('on_settings_pressed is not yet implemented')

    def create_data_table(self, column_data, row_data):
        """Creates the data table
        :param column_data: The column names given as tupes with width
        :param row_data: The data to insert into the table initially"""
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.9),
            check=False,  # draw checkbox for each row
            column_data=column_data,
            row_data=row_data
        )

        table.bind(on_check_press=self.on_press_checkbox)
        table.bind(on_row_press=self.on_select_row)
        return table

    def create_button_frame(self):
        """Creates the button frame on the lower edge of the screen.
        Two buttons are filled: go back to main screen and one button to
        insert new data."""
        btn_frame = MDBoxLayout(orientation="horizontal",
                                spacing=5,
                                padding=5,
                                size_hint=(0.9, 0.1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                )

        btn_frame.add_widget(self.create_back_button())
        btn_frame.add_widget(self.create_insert_button())
        return btn_frame

    def create_insert_button(self):
        """Create the insert button - to insert new data to the table"""
        return MDRaisedButton(text="Eingabe",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_insert_button_pressed)

    def on_insert_button_pressed(self, widget=None):
        """Call back for inserting new data to the table,
        The corresponding new_item_screen must be set to use this"""
        entry_screen = self.manager_screens.get_screen(self.new_item_screen)
        entry_screen.status = 'new'
        self.manager_screens.current = self.new_item_screen

    def create_back_button(self):
        """Creates the back button to return to the main screen"""
        return MDRaisedButton(text="Zurueck",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_back_button_pressed)

    def on_back_button_pressed(self, widget=None):
        """Function to return to the main screen"""
        self.manager_screens.current = "main screen"

    def on_press_checkbox(self):
        """Called by table """
        pass

    def on_select_row(self):
        """Called by table """
        pass
