from core.Navigator import Navigator
from tests.car import Car


class CarController:
    """
    Example class
    """
    def __init__(self):
        self.car = Car()
        self.logged_in = False
        self.nav = Navigator()
        self.nav.set_end('>: ')

    def show_motd(self):
        print("""
+--------------------------------------+
+ Car control (example application)    +
+ v1.0                                 +
+--------------------------------------+
        """)
        self.nav.navigate('guest')
        print("Welcome, guest!")

    def get_nav(self):
        return self.nav.getLocation()

    def login(self, username):
        password = input("Enter your password: ")
        if password == "***":
            print("\n\r Welcome back, "+ username + "\n\r")
            self.nav.navigate(username)
            self.logged_in = True
        else:
            print("[Access denied] password incorrect")

    def logout(self):
        if self.logged_in == False:
            print("Please login first!")
            return 0

        self.nav.clean()
        self.nav.navigate('guest')
        self.logged_in = False
        print("Logged out successfully")


    def set_car_color(self, color):
        if self.logged_in == False:
            print("Permission denied!")
            return 0

        self.car.set_color(color)
        print("Changed car color to " + color)

    def get_car_color(self):
        return self.car.get_color()

    def get_car_properties(self):
        return self.car.get_all()
