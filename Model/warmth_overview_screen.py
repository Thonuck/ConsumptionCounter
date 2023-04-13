from Model.base_model import BaseScreenModel


class WarmthOverviewScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.WarmthOverviewScreen.warmth_overview_screen.WarmthOverviewScreenView` class.
    """

    def get(self):
        with self.data_base.warmth() as warmth:
            return warmth

    def delete_item(self, item_data):

        with self.data_base.warmth() as warmth:
            if item_data in warmth:
                warmth.remove(item_data)

        self.notify_observers('warmth overview screen')
