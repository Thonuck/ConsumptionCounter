from View.base_input_screen import BaseInputScreen


class SportActivityInputScreenView(BaseInputScreen):
    back_screen = 'sport activity screen'
    status = 'new'


    def __init__(self, **kwargs):

        self.elements = {'datum': {'id': 'sport_activity_datum',
                                   'text': 'Datum'},
                         'activity': {'id': 'sport_activity_type',
                                      'text': 'Activity'}}

        super().__init__(input_title="Sport Activity Input",
                         overview_screen = 'sport activity screen',
                         **kwargs)



    def get_data(self):
        return {'datum': self.elements['datum']['widget'].text,
                'activity': self.elements['activity']['widget'].text}

