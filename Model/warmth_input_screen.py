from Model.base_model import BaseScreenModel


class WarmthInputScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.WarmthInputScreen.warmth_input_screen.WarmthInputScreenView` class.
    """
    def add(self, new_data):
        with self.data_base.warmth() as warmth:
            warmth.append(new_data)

        self.notify_observers('warmth overview screen')

    def get_last_element(self):
        with self.data_base.warmth() as warmth:
            if warmth:
                try:
                    return warmth[-1]
                except KeyError:
                    return None
                except IndexError:
                    return None
            return None
