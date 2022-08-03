import pygame
from math import sqrt

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Meteor3")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
RECT_GRAY = (100, 100, 100)
BEIGE = (245, 245, 220)
P_BLUE = (147, 214, 237)

##################################################

G = 6.67384*(10**-11)

loc_a = [10, 10]
m_a = 1
loc_b = [50, 50]
m_b = 1

def newton(loc_a, loc_b, G, m_a, m_b):
    r = sqrt((loc_a[0]-loc_b[0])**2+(loc_a[1]-loc_b[1])**2)
    f = G*m_a*m_b/r**2

    newton_x_a = f*(loc_a[0]-loc_b[0])/r**3
    newton_y_a = f*(loc_a[1]-loc_b[1])/r**3
    newton_x_b = f*(loc_b[0]-loc_a[0])/r**3
    newton_y_b = f*(loc_b[1]-loc_a[1])/r**3

    return newton_x_a, newton_y_a, newton_x_b, newton_y_b

##################################################

running = True
while running:
    dt = clock.tick(120)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.