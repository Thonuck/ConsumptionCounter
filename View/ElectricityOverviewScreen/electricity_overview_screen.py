from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from View.base_table_screen import BaseTableScreen


class ElectricityOverviewScreenView(BaseTableScreen):

    def __init__(self, **kwargs):
        column_data = [("Datum", dp(20)),
                       ("Zeit", dp(20)),
                       ("Stand", dp(40))]

        super().__init__(title='Stromverbrauch Übersicht',
                         new_item_screen='electricity input screen',
                         back_screen='main screen',
                         column_data=column_data,
                         row_data=[],
                         columns=['datum', 'time', 'stand'],
                         **kwargs)    
