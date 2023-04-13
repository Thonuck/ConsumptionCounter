from View.base_input_screen import BaseInputScreen


class WarmthInputScreenView(BaseInputScreen):
    back_screen = 'warmth overview screen'
    status = 'new'


    def __init__(self, **kwargs):

        self.elements = {'datum': {'id': 'warmth_datum',
                                   'text': 'Datum'},
                         'time': {'id': 'warmth_time',
                                  'text': 'Uhrzeit'},
                         'stand': {'id': 'warmth_stand',
                                   'text': 'Zählerstand'}}

        super().__init__(input_title="Wärme Eingabe",
                         overview_screen = 'warmth overview screen',
                         **kwargs)

    def get_data(self):
        return {'datum': self.elements['datum']['widget'].text,
                'time': self.elements['time']['widget'].text,
                'stand': self.elements['stand']['widget'].text}

    def pre_fill_elements(self):
        self.elements['datum']['widget'].text = self.controller.get_date()
        self.elements['time']['widget'].text = self.controller.get_time()
        # self.elements['stand']['widget'].text = self.controller.get_last('stand')
