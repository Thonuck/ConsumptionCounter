# The screen's dictionary contains the objects of the models and controllers
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
from Model.water_overview_screen import WaterOverviewScreenModel
from Controller.water_overview_screen import WaterOverviewScreenController
from Model.water_input_screen import WaterInputScreenModel
from Controller.water_input_screen import WaterInputScreenController
from Model.settings_screen import SettingsScreenModel
from Controller.settings_screen import SettingsScreenController
from Model.warmth_input_screen import WarmthInputScreenModel
from Controller.warmth_input_screen import WarmthInputScreenController
from Model.warmth_overview_screen import WarmthOverviewScreenModel
from Controller.warmth_overview_screen import WarmthOverviewScreenController

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
    },
    "water input screen": {
        "model": WaterInputScreenModel,
        "controller": WaterInputScreenController,
    },
    "water overview screen": {
        "model": WaterOverviewScreenModel,
        "controller": WaterOverviewScreenController,
    },
    "settings screen": {
        "model": SettingsScreenModel,
        "controller": SettingsScreenController,
    },
    "warmth input screen": {
        "model": WarmthInputScreenModel,
        "controller": WarmthInputScreenController,
    },
    "warmth overview screen": {
        "model": WarmthOverviewScreenModel,
        "controller": WarmthOverviewScreenController,
    },
}
