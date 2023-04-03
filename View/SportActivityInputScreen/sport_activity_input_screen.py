from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from View.base_app_screen import BaseAppScreenView


class SportActivityInputScreenView(BaseAppScreenView):
    back_screen = 'sport activity screen'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar(title="Sport Activity Overview"))

        layout.add_widget(self.add_input_widgets())

        layout.add_widget(self.create_button_frame(add=True))

        self.add_widget(layout)

    def add_input_widgets(self):
        anchor_layout = AnchorLayout(anchor_y='center')

        item_layout = MDBoxLayout(spacing= 5,
                                  padding=20,
                                  size_hint_x=0.9,
                                  size_hint_y=0.5,
                                  orientation='vertical')

        datum_text_field = MDTextField(id='sport_activity_datum',
                                       hint_text='Datum',
                                       font_size='24sp')
        item_layout.add_widget(datum_text_field)

        activity_text_field = MDTextField(id='sport_activity_type',
                                       hint_text='Activity',
                                       font_size='24sp')
        item_layout.add_widget(activity_text_field)

        anchor_layout.add_widget(item_layout)

        return anchor_layout

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_add_button_pressed(self, widget=None):
        self.log_warning("Ok, let's continue here...")