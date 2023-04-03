from kivymd.uix.boxlayout import MDBoxLayout

from View.base_app_screen import BaseAppScreenView


class SportActivityInputScreenView(BaseAppScreenView):
    back_screen = 'sport activity screen'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        layout.add_widget(self.create_top_bar(title="Sport Activity Overview"))

        layout.add_widget(self.create_button_frame())

        self.add_widget(layout)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
