from Model.base_model import BaseScreenModel

class SportActivityScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SportActivityScreen.sport_activity_screen.SportActivityScreenView` class.
    """

    def get(self):
        with self.data_base.sport_activities() as sport_activities:
            return sport_activities

    def delete_item(self, item_data):

        with self.data_base.sport_activities() as sport_activities:
            if item_data in sport_activities:
                sport_activities.remove(item_data)

        self.notify_observers('sport activity screen')

