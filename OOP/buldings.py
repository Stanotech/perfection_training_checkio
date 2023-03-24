class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.point_x = west
        self.point_y = south
        self.x_length = width_WE
        self.y_length = width_NS
        self.height = height

    def corners(self):
        return {'north-east': [self.point_x + self.x_length, self.point_y + self.y_length], 'south-east': [self.point_y, self.point_x + self.x_length], 'south-west': [self.point_y, self.point_x], 'north-west': [self.point_y + self.y_length, self.point_x]}

    def area(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    print(json_dict(b.corners()))
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
