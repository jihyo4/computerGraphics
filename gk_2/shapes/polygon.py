import random

from shapes.line import Line


class Polygon:
    def __init__(self, line_list=[], color=None):
        self.line_list = line_list
        self.color = color

    def __find_min(self, xyz: int) -> int:
        min_z = None
        for line in self.line_list:
            line: Line = line
            if min_z is None:
                min_z = min(line.a[xyz], line.b[xyz])
            else:
                min_z = min(min(line.a[xyz], line.b[xyz]), min_z)
        return min_z

    def __find_max(self, xyz: int) -> int:
        max_z = None
        for line in self.line_list:
            line: Line = line
            if max_z is None:
                max_z = max(line.a[xyz], line.b[xyz])
            else:
                max_z = max(max(line.a[xyz], line.b[xyz]), max_z)
        return max_z

    def __find_midpoint(self) -> [int, int, int]:
        return (self.__find_max(xyz=0) + self.__find_min(xyz=0)) / 2.0, \
               (self.__find_max(xyz=1) + self.__find_min(xyz=1)) / 2.0, \
               (self.__find_max(xyz=2) + self.__find_min(xyz=2)) / 2.0

    def change_line_order(self):
        new_polygon = Polygon([], color=self.color)
        last_point = None
        i = 0
        for line in self.line_list:
            line: Line = line
            if i == 0:
                if self.line_list[0].b == self.line_list[1].a or self.line_list[0].b == self.line_list[1].b:
                    new_polygon.line_list.append(line)
                else:
                    new_polygon.line_list.append(Line(self.line_list[i].b, self.line_list[i].a))
            else:
                if self.line_list[i].a == last_point:
                    new_polygon.line_list.append(line)
                else:
                    new_polygon.line_list.append(Line(self.line_list[i].b, self.line_list[i].a))
            last_point = new_polygon.line_list[i].b
            i += 1
        return new_polygon

    def get_points(self):
        points = []
        for line in self.line_list:
            if line.a not in points:
                points.append(line.a)
            if line.b not in points:
                points.append(line.b)
        return points

    def distance(self) -> int:
        centroid = self.__find_midpoint()
        return int(centroid[0] ** 2 + centroid[1] ** 2 + centroid[2] ** 2)

    def __get_plane_from_polygon(self):
        points = self.get_points()
        x1 = points[0][0]
        y1 = points[0][1]
        z1 = points[0][2]

        x2 = points[1][0]
        y2 = points[1][1]
        z2 = points[1][2]

        x3 = points[2][0]
        y3 = points[2][1]
        z3 = points[2][2]

        ux = x2 - x1
        uy = y2 - y1
        uz = z2 - z1
        vx = x3 - x1
        vy = y3 - y1
        vz = z3 - z1

        a = uy * vz - uz * vy
        b = uz * vx - ux * vz
        c = ux * vy - uy * vx
        d = (-a * x1 - b * y1 - c * z1)

        return [a, b, c, d]

    @staticmethod
    def __point_matrix_multiplication(matrix, point) -> float:
        return matrix[0] * point[0] + matrix[1] * point[1] + matrix[2] * point[2] + matrix[3]

    def __check_point_side_against_plane(self, matrix, point):
        return self.__point_matrix_multiplication(matrix, point) * self.__point_matrix_multiplication(matrix, [0, 0, 0])

    def __is_point_on_observable_site(self, other):
        result = self.__check_point_side_against_plane(self.__get_plane_from_polygon(), other.__find_midpoint())
        if result > 0:
            return -1
        else:
            return 1

    def __lt__(self, other):
        if type(other) is Polygon:
            other: Polygon = other
            return self.__is_point_on_observable_site(other)
        else:
            return -1
