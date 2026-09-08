class Address:
    index = "124527"
    town = "Moscow"
    street = "Pushkina"
    house = "15"
    flat = "346"

    def __init__(self, index, town, house, flat):
        self.i = index
        self.t = town
        self.h = house
        self.f = flat
        