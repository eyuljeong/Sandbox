import pygame
from math import pi

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Polygon")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont("휴먼편지체", 30)

# 색 상수
P_BLUE = (147, 214, 237)
BACKGROUND = (245, 245, 220)

##################################################

# 변수
width_list = [30, 40, 50, 60, 70, 60, 50, 40, 30]
height_list = [70, 60, 50, 40, 30, 40, 50, 60, 70]
width_num = 0
height_num = 0

##################################################

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30) # fps

    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            running = False

    # 화면
    screen.fill(BACKGROUND)

    # 사각형 (화면, 색상, [왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 아웃라인의 두께)
    pygame.draw.rect(screen, P_BLUE, [20, 75, 50, 20])
    pygame.draw.rect(screen, P_BLUE, [20, 110, 50, 20], 5)

    # 삼각형 (화면, 색상, [꼭짓점 3개], 아웃라인의 두께)
    pygame.draw.polygon(screen, P_BLUE, [[230, 85], [275, 85], [230, 130]])
    pygame.draw.polygon(screen, P_BLUE, [[275, 95], [275, 130], [240, 130]], 3)

    # 원 (화면, 색상, 중심, 반지름, 아웃라인의 두께)
    pygame.draw.circle(screen, P_BLUE, [90, 85], 10)
    pygame.draw.circle(screen, P_BLUE, [90, 120], 10, 5)

    # 부채꼴 (화면, 색상, [둘러싸는 사각형의 왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 시작 각도, 끝 각도, 아웃라인의 두께 = 1)
    pygame.draw.arc(screen, P_BLUE, [110, 85, 40, 40], pi/30, pi/3, 5)
    pygame.draw.arc(screen, P_BLUE, [110, 85, 40, 40], pi/2, 29*pi/30, 5)
    pygame.draw.arc(screen, P_BLUE, [110, 85, 40, 40], 31*pi/30, 59*pi/30, 5)

    # 타원 (화면, 색상, [둘러싸는 사각형의 왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 아웃라인의 두께)
    pygame.draw.ellipse(screen, P_BLUE, [160, 75, 50, 20])
    pygame.draw.ellipse(screen, P_BLUE, [160, 110, 50, 20], 5)

    # 선 (화면, 색상, 시작 점, 끝 점, 굵기 = 1)
    pygame.draw.line(screen, P_BLUE, [20, 190], [100, 190])
    pygame.draw.line(screen, P_BLUE, [20, 200], [100, 200], 5)

    # 선들 (화면, 색상, 닫힘 여부, [시작 점, ..., 끝 점], 굵기 = 1)
    pygame.draw.lines(screen, P_BLUE, False, [[20, 220], [50, 220], [50, 240]], 3)
    pygame.draw.lines(screen, P_BLUE, True, [[70, 220], [70, 240], [100, 240]], 3)

    # 부드러운 선 (화면, 색상, 시작 점, 끝 점, Anti-Aliasing = True)
    pygame.draw.aaline(screen, P_BLUE, [20, 260], [100, 290], True)
    pygame.draw.aaline(screen, P_BLUE, [20, 270], [100, 300], False)

    # 부드러운 선들 (화면, 색상, 닫힘 여부, [시작 점, ..., 끝 점], Anti-Aliasing = True)
    pygame.draw.aalines(screen, P_BLUE, False, [[20, 300], [100, 320], [100, 340], [20, 360]], True)
    pygame.draw.aalines(screen, P_BLUE, True, [[20, 370], [100, 390], [100, 410], [20, 430]], False)

    ##################################################

    # ?
    width_num += 1
    height_num += 1
    if width_num == 9:
        width_num = 0
    if height_num == 9:
        height_num = 0

    pygame.draw.ellipse(screen, P_BLUE, [320, 240, width_list[width_num], height_list[height_num]])
    pygame.draw.ellipse(screen, P_BLUE, [320, 240 - height_list[height_num], width_list[width_num], height_list[height_num]], 5)
    pygame.draw.ellipse(screen, P_BLUE, [320 - width_list[width_num], 240, width_list[width_num], height_list[height_num]], 5)
    pygame.draw.ellipse(screen, P_BLUE, [320 - width_list[width_num], 240 - height_list[height_num], width_list[width_num], height_list[height_num]])
    pygame.draw.circle(screen, P_BLUE, [320, 240], 10, 5)
    pygame.draw.rect(screen, P_BLUE, [250, 170, 140, 140], 5)
    
    ##################################################

    # 안내
    figure_text = game_font.render("도형", True, P_BLUE)
    figure_rect = figure_text.get_rect(topleft = (20, 30))
    screen.blit(figure_text, figure_rect)

    line_text = game_font.render("선", True, P_BLUE)
    line_rect = line_text.get_rect(topleft = (20, 150))
    screen.blit(line_text, line_rect)

    pygame.display.update()

pygame.quit()