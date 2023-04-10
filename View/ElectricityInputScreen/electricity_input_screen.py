from View.base_input_screen import BaseInputScreen


class ElectricityInputScreenView(BaseInputScreen):
    back_screen = 'electricity overview screen'
    status = 'new'


    def __init__(self, **kwargs):

        self.elements = {'datum': {'id': 'water_datum',
                                   'text': 'Datum'},
                         'time': {'id': 'water_time',
                                  'text': 'Uhrzeit'},
                         'stand': {'id': 'water_stand',
                                   'text': 'Zählerstand'}}

        super().__init__(input_title="Strom Eingabe",
                         overview_screen = 'electricity overview screen',
                         **kwargs)

    def get_data(self):
        return {'datum': self.elements['datum']['widget'].text,
                'time': self.elements['time']['widget'].text,
                'stand': self.elements['stand']['widget'].text}

    def pre_fill_elements(self):
        self.elements['datum']['widget'].text = self.controller.get_date()
        self.elements['time']['widget'].text = self.controller.get_time()
        self.elements['stand']['widget'].text = self.controller.get_last('stand')
