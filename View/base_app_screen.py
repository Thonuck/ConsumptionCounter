from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar

from View.base_screen import BaseScreenView
import logging


logger = logging.getLogger()


class BaseAppScreenView(BaseScreenView):
    back_screen = ''

    def log_info(self, log_line):
        logger.info('{}:{}'.format(self.__class__.__name__, log_line))

    def log_warning(self, log_line):
        logger.warning('{}:{}'.format(self.__class__.__name__, log_line))

    def create_top_bar(self, title):
        """Creates the window top bar
        :param title: The string to display as title"""
        return MDTopAppBar(
            title=title,
            right_action_items=[['dots-vertical', lambda x: self.on_settings_pressed()]])

    def create_back_button(self):
        """Creates the back button to return to the main screen"""
        return MDRaisedButton(text="Zurueck",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_back_button_pressed)

    def create_button_frame(self, back=True, insert=True, add=False):
        """Creates the button frame on the lower edge of the screen.
        Two buttons are filled: go back to main screen and one button to
        insert new data."""
        btn_frame = MDBoxLayout(orientation="horizontal",
                                spacing=5,
                                padding=5,
                                size_hint=(0.9, 0.1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                )

        if back:
            btn_frame.add_widget(self.create_back_button())
        if insert:
            if not hasattr(self, 'new_item_screen'):
                logger.warning("No new_item_screen defined!")
            else:
                btn_frame.add_widget(self.create_insert_button())
        if add:
            btn_frame.add_widget(self.create_add_button())
        return btn_frame

    def on_back_button_pressed(self, widget=None):
        """Function to return to the main screen"""
        if not hasattr(self, 'back_screen') and not self.back_screen:
            self.log_warning('on_back_button_pressed: No back_screen defined!')
        self.manager_screens.current = self.back_screen

    def create_add_button(self, widget=None):
        return MDRaisedButton(text="Hinzufuegen",
                              size_hint=(1, None),
                              font_size='24sp',
                              on_release=self.on_add_button_pressed)

    def on_add_button_pressed(self, widget=None):
        self.log_warning('on_enter_data_pressed: not implemented yet!')