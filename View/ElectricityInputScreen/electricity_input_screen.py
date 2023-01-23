from View.base_screen import BaseScreenView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import logging


logger = logging.getLogger()


class ElectricityInputScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = 'new'
        self.dialog = None

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def log(self, log_line):
        """Logs the given log line to the kivy logger

        :param log_line: The line to log
        """
        logger.info('ElectricityInputScreenView: {}'.format(log_line))

    def on_pre_enter(self):
        """Event called by screenmanager
        """
        self.log("On pre enter status {}".format(self.status))
        
        if self.status == 'edit':
            self.controller.on_pre_update_data()
        else:
            self.stand_data.text = self.model.get_last_stand()
            self.date_data.text = self.controller.get_date()
            self.time_data.text = self.controller.get_time()
    
    def on_enter(self):
        """Event called by screenmanager
        """
        self.log("On enter")

    def on_pre_leave(self):
        """Event called by screenmanager
        """
        self.log("On pre leave")

    def on_leave(self):
        """Event called by screenmanager
        """
        self.log("On leave")
        self.status = 'new'

    def on_enter_data_pressed(self):
        if self.status == 'new':
            # check if stand data is integer, numeric value
            try:
                stand_value = float(self.stand_data.text)
            except ValueError:
                self.show_alert_dialog(message="Stand sollte eine Zählerstand sein!")
                return

            last_value = self.model.get_last_stand()
            if float(last_value) >= stand_value:
                self.show_alert_dialog(message="Der Stand sollte größer als der Letzte ({})sein!".format(last_value))
                return
                     
            self.controller.on_enter_data()
        else:
            self.controller.on_update_data()

        self.manager_screens.current = "electricity overview screen"

    def on_cancel_pressed(self):
        self.manager_screens.current = "electricity overview screen"

    def get_entered_data(self):
        return {'date': self.app_layout.entry_screen.date_data.text,
                'count': self.app_layout.entry_screen.stand_data.text,
                'time': self.app_layout.entry_screen.time_data.text}

    def show_alert_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda _: self.close_dialog()
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None
