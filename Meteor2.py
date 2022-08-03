from math import sqrt
import pygame
from random import randrange

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

class Meteor():
    def __init__(self, m_loc, to_x = 0, to_y = 0, m_R = 10):
        self.m_loc = m_loc
        self.to_x = to_x
        self.to_y = to_y
        self.m_R = m_R

def gravity(m_loc, p_loc, p_G):
    d = sqrt((p_loc[0] - m_loc[0])**2 + (p_loc[1] - m_loc[1])**2)

    g_x = p_G * (p_loc[0] - m_loc[0]) / (d**3)
    g_y = p_G * (p_loc[1] - m_loc[1]) / (d**3)

    return g_x, g_y

p_loc = [320, 240]
p_G = 700
p_R = 30

meteorList = []

mouse_down = 0

K = 0.01 # 발사 속도 비례상수

##################################################

running = True
while running:
    dt = clock.tick(120)
    screen.fill(BEIGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = 1

            start_x = mouse[0]
            start_y = mouse[1]

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = 0

            end_x = mouse[0]
            end_y = mouse[1]

            # 발사 속도
            to_x = K * (end_x - start_x)
            to_y = K * (end_y - start_y)

            # 크기
            m_R = randrange(5, 31)

            meteorList.append(Meteor([start_x, start_y], to_x, to_y, m_R))


    mouse = pygame.mouse.get_pos()

##################################################

    for meteor in meteorList:
        g_x, g_y = gravity(meteor.m_loc, p_loc, p_G)

        meteor.to_x += g_x
        meteor.to_y += g_y
        meteor.m_loc = [meteor.m_loc[0] + meteor.to_x, meteor.m_loc[1] + meteor.to_y]
        
        if sqrt((p_loc[0] - meteor.m_loc[0])**2 + (p_loc[1] - meteor.m_loc[1])**2) <= p_R + meteor.m_R:
            meteorList.pop(meteorList.index(meteor))

        pygame.draw.circle(screen, RECT_GRAY, (meteor.m_loc[0], meteor.m_loc[1]), meteor.m_R)

    if mouse_down == 1:
        pygame.draw.line(screen, WHITE, [start_x, start_y], [mouse[0], mouse[1]], 3)
        pygame.draw.circle(screen, WHITE, (start_x, start_y), 10, 3)
        pygame.draw.circle(screen, WHITE, (mouse[0], mouse[1]), 10, 3)
    pygame.draw.circle(screen, BLACK, (p_loc[0], p_loc[1]), p_R)

    pygame.display.update()

pygame.quit()