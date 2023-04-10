from abc import abstractmethod

from kivy.core.window import Window
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

    def __init__(self,
                 title,
                 back_screen,
                 new_item_screen,
                 column_data,
                 columns,
                 row_data=[],
                 **kwargs):
        super().__init__(**kwargs)

        self.table = None
        self.back_screen = back_screen
        self.new_item_screen = new_item_screen
        self.columns = columns

        self.layout = MDBoxLayout(orientation="vertical",
                                  spacing=5,
                                  padding=5)

        self.layout.add_widget(self.create_top_bar(title=title))
        self.layout.add_widget(self.create_data_table(column_data=column_data,
                                                 row_data=row_data))
        self.layout.add_widget(self.create_button_frame())

        Window.bind(on_resize=lambda *args: self.update_rows_num())

        self.add_widget(self.layout)

    def update_rows_num(self):
        print("update rows num")
        print("layout size:: {}".format(self.size))
        

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
        #self.columns = [x[0] for x in column_data]
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.9),
            check=False,  # draw checkbox for each row
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num=7,
        )

        self.table.bind(on_check_press=self.on_press_checkbox)
        self.table.bind(on_row_press=self.on_select_row)
        return self.table

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
        self.open_edit_screen(row_data)

    @abstractmethod
    def open_edit_screen(self, row_data):
        pass

    def on_dialog_delete_row(self, instance_row):
        self.dialog.dismiss()
        self.dialog = None
        row_data = self.get_instance_row_data(instance_row)

        data_item = dict(zip(self.columns, row_data))
        self.log_info("Deleting Row {}".format(row_data))
        self.controller.delete_item(data_item)

    def get_instance_row_data(self, instance_row):
        start, end = instance_row.table.recycle_data[instance_row.index]['range']
        return [x['text'] for x in instance_row.table.recycle_data[int(start):int(end) + 1]]
