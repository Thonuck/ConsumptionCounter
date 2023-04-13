from kivy.metrics import dp
from View.base_screen import BaseScreenView
from View.base_table_screen import BaseTableScreen

class WarmthOverviewScreenView(BaseTableScreen):

    def __init__(self, **kwargs):
        column_data = [("Datum", dp(20)),
                       ("Zeit", dp(20)),
                       ("Stand", dp(40))]

        super().__init__(title='Wärme Übersicht',
                         new_item_screen='warmth input screen',
                         back_screen='main screen',
                         column_data=column_data,
                         row_data=[],
                         columns=['datum', 'time', 'stand'],
                         **kwargs)    
