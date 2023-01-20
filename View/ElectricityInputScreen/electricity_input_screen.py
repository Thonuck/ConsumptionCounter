from View.base_screen import BaseScreenView
import logging

logger = logging.getLogger()


class ElectricityInputScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = 'new'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def log(self, log_line):
        logger.info('ElectricityInputScreenView: {}'.format(log_line))

    def on_pre_enter(self):
        self.log("On pre enter status {}".format(self.status))
        
        if self.status == 'edit':
            self.controller.on_pre_update_data()
        else:
            self.stand_data.text = ''
            self.date_data.text = self.controller.get_date()
            self.time_data.text = self.controller.get_time()
    
    def on_enter(self):
        self.log("On enter")

    def on_pre_leave(self):
        self.log("On pre leave")

    def on_leave(self):
        self.log("On leave")
        self.status = 'new'

    def on_enter_data_pressed(self):
        if self.status == 'new':
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

