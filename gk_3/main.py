
import pygame
from pygame import K_d, K_a, K_w, K_s, K_1, K_2, K_3, K_4, K_5

from phong_ball import PhongBall

WINDOW_X_SIZE = 400
WINDOW_Y_SIZE = 400

window = pygame.display.set_mode((WINDOW_X_SIZE, WINDOW_Y_SIZE))
active = True
ball = PhongBall()


refresh = True

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                ball.move_light_pos_x(-1)
                refresh = True
            if event.key == K_d:
                ball.move_light_pos_x(1)
                refresh = True
            if event.key == K_w:
                ball.move_light_pos_y(-1)
                refresh = True
            if event.key == K_s:
                ball.move_light_pos_y(1)
                refresh = True
            if event.key == K_1:
                ball.change_material(0)
                refresh = True
            if event.key == K_2:
                ball.change_material(1)
                refresh = True
            if event.key == K_3:
                ball.change_material(2)
                refresh = True
            if event.key == K_4:
                ball.change_material(3)
                refresh = True
            if event.key == K_5:
                ball.change_material(4)
                refresh = True
    if refresh:
        pygame.draw.rect(window, (0, 0, 0), (0, 0, WINDOW_X_SIZE, WINDOW_Y_SIZE))
        ball.create_image(window)
        pygame.display.update()
        refresh = False
        print(ball.light_pos)
