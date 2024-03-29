from View.base_app_screen import BaseAppScreenView
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast

class BaseInputScreen(BaseAppScreenView):
    def __init__(self,
                 input_title,
                 overview_screen,
                 **kwargs):
        super().__init__(**kwargs)

        self.overview_screen = overview_screen

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar(title=input_title))

        layout.add_widget(self.add_input_widgets())

        layout.add_widget(self.create_button_frame(add=True))

        self.add_widget(layout)


    def add_input_widgets(self):
        anchor_layout = AnchorLayout(anchor_y='top')

        item_layout = MDBoxLayout(spacing= 5,
                                  padding=20,
                                  size_hint_x=0.9,
                                  size_hint_y=0.5,
                                  orientation='vertical')
        

        for element_name in self.elements:
            self.elements[element_name]['widget'] = MDTextField(hint_text=self.elements[element_name]['text'],
                                                                # id=self.elements[element_name]['id'],
                                                                font_size='24sp')
            item_layout.add_widget(self.elements[element_name]['widget'])
           
        anchor_layout.add_widget(item_layout)

        return anchor_layout


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

        self.manager_screens.current = self.back_screen 


    def on_pre_enter(self, *args):
        """Event called by screenmanager
        fill elements depending on reason"""

        self.log_info('On pre enter status {}'.format(self.status))

        if self.status == 'edit':
            self.controller.on_pre_update_data()
        else:
            self.pre_fill_elements()
