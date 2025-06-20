import numpy as numpy


class Line:
    def __init__(self, a: [], b: []):
        if len(a) != len(b) != 3:
            raise ValueError()
        self.a: [] = a
        self.b: [] = b

    def trim_line(self):
        if self.a[2] * self.b[2] < 0:
            dx = self.b[0] - self.a[0]
            dy = self.b[1] - self.a[1]
            dz = self.b[2] - self.a[2]
            y = numpy.float64(-dy * (self.a[2] - 1)) / dz + self.a[1]
            x = numpy.float64(-dx * (self.a[2] - 1)) / dz + self.a[0]
            if self.a[2] < 0:
                return Line([x, y, 0], self.b)
            else:
                return Line(self.a, [x, y, 0])
        return self

    def scale_line(self, scale):
        x1 = self.a[0] * scale
        y1 = self.a[1] * scale
        z1 = self.a[2]
        x2 = self.b[0] * scale
        y2 = self.b[1] * scale
        z2 = self.b[2]
        return Line([x1, y1, z1], [x2, y2, z2])

    def project_to2_d(self, distance_from_camera):
        x1 = numpy.float64(self.a[0]) / numpy.float64(self.a[2]) * numpy.float64(distance_from_camera)
        y1 = numpy.float64(self.a[1]) / numpy.float64(self.a[2]) * numpy.float64(distance_from_camera)
        z1 = numpy.float64(self.a[2])
        x2 = numpy.float64(self.b[0]) / numpy.float64(self.b[2]) * numpy.float64(distance_from_camera)
        y2 = numpy.float64(self.b[1]) / numpy.float64(self.b[2]) * numpy.float64(distance_from_camera)
        z2 = numpy.float64(self.b[2])

        return Line([x1, y1, z1], [x2, y2, z2])

    def move_to_center(self, screen_width, screen_height):
        x1 = self.a[0] + screen_width / 2.0
        y1 = self.a[1] + screen_height / 2.0
        z1 = self.a[2]
        x2 = self.b[0] + screen_width / 2.0
        y2 = self.b[1] + screen_height / 2.0
        z2 = self.b[2]

        return Line([x1, y1, z1], [x2, y2, z2])

    def revert_coordinates(self, screen_height):
        x1 = self.a[0]
        y1 = screen_height - self.a[1]
        z1 = self.a[2]
        x2 = self.b[0]
        y2 = screen_height - self.b[1]
        z2 = self.b[2]
        return Line([x1, y1, z1], [x2, y2, z2])

    def __str__(self):
        return f"{self.a} - {self.b}"
