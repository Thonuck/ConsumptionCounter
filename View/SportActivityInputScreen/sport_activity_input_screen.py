from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast

from View.base_app_screen import BaseAppScreenView


class SportActivityInputScreenView(BaseAppScreenView):
    back_screen = 'sport activity screen'
    status = 'new'


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

        self.datum_text_field = MDTextField(id='sport_activity_datum',
                                       hint_text='Datum',
                                       font_size='24sp')
        item_layout.add_widget(self.datum_text_field)

        self.activity_text_field = MDTextField(id='sport_activity_type',
                                       hint_text='Activity',
                                       font_size='24sp')
        item_layout.add_widget(self.activity_text_field)

        anchor_layout.add_widget(item_layout)

        return anchor_layout

    def get_data(self):
        return {'datum': self.datum_text_field.text, 'activity': self.activity_text_field.text}

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurrdated in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_add_button_pressed(self, widget=None):

        could_be_added = True
        data = self.get_data()
        all_filled = all([x for x in data.values()])
        if not all_filled:
            toast("Not able to add data")
            return

        if self.status == 'new':
            self.controller.on_enter_data()
        else:
            self.controller.on_update_data()

        self.manager_screens.current = 'sport activity screen'

    def on_pre_enter(self, *args):
        """Event called by screenmanager
        fill elements depending on reason"""

        self.log_info('On pre enter status {}'.format(self.status))

        if self.status == 'edit':
            self.controller.on_pre_update_data()
        else:
            self.datum_text_field.text = self.controller.get_date()
            pass
