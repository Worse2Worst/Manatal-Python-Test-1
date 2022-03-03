from math import pi


class Circle:
    def __init__(self, radius):
        assert radius > 0, 'Radius must be greater than 0'
        self.radius = radius

    def get_area(self):
        return pi * self.radius * self.radius

    def get_perimeter(self):
        return 2.0 * pi * self.radius
