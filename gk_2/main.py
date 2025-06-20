import pygame as pg

from camera import Camera
from shapes.cube import Cube

BROWN = (150, 126, 118)
BEIGE = (248, 237, 227)
BLUE = (193, 239, 255)
RED = (255, 179, 179)
PINK = (249, 206, 238)
PEACH = (235, 99, 131)
GREEN = (196, 223, 170)
SAGE = (105, 132, 116)
PURPLE = (217, 215, 241)

WINDOW_X_SIZE = 1280
WINDOW_Y_SIZE = 720

DISTANCE_FROM_CAMERA = 450
DISTANCE_BETWEEN_POINTS = 150
DISTANCE_FROM_CENTER = 100

window = pg.display.set_mode((WINDOW_X_SIZE, WINDOW_Y_SIZE))

active = True
def create_cubes():
    cubes = [
        #Cube(DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, BROWN, DISTANCE_FROM_CAMERA,
            #DISTANCE_BETWEEN_POINTS),
        #Cube(-DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, BLUE, DISTANCE_FROM_CAMERA,
            #DISTANCE_BETWEEN_POINTS),
        #Cube(DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, RED, DISTANCE_FROM_CAMERA,
            #DISTANCE_BETWEEN_POINTS),
        Cube(DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER+50, -DISTANCE_FROM_CENTER+50, PINK, DISTANCE_FROM_CAMERA,
            DISTANCE_BETWEEN_POINTS),
        #Cube(-DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, PEACH, DISTANCE_FROM_CAMERA,
            #DISTANCE_BETWEEN_POINTS),
        Cube(-DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, GREEN, DISTANCE_FROM_CAMERA,
            DISTANCE_BETWEEN_POINTS),
        Cube(DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER-30, -DISTANCE_FROM_CENTER+100, SAGE, DISTANCE_FROM_CAMERA,
            DISTANCE_BETWEEN_POINTS),
        Cube(-DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER-50, -DISTANCE_FROM_CENTER+150, PURPLE, DISTANCE_FROM_CAMERA,
            DISTANCE_BETWEEN_POINTS),
    ]
    return cubes

cubes = create_cubes()
clock = pg.time.Clock()

camera = Camera(cubes)
while active:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            active = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                camera.move_down()
            if event.key == pg.K_UP:
                camera.move_up()
            if event.key == pg.K_LEFT:
                camera.move_left()
            if event.key == pg.K_RIGHT:
                camera.move_right()
            if event.key == pg.K_m:
                camera.move_forward()
            if event.key == pg.K_n:
                camera.move_back()

            if event.key == pg.K_w:
                camera.rotate_x(1)
            if event.key == pg.K_s:
                camera.rotate_x(-1)
            if event.key == pg.K_a:
                camera.rotate_y(1)
            if event.key == pg.K_d:
                camera.rotate_y(-1)
            if event.key == pg.K_f:
                camera.rotate_z(1)
            if event.key == pg.K_r:
                camera.rotate_z(-1)

            if event.key == pg.K_KP_MINUS:
                camera.scale_down()
            if event.key == pg.K_KP_PLUS:
                camera.scale_up()

            if event.key == pg.K_SPACE:
                cubes = create_cubes()
                camera = Camera(cubes)
    pg.draw.rect(window, BEIGE, (0, 0, WINDOW_X_SIZE, WINDOW_Y_SIZE))
    camera.draw(window, 450, WINDOW_X_SIZE, WINDOW_Y_SIZE, z1=False)
    pg.display.update()
    clock.tick(1000)
