from core.Navigator import Navigator


class Car:
    """
    Example class
    """
    def __init__(self):
        self.color = 'white'
        self.height = 80
        self.speed = 180
        self.wheels = 4

    def set_color(self, color):
        self.color = color

    def set_properties(self, height, speed, wheels):
        self.height = height
        self.speed = speed
        self.wheels = wheels

    def get_color(self):
        print('color: ' + self.color)

    def get_all(self):
        print('color: ' + self.color)
        print('height:', self.height, 'speed:', self.speed, 'wheels:', self.wheels)