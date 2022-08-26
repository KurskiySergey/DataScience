class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def total_mass(self, mass_per_sq_meter, depth):
        return self._width * self._length * mass_per_sq_meter * depth / 1000


if __name__ == "__main__":
    road = Road(width=20, length=5000)
    mass = road.total_mass(mass_per_sq_meter=25, depth=5)
    print(mass)
