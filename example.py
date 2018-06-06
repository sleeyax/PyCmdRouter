from core.CommandRouter import CommandRouter
from tests.CarController import CarController

carController = CarController()
router = CommandRouter()
router.set_callback(carController)

router.register('login {:str}', 'login')
router.register('logout', 'logout')
router.register('set color {:str}', 'set_car_color')
router.register('get color', 'get_car_color')

carController.show_motd()
command = input(carController.get_nav())
while command != "exit":
    router.route(command)
    command = input(carController.get_nav())
