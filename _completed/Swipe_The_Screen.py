import pygame
import os
from math import pi

# 초기화
pygame.init()

# 화면 크기
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("STS")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont("휴먼편지체", 30)

# 색 상수
P_BLUE = (147, 214, 237)

##################################################

# 배경
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "Swipe_The_Screen_background.png"))


# 변수
mousex_start = 0 # 시작점
mousey_start = 0
mousex_end = 0 # 끝점
mousey_end = 0
mouse_num = 0 # 마우스 클릭 확인 여부

mapx = 0 # 이동거리
mapy = 0

##################################################

running = True
while running:
    dt = clock.tick(60) # fps
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        # 종료
        if event.type == pygame.QUIT:
            running = False

        # 마우스
        if event.type == pygame.MOUSEBUTTONDOWN: # 누를 때 한 번 실행
            mouse_num = 1
            mousex_start = pygame.mouse.get_pos()[0] # 시작점 설정
            mousey_start = pygame.mouse.get_pos()[1]
        
        if event.type == pygame.MOUSEBUTTONUP: # 땔 때 한 번 실행
            mouse_num = 0
            mapx += mousex_end - mousex_start
            mapy += mousey_end - mousey_start
            mousex_end = mousex_start = 0 # 시작점, 끝점 초기화
            mousey_end = mousey_start = 0

    # 마우스 현재 위치
    if mouse_num == 1: # 누른 상태라면
        mousex_end = pygame.mouse.get_pos()[0] # 끝점 설정
        mousey_end = pygame.mouse.get_pos()[1]

##################################################

    totalx = mapx + mousex_end - mousex_start
    totaly = mapy + mousey_end - mousey_start

    # 화면
    screen.blit(background, (300 + totalx, totaly)) # 기준점 (0, 0)
    pygame.draw.circle(screen, P_BLUE, [640 + totalx, 360 + totaly], 10, 3)
    
    # ^^
    pygame.draw.arc(screen, P_BLUE, [1210, 10, 50, 45], 0, 2*pi, 4)
    pygame.draw.arc(screen, P_BLUE, [1220, 19, 15, 20], 0, pi, 3)
    pygame.draw.arc(screen, P_BLUE, [1240, 20, 15, 20], 0, pi, 3)
    pygame.draw.arc(screen, P_BLUE, [1225, 25, 20, 20], pi, 2*pi, 3)

    # By. 룡긍
    water_text = game_font.render("By. 룡긍", True, P_BLUE)
    water_rect = water_text.get_rect(topleft = (20, 20))
    screen.blit(water_text, water_rect)

    pygame.display.update()

pygame.quit()