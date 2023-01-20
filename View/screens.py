# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.electricity_input_screen import ElectricityInputScreenModel
from Controller.electricity_input_screen import ElectricityInputScreenController
from Model.electricity_overview_screen import ElectricityOverviewScreenModel
from Controller.electricity_overview_screen import ElectricityOverviewScreenController

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
}