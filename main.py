import pygame
import random
pygame.init()

fullscreen = False
window_width = 1000
window_height = 800
speed = 15
rect_width = 150
rect_height = 150
rect_x = random.randint(0, window_width) / 2
rect_y = random.randint(0, window_height) / 2

if fullscreen:
    window_width = 1920
    window_height = 1080
    rect_width = 225
    rect_height = 225
    speed = 10
else:
    pass


color = [
    (204, 0, 0),
    (0, 204, 0),
    (0, 0, 204),
    (0, 204, 204),
    (255, 128, 0),
    (255, 0, 127),
    (102, 255, 178)
]


DVD_velx = 2
DVD_vely = DVD_velx

border_left = 0
border_right = window_width
border_top = 0
border_bottom = window_height

WIN = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("DVD screensaver")

color_choice = random.choice(color)

inital_directionx = random.randint(1, 2)
inital_directiony = random.randint(1, 2)

run = True
while run:
    pygame.time.delay(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    WIN.fill((0, 0, 0))
    DVD = pygame.draw.rect(WIN, (color_choice), (rect_x, rect_y, rect_width, rect_height))

    rect_left = rect_x
    rect_right = rect_x + rect_width
    rect_top = rect_y
    rect_bottom = rect_y + rect_height

    #if statement hell
    if inital_directionx == 1:
        rect_x += DVD_velx
    if inital_directionx == 2:
        rect_x -= DVD_velx
    if inital_directiony == 1:
        rect_y += DVD_vely
    if inital_directiony == 2:
        rect_y -= DVD_vely

    if rect_left <= border_left:
        rect_x += 4
        DVD_velx = DVD_velx * -1
        color_choice = random.choice(color)
    if rect_right >= border_right:
        rect_x -= 4
        DVD_velx = DVD_velx * -1
        color_choice = random.choice(color)
    if rect_top <= border_top:
        rect_y += 4
        DVD_vely = DVD_vely * -1
        color_choice = random.choice(color)
    if rect_bottom >= border_bottom:
        rect_y -= 4
        DVD_vely = DVD_vely * -1
        color_choice = random.choice(color)

    print(DVD_velx, DVD_vely)

    pygame.display.update()
