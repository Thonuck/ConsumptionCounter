# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.
from Controller.finances_screen import FinancesScreenController
from Controller.sport_activity_input_screen import SportActivityInputScreenController
from Controller.sport_activity_screen import SportActivityScreenController
from Model.finances_screen import FinancesScreenModel
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.electricity_input_screen import ElectricityInputScreenModel
from Controller.electricity_input_screen import ElectricityInputScreenController
from Model.electricity_overview_screen import ElectricityOverviewScreenModel
from Controller.electricity_overview_screen import ElectricityOverviewScreenController
from Model.sport_activity_input_screen import SportActivityInputScreenModel
from Model.sport_activity_screen import SportActivityScreenModel

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "electricity input screen": {
        "model": ElectricityInputScreenModel,
        "controller": ElectricityInputScreenController,
    },

    "electricity overview screen": {
        "model": ElectricityOverviewScreenModel,
        "controller": ElectricityOverviewScreenController,
    },

    "sport activity screen": {
        "model": SportActivityScreenModel,
        "controller": SportActivityScreenController,
    },

    "finance overview screen": {
        "model": FinancesScreenModel,
        "controller": FinancesScreenController,
    },

    "sport activity input screen": {
        "model": SportActivityInputScreenModel,
        "controller": SportActivityInputScreenController,
    }
}