from math import sqrt
import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Meteor Simulation")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
RECT_GRAY = (100, 100, 100)
P_BLUE = (147, 214, 237)
BEIGE = (245, 245, 220)

##################################################

to_x = 0
to_y = 2

m_loc = [100, 100]
m_R = 10

p_loc = [200, 200]
p_G = 1000
p_R = 30

def gravity(m_loc, p_loc, p_G):
    d = sqrt((p_loc[0] - m_loc[0])**2 + (p_loc[1] - m_loc[1])**2)

    g_x = p_G * (p_loc[0] - m_loc[0]) / (d**3)
    g_y = p_G * (p_loc[1] - m_loc[1]) / (d**3)

    return g_x, g_y

##################################################

running = True
while running:
    dt = clock.tick(60)
    screen.fill(BEIGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    g_x, g_y = gravity(m_loc, p_loc, p_G)

    to_x += g_x
    to_y += g_y

    m_loc = [m_loc[0] + to_x, m_loc[1] + to_y]

##################################################
    
    pygame.draw.circle(screen, RECT_GRAY, (m_loc[0], m_loc[1]), m_R)
    pygame.draw.circle(screen, GRAY, (p_loc[0], p_loc[1]), p_R)

    pygame.display.update()

pygame.quit()