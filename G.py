import pygame
import math

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("G")
# icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\SandBox\\Butt_On_icon.png")
# pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
text_font = pygame.font.SysFont(None, 25)
num_font = pygame.font.SysFont(None, 20)

# 색 상수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 128, 0)

##################################################

# 함수
def f(x):
    y = x**5 - 3*x**4 + 3*x**3 + 6*x**2 - 4*x + 9
    return y

##################################################

# 점
n = -1
left_dot_list= []
right_dot_list= []

# scale
x_scale = 10
y_scale = 7.5

# button
x_scale_left_button_down = 0
x_scale_right_button_down = 0
y_scale_left_button_down = 0
y_scale_right_button_down = 0

##################################################

running = True
while running:
    dt = clock.tick(100)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # x_scale
            if (mouse[0] - 37)**2 + (mouse[1] - 30)**2 <= 100:
                if x_scale >= 2:
                    x_scale -= 1
                    n = 0
                    left_dot_list = []
                    right_dot_list = []
                    x_scale_left_button_down = 1
            if (mouse[0] - 64)**2 + (mouse[1] - 30)**2 <= 100:
                x_scale += 1
                n = 0
                left_dot_list = []
                right_dot_list = []
                x_scale_right_button_down = 1

            # y_scale
            if (mouse[0] - 37)**2 + (mouse[1] - 60)**2 <= 100:
                if y_scale >= 2:
                    y_scale -= 1
                    n = 0
                    left_dot_list = []
                    right_dot_list = []
                    y_scale_left_button_down = 1
            if (mouse[0] - 64)**2 + (mouse[1] - 60)**2 <= 100:
                y_scale += 1
                n = 0
                left_dot_list = []
                right_dot_list = []
                y_scale_right_button_down = 1

        if event.type == pygame.MOUSEBUTTONUP:
            x_scale_left_button_down = 0
            x_scale_right_button_down = 0
            y_scale_left_button_down = 0
            y_scale_right_button_down = 0


    # 마우스
    mouse = pygame.mouse.get_pos()

##################################################

    # 점 1
    n += 1

        # x > 0
    x = 0.1 * n
    y = f(x)
    x *= x_scale
    y *= y_scale
    right_dot_list.append([x + (screen_width / 2), -y + (screen_height / 2)])

        # x < 0
    x = 0.1 * -n
    y = f(x)
    x *= x_scale
    y *= y_scale
    left_dot_list.append([x + (screen_width / 2), -y + (screen_height / 2)])


    # 점 2
    n += 1

        # x > 0
    x = 0.1 * n
    y = f(x)
    x *= x_scale
    y *= y_scale
    right_dot_list.append([x + (screen_width / 2), -y + (screen_height / 2)])

    pygame.draw.line(screen, GREEN, [x + (screen_width / 2), 0], [x + (screen_width / 2), screen_height])

        # x < 0
    x = 0.1 * -n
    y = f(x)
    x *= x_scale
    y *= y_scale
    left_dot_list.append([x + (screen_width / 2), -y + (screen_height / 2)])
    
    pygame.draw.line(screen, GREEN, [x + (screen_width / 2), 0], [x + (screen_width / 2), screen_height])

##################################################

    # 그래프
    pygame.draw.aalines(screen, WHITE, False, right_dot_list)
    pygame.draw.aalines(screen, WHITE, False, left_dot_list)

    # x축, y축
    pygame.draw.line(screen, GRAY, [-1000, 240], [1000, 240])
    pygame.draw.line(screen, GRAY, [320, 1000], [320, -1000])
    pygame.draw.polygon(screen, GRAY, [[320, 0], [315, 10], [325, 10]])
    pygame.draw.polygon(screen, GRAY, [[640, 240], [630, 235], [630, 245]])

    # 점
        # x축, y축 끝 값
    x_text = num_font.render("{0}".format(round((screen_width / 2) / x_scale, 2)), True, GRAY)
    x_rect = x_text.get_rect(topright = (630, 250))
    screen.blit(x_text, x_rect)

    y_text = num_font.render("{0}".format(round((screen_height / 2) / y_scale, 2)), True, GRAY)
    y_rect = y_text.get_rect(topright = (310, 10))
    screen.blit(y_text, y_rect)

        # x축, y축 중앙값
    pygame.draw.line(screen, GRAY, [480, 235], [480, 245])
    pygame.draw.line(screen, GRAY, [160, 235], [160, 245])
    pygame.draw.line(screen, GRAY, [315, 120], [325, 120])
    pygame.draw.line(screen, GRAY, [315, 360], [325, 360])

        # 마우스
    mouse_dot_x = (mouse[0] - screen_width / 2) / x_scale # pixel -> (x, y)
    mouse_dot_y = f(mouse_dot_x)

    pygame.draw.circle(screen, GREEN, [mouse[0], -mouse_dot_y * y_scale + screen_height / 2], 5)
    mouse_dot_text = num_font.render("({0}, {1})".format(round(mouse_dot_x, 2), round(mouse_dot_y, 2)), True, GRAY)
    mouse_dot_rect = mouse_dot_text.get_rect(topleft = (mouse[0] + 5, -mouse_dot_y * y_scale + screen_height / 2 + 5))
    screen.blit(mouse_dot_text, mouse_dot_rect)

    # 버튼
        # x_scale_left
    pygame.draw.polygon(screen, GRAY, [[30, 30], [40, 25], [40, 35]])
    pygame.draw.circle(screen, GRAY, [37, 30], 10, 1)
    if x_scale_left_button_down == 1:
        pygame.draw.circle(screen, GRAY, [37, 30], 10)
    
        # x_scale_right
    pygame.draw.polygon(screen, GRAY, [[70, 30], [60, 25], [60, 35]])
    pygame.draw.circle(screen, GRAY, [64, 30], 10, 1)
    if x_scale_right_button_down == 1:
        pygame.draw.circle(screen, GRAY, [64, 30], 10)
    
    y_text = text_font.render("x_scale", True, GRAY)
    y_rect = y_text.get_rect(topleft = (85, 20))
    screen.blit(y_text, y_rect)

        # y_scale_left
    pygame.draw.polygon(screen, GRAY, [[30, 60], [40, 55], [40, 65]])
    pygame.draw.circle(screen, GRAY, [37, 60], 10, 1)
    if y_scale_left_button_down == 1:
        pygame.draw.circle(screen, GRAY, [37, 60], 10)

        # y_scale_right
    pygame.draw.polygon(screen, GRAY, [[70, 60], [60, 55], [60, 65]])
    pygame.draw.circle(screen, GRAY, [64, 60], 10, 1)
    if y_scale_right_button_down == 1:
        pygame.draw.circle(screen, GRAY, [64, 60], 10)

    y_text = text_font.render("y_scale", True, GRAY)
    y_rect = y_text.get_rect(topleft = (85, 50))
    screen.blit(y_text, y_rect)

    pygame.display.update()

pygame.quit()