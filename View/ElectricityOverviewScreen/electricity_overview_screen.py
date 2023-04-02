from kivymd.uix.toolbar import MDTopAppBar

from View.base_screen import BaseScreenView
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
import logging

logger = logging.getLogger()

class ElectricityOverviewScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.controller.update_table_from_database()

    def log_info(self, log_line):
        logger.info('ElectricityOverviewScreenView: {}'.format(log_line))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log_info("IDS: {}".format(self.ids))
         
        layout = MDBoxLayout(orientation="vertical",
                             spacing=5,
                             padding=5)

        top_bar = MDTopAppBar(title="Electicity Overview",
                              right_action_items=[["dots-vertical", lambda x: self.on_settings_pressed()]])

        self.table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.9),
            check = False,  # draw checkbox for each row
            column_data = [("Datum", dp(20)),
                           ("Uhrzeit", dp(18)),
                           ("Stand", dp(20))],
            row_data = [("15.12.2022", "21:56", "123456.7"),
                        ("13.12.2022", "20:16", "123400.7"),
                        ("10.12.2022", "05:16", "123304.7")]

        )
        self.table.bind(on_check_press=self.on_press_checkbox)
        self.table.bind(on_row_press=self.on_select_row)

        btn_frame = MDBoxLayout(orientation="horizontal",
                                spacing=5,
                                padding=5,
                                size_hint = (0.9, 0.1),
                                pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                                )

        insert_btn = MDRaisedButton(text="Eingabe",
                                    size_hint=(1, None),
                                    font_size='24sp',
                                    on_release=self.on_entry_button)

        back_btn = MDRaisedButton(text="Zurueck",
                                  size_hint=(1, None),
                                  font_size='24sp',
                                  on_release=self.on_back_button)

        btn_frame.add_widget(back_btn)
        btn_frame.add_widget(insert_btn)

        layout.add_widget(top_bar)
        layout.add_widget(self.table)
        layout.add_widget(btn_frame)

        self.add_widget(layout)
        self.dialog = None

    def on_entry_button(self, widget=None):
        entry_screen = self.manager_screens.get_screen("electricity input screen")
        entry_screen.status = 'new'
        self.manager_screens.current = "electricity input screen"


    def on_back_button(self, widget=None):
        self.manager_screens.current = "main screen"

    def on_press_checkbox(self, instanace_table, current_row):
        self.log_info("SELECT ROW: {} - {}".format(instance_table, current_row))

    def on_select_row(self, instance_table, instance_row):
        self.log_info("SELECT ROW: {} - {}".format(instance_table, instance_row))
        self.show_item_dialog(instance_row)


    def get_instance_row_data(self, instance_row):
        
        start, end = instance_row.table.recycle_data[instance_row.index]['range']
        return [x['text'] for x in instance_row.table.recycle_data[int(start):int(end)+1]]

    def show_item_dialog(self, instance_row):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Was willst Du machen?",
                buttons=[
                    MDRaisedButton(
                        text="Loeschen",
                        font_size="24sp",
                        on_release=lambda _: self.on_dialog_delete_row(instance_row)
                    ),
                    MDRaisedButton(
                        text="Editieren",
                        font_size="24sp",
                        on_release=lambda _: self.on_dialog_edit_row(instance_row)
                    ),
                ],
            )
        self.dialog.open()

    def on_dialog_edit_row(self, instance_row):
        self.dialog.dismiss()
        self.dialog = None
        row_data = self.get_instance_row_data(instance_row)
        self.log_info("Editing Row {}".format(row_data))

        input_screen = self.manager_screens.get_screen("electricity input screen")
        input_screen.date_data.text = row_data[0]
        input_screen.time_data.text = row_data[1]
        input_screen.stand_data.text = row_data[2]
        self.log_info("setting to edit")
        input_screen.status = 'edit'
        self.manager_screens.current = "electricity input screen"
        

    def on_dialog_delete_row(self, instance_row):
        self.dialog.dismiss()
        self.dialog = None
        row_data = self.get_instance_row_data(instance_row)
        self.log_info("Deleting Row {}".format(row_data))
        self.controller.delete_row_data(row_data)


    def on_settings_pressed(self):
        self