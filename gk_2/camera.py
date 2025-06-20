from math import cos, sin

import pygame

from shapes.cube import Cube
from shapes.line import Line
from shapes.polygon import Polygon

ALOT = 1e6


class Camera:
    def __init__(self, elem: []):
        self.screen_elems = elem
        self.scale = 1
        self.movingStep = 100
        self.rotationDegree = 0.1
        self.scaling_step = 0.5

    def move_forward(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[2] = p[2] + self.movingStep

    def move_back(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[2] = p[2] - self.movingStep

    def move_left(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[0] = p[0] + self.movingStep

    def move_right(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[0] = p[0] - self.movingStep

    def move_up(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[1] = p[1] - self.movingStep

    def move_down(self):
        for d in self.screen_elems:
            for p in d.point_list:
                p[1] = p[1] + self.movingStep

    def rotate_x(self, sign):
        for d in self.screen_elems:
            for p in d.point_list:
                p[1] = p[1] * cos(self.rotationDegree * sign) - p[2] * sin(self.rotationDegree * sign)
                p[2] = p[1] * sin(self.rotationDegree * sign) + p[2] * cos(self.rotationDegree * sign)

    def rotate_y(self, sign):
        for d in self.screen_elems:
            for p in d.point_list:
                p[0] = (p[0] * cos(self.rotationDegree * sign) + p[2] * sin(self.rotationDegree * sign))
                p[2] = (-p[0] * sin(self.rotationDegree * sign) + p[2] * cos(self.rotationDegree * sign))

    def rotate_z(self, sign):
        for d in self.screen_elems:
            for p in d.point_list:
                p[0] = p[0] * cos(self.rotationDegree * sign) - p[1] * sin(self.rotationDegree * sign)
                p[1] = p[0] * sin(self.rotationDegree * sign) + p[1] * cos(self.rotationDegree * sign)

    def scale_up(self):
        self.scale += self.scaling_step

    def scale_down(self):
        self.scale -= self.scaling_step

    def draw(self, screen, distance_from_camera, screen_width, screen_height, z1=False):
        if z1:
            for elem in self.screen_elems:
                for line in elem.line_list:
                    line: Line = line
                    line = line.trim_line().scale_line(self.scale).project_to2_d(distance_from_camera) \
                        .move_to_center(screen_width, screen_height).revert_coordinates(screen_height)
                    x1 = line.a[0]
                    y1 = line.a[1]
                    x2 = line.b[0]
                    y2 = line.b[1]
                    if line.a[2] >= 0 and line.b[2] >= 0:
                        pygame.draw.line(screen, elem.color, (x1, y1), (x2, y2))
        else:
            sorted_polygons = self.__sort_polygons()
            for polygon in sorted_polygons:
                polygon: Polygon = polygon
                polygon = polygon.change_line_order()
                points = []
                for line in polygon.line_list:
                    line: Line = line.trim_line().scale_line(self.scale).project_to2_d(distance_from_camera) \
                        .move_to_center(screen_width, screen_height).revert_coordinates(screen_height)
                    if line.a[2] >= 0 and line.b[2] >= 0:
                        points.append((max(min(line.a[0], ALOT), -ALOT), max(min(line.a[1], ALOT), -ALOT)))
                        points.append((max(min(line.b[0], ALOT), -ALOT), max(min(line.b[1], ALOT), -ALOT)))
                try:
                    pygame.draw.polygon(screen, polygon.color, points)
                except:
                    pass

    def __sort_polygons(self):
        sorted_polygon_list = []
        for elem in self.screen_elems:
            elem: Cube = elem
            sorted_polygon_list += elem.polygon_list
        sorted_polygon_list = sorted(sorted_polygon_list, key=lambda x: x.distance(), reverse=True)
        sorted_polygon_list.sort()
        sorted_polygon_list.sort()
        return sorted_polygon_list
