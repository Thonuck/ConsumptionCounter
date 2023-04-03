from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from View.base_app_screen import BaseAppScreenView
import logging


logger = logging.getLogger()


class BaseTableScreen(BaseAppScreenView):
    new_item_screen = ''
    dialog = None

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.controller.update_table_from_database()

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



    def on_press_checkbox(self):
        """Called by table """
        pass

    def on_select_row(self, instance_table, instance_row):
        """Called by table """
        self.log_info("SELECT ROW: {} - {}".format(instance_table, instance_row))
        self.show_item_dialog(instance_row)

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
        # self.log_info("Editing Row {}".format(row_data))

        # input_screen = self.manager_screens.get_screen("electricity input screen")
        # input_screen.date_data.text = row_data[0]
        # input_screen.time_data.text = row_data[1]
        # input_screen.stand_data.text = row_data[2]
        # self.log_info("setting to edit")
        # input_screen.status = 'edit'
        # self.manager_screens.current = "electricity input screen"

    def on_dialog_delete_row(self, instance_row):
        self.dialog.dismiss()
        self.dialog = None
        row_data = self.get_instance_row_data(instance_row)
        self.log_info("Deleting Row {}".format(row_data))
        self.controller.delete_row_data(row_data)

    def get_instance_row_data(self, instance_row):
        start, end = instance_row.table.recycle_data[instance_row.index]['range']
        return [x['text'] for x in instance_row.table.recycle_data[int(start):int(end) + 1]]
