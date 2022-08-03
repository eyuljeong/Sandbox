import pygame
import math
from math import pi
from pygame.constants import K_LEFT, K_RIGHT

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Spinning_Rect")
# icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\SandBox\\Butt_On_icon.png")
# pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
logo_font = pygame.font.SysFont("consolas", 15, True, True)
angle_font = pygame.font.SysFont("consolas", 20)
menu_font = pygame.font.SysFont("consolas", 15)

# 색 상수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
RECT_GRAY = (100, 100, 100)
P_BLUE = (147, 214, 237)
BEIGE = (245, 245, 220)

##################################################

# 사각형
width = 200
radius = 10
ratio = 5
angle = 0

# 밝기
def brightness(default_brightness, angle):
    new_rgb = []
    for num in default_brightness:
        rotated_brightness = num * (-math.cos(angle % math.pi) + 1)
        new_rgb.append(round(rotated_brightness))
    return tuple(new_rgb)

# 키보드
key_num = 0

##################################################

# angle 버튼 1
butt1_x = 320
butt1_y = 400
butt1_radius = 15
butt1_num = 0
butt1_left_end = 120
butt1_right_end = 520

# menu 버튼 2
butt2_x = 600
butt2_y = 30
butt2_radius = 17
butt2_num = 0

menu_x = 640
menu_autox = 0
menu_speed = 0.05

# width 버튼 3
butt3_x = 460
butt3_y = 100
butt3_radius = 10
butt3_num = 0
butt3_left_end = 380
butt3_right_end = 580

# height 버튼 4
butt4_x = 400
butt4_y = 200
butt4_radius = 10
butt4_num = 0
butt4_left_end = 380
butt4_right_end = 580

# FOV 버튼 5
butt5_x = 398
butt5_y = 300
butt5_radius = 10
butt5_num = 0
butt5_left_end = 380
butt5_right_end = 580

##################################################

running = True
while running:
    dt = clock.tick(60)
    screen.fill(BEIGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # angle 버튼 1
            if (mouse[0] - butt1_x)**2 + (mouse[1] - butt1_y)**2 <= butt1_radius**2:
                butt1_num = 1

            # menu 버튼 2
            if (mouse[0] - butt2_x)**2 + (mouse[1] - butt2_y)**2 <= butt2_radius**2:
                if butt2_num == 0:
                    butt2_num = 1
                    menu_x = 640
                    menu_autox = 0
                elif butt2_num == 1:
                    butt2_num = 0
            if mouse[0] < 320 and butt2_num == 1:
                butt2_num = 0

            # width 버튼 3
            if butt2_num == 1 and (mouse[0] - butt3_x)**2 + (mouse[1] - butt3_y)**2 <= butt3_radius**2:
                butt3_num = 1
                butt1_x = 370

            # height 버튼 4
            if butt2_num == 1 and (mouse[0] - butt4_x)**2 + (mouse[1] - butt4_y)**2 <= butt4_radius**2:
                butt4_num = 1
                butt1_x = 370
    
            # FOV 버튼 5
            if butt2_num == 1 and (mouse[0] - butt5_x)**2 + (mouse[1] - butt5_y)**2 <= butt5_radius**2:
                butt5_num = 1
                butt1_x = 320 + 100 * 7/8

        if event.type == pygame.MOUSEBUTTONUP:
            # angle 버튼 1
            butt1_num = 0

            # width 버튼 3
            butt3_num = 0

            # height 버튼 4
            butt4_num = 0

            # FOV 버튼 5
            butt5_num = 0

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                key_num = 1
            elif event.key == K_RIGHT:
                key_num = 2

        if event.type == pygame.KEYUP:
            key_num = 0

    # 마우스
    mouse = pygame.mouse.get_pos()

##################################################

    # 키보드
    if key_num == 1:
        butt1_x -= 1
    elif key_num == 2:
        butt1_x += 1

    if butt1_x < butt1_left_end:
        butt1_x = butt1_left_end
    elif butt1_x > butt1_right_end:
        butt1_x = butt1_right_end

##################################################

    # 보조선
    axis = [[(screen_width - width)/ 2, screen_height/2], [(screen_width + width)/ 2, screen_height/2]]
    pygame.draw.line(screen, GRAY, axis[0], axis[1], 1)
    pygame.draw.circle(screen, GRAY, axis[0], radius, 1)
    pygame.draw.circle(screen, GRAY, axis[1], radius, 1)
    pygame.draw.ellipse(screen, GRAY, [axis[0][0] - radius, axis[0][1] - radius*ratio,\
         2*radius, 2*radius*ratio], 1)
    pygame.draw.ellipse(screen, GRAY, [axis[1][0] - radius, axis[1][1] - radius*ratio,\
         2*radius, 2*radius*ratio], 1)

    # 사각형
    rotated_GRAY = brightness(RECT_GRAY, angle)
    pygame.draw.polygon(screen, rotated_GRAY, [\
        [axis[0][0] + radius*math.cos(angle), axis[0][1] + radius*math.sin(angle)*ratio],
        [axis[0][0] - radius*math.cos(angle), axis[0][1] - radius*math.sin(angle)*ratio],
        [axis[1][0] - radius*math.cos(angle), axis[1][1] + radius*math.sin(angle)*ratio]])
    pygame.draw.polygon(screen, rotated_GRAY, [\
        [axis[0][0] - radius*math.cos(angle), axis[1][1] - radius*math.sin(angle)*ratio],
        [axis[1][0] + radius*math.cos(angle), axis[1][1] - radius*math.sin(angle)*ratio],
        [axis[1][0] - radius*math.cos(angle), axis[0][1] + radius*math.sin(angle)*ratio]])

##################################################

    # angle 버튼 1
    if butt1_num == 1:
        butt1_x = pygame.mouse.get_pos()[0]
        if butt1_x < butt1_left_end:
            butt1_x = butt1_left_end
        elif butt1_x > butt1_right_end:
            butt1_x = butt1_right_end

    pygame.draw.circle(screen, GRAY, (butt1_left_end, butt1_y), butt1_radius + 3) # 아웃라인
    pygame.draw.circle(screen, GRAY, (butt1_right_end, butt1_y), butt1_radius + 3)
    pygame.draw.rect(screen, GRAY, (butt1_left_end, butt1_y - butt1_radius, butt1_right_end - butt1_left_end, 2*butt1_radius), 7)
    pygame.draw.circle(screen, P_BLUE, (butt1_left_end, butt1_y), butt1_radius) # 배경
    pygame.draw.circle(screen, P_BLUE, (butt1_right_end, butt1_y), butt1_radius)
    pygame.draw.rect(screen, P_BLUE, (butt1_left_end, butt1_y - butt1_radius, butt1_right_end - butt1_left_end, 2*butt1_radius))
    pygame.draw.line(screen, GRAY, [(butt1_left_end + butt1_right_end)/2, butt1_y - butt1_radius],
    [(butt1_left_end + butt1_right_end)/2, butt1_y + butt1_radius - 1])

    pygame.draw.circle(screen, WHITE, (butt1_x, butt1_y), butt1_radius, 3)
    if butt1_num == 0:
        pygame.draw.circle(screen, WHITE, (butt1_x, butt1_y), butt1_radius)

    butt1_value = (butt1_x - butt1_left_end)/(butt1_right_end - butt1_left_end)*4*pi - 2*pi
    butt1_value_text = angle_font.render("ANGLE | " + str(round(butt1_value/pi, 2)) + "π", True, BLACK)
    butt1_value_rect = butt1_value_text.get_rect(topleft = (butt1_left_end, butt1_y - butt1_radius - 25))
    screen.blit(butt1_value_text, butt1_value_rect)

    angle = butt1_value

##################################################

    # menu 버튼 2
    pygame.draw.rect(screen, RECT_GRAY, (butt2_x - 10, butt2_y - 9, 20, 4))
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x - 10, butt2_y - 7), 2)
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x + 10, butt2_y - 7), 2)
    pygame.draw.rect(screen, RECT_GRAY, (butt2_x - 10, butt2_y - 2, 20, 4))
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x - 10, butt2_y), 2)
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x + 10, butt2_y), 2)
    pygame.draw.rect(screen, RECT_GRAY, (butt2_x - 10, butt2_y + 5, 20, 4))
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x - 10, butt2_y + 7), 2)
    pygame.draw.circle(screen, RECT_GRAY, (butt2_x + 10, butt2_y + 7), 2)

    # 메뉴
    if butt2_num == 1:
        menu_autox += menu_speed * dt
        menu_x -= menu_autox
        if menu_x < 320: # 640 -> 320
            menu_x = 320

        menu = pygame.Surface((320, 480), pygame.SRCALPHA)
        menu.fill((230, 230, 230, 200))
        screen.blit(menu, (menu_x, 0))

        menu_border = pygame.Surface((3, 480), pygame.SRCALPHA)
        menu_border.fill((100, 100, 100, 200))
        screen.blit(menu_border, (menu_x, 0))

##################################################

        
        # width 버튼 3
        if butt3_num == 1:
            butt3_x = pygame.mouse.get_pos()[0]
            if butt3_x < butt3_left_end:
                butt3_x = butt3_left_end
            elif butt3_x > butt3_right_end:
                butt3_x = butt3_right_end

        pygame.draw.circle(screen, RECT_GRAY, (butt3_left_end + menu_x - 320, butt3_y), butt3_radius + 3) # 아웃라인
        pygame.draw.circle(screen, RECT_GRAY, (butt3_right_end + menu_x - 320, butt3_y), butt3_radius + 3)
        pygame.draw.rect(screen, RECT_GRAY, (butt3_left_end + menu_x - 320, butt3_y - butt3_radius, butt3_right_end - butt3_left_end, 2*butt3_radius), 7)
        pygame.draw.circle(screen, BEIGE, (butt3_left_end + menu_x - 320, butt3_y), butt3_radius) # 배경
        pygame.draw.circle(screen, BEIGE, (butt3_right_end + menu_x - 320, butt3_y), butt3_radius)
        pygame.draw.rect(screen, BEIGE, (butt3_left_end + menu_x - 320, butt3_y - butt3_radius, butt3_right_end - butt3_left_end, 2*butt3_radius))
        pygame.draw.line(screen, RECT_GRAY, [(butt3_left_end + butt3_right_end)/2 + menu_x - 320, butt3_y - butt3_radius],\
            [(butt3_left_end + butt3_right_end)/2 + menu_x - 320, butt3_y + butt3_radius - 1])

        pygame.draw.circle(screen, WHITE, (butt3_x + menu_x - 320, butt3_y), butt3_radius)
        if butt3_num == 0:
            pygame.draw.circle(screen, GRAY, (butt3_x + menu_x - 320, butt3_y), butt3_radius - 3)
        if butt3_num == 1:
            pygame.draw.circle(screen, GRAY, (butt3_x + menu_x - 320, butt3_y), butt3_radius, 3)

        butt3_value = (butt3_x - butt3_left_end)/(butt3_right_end - butt3_left_end)*500
        butt3_value_text = menu_font.render("WIDTH | " + str(round(butt3_value, 1)), True, BLACK)
        butt3_value_rect = butt3_value_text.get_rect(topleft = (butt3_left_end + menu_x - 320, butt3_y - butt3_radius - 20))
        screen.blit(butt3_value_text, butt3_value_rect)

        width = butt3_value

##################################################

        # FOV 버튼 5
        if butt5_num == 1:
            butt5_x = pygame.mouse.get_pos()[0]
            if butt5_x < butt5_left_end:
                butt5_x = butt5_left_end
            elif butt5_x > butt5_right_end:
                butt5_x = butt5_right_end

        pygame.draw.circle(screen, RECT_GRAY, (butt5_left_end + menu_x - 320, butt5_y), butt5_radius + 3) # 아웃라인
        pygame.draw.circle(screen, RECT_GRAY, (butt5_right_end + menu_x - 320, butt5_y), butt5_radius + 3)
        pygame.draw.rect(screen, RECT_GRAY, (butt5_left_end + menu_x - 320, butt5_y - butt5_radius, butt5_right_end - butt5_left_end, 2*butt5_radius), 7)
        pygame.draw.circle(screen, BEIGE, (butt5_left_end + menu_x - 320, butt5_y), butt5_radius) # 배경
        pygame.draw.circle(screen, BEIGE, (butt5_right_end + menu_x - 320, butt5_y), butt5_radius)
        pygame.draw.rect(screen, BEIGE, (butt5_left_end + menu_x - 320, butt5_y - butt5_radius, butt5_right_end - butt5_left_end, 2*butt5_radius))
        pygame.draw.line(screen, RECT_GRAY, [(butt5_left_end + butt5_right_end)/2 + menu_x - 320, butt5_y - butt5_radius],\
            [(butt5_left_end + butt5_right_end)/2 + menu_x - 320, butt5_y + butt5_radius - 1])

        pygame.draw.circle(screen, WHITE, (butt5_x + menu_x - 320, butt5_y), butt5_radius)
        if butt5_num == 0:
            pygame.draw.circle(screen, GRAY, (butt5_x + menu_x - 320, butt5_y), butt5_radius - 3)
        if butt5_num == 1:
            pygame.draw.circle(screen, GRAY, (butt5_x + menu_x - 320, butt5_y), butt5_radius, 3)

        butt5_value = (butt5_x - butt5_left_end)/(butt5_right_end - butt5_left_end)*100 + 1
        butt5_value_text = menu_font.render("FOV | " + str(round(butt5_value, 1)), True, BLACK)
        butt5_value_rect = butt5_value_text.get_rect(topleft = (butt5_left_end + menu_x - 320, butt5_y - butt5_radius - 20))
        screen.blit(butt5_value_text, butt5_value_rect)

        radius = butt5_value

##################################################

        # height 버튼 4
        if butt4_num == 1:
            butt4_x = pygame.mouse.get_pos()[0]
            if butt4_x < butt4_left_end:
                butt4_x = butt4_left_end
            elif butt4_x > butt4_right_end:
                butt4_x = butt4_right_end

        pygame.draw.circle(screen, RECT_GRAY, (butt4_left_end + menu_x - 320, butt4_y), butt4_radius + 3) # 아웃라인
        pygame.draw.circle(screen, RECT_GRAY, (butt4_right_end + menu_x - 320, butt4_y), butt4_radius + 3)
        pygame.draw.rect(screen, RECT_GRAY, (butt4_left_end + menu_x - 320, butt4_y - butt4_radius, butt4_right_end - butt4_left_end, 2*butt4_radius), 7)
        pygame.draw.circle(screen, BEIGE, (butt4_left_end + menu_x - 320, butt4_y), butt4_radius) # 배경
        pygame.draw.circle(screen, BEIGE, (butt4_right_end + menu_x - 320, butt4_y), butt4_radius)
        pygame.draw.rect(screen, BEIGE, (butt4_left_end + menu_x - 320, butt4_y - butt4_radius, butt4_right_end - butt4_left_end, 2*butt4_radius))
        pygame.draw.line(screen, RECT_GRAY, [(butt4_left_end + butt4_right_end)/2 + menu_x - 320, butt4_y - butt4_radius],\
            [(butt4_left_end + butt4_right_end)/2 + menu_x - 320, butt4_y + butt4_radius - 1])

        pygame.draw.circle(screen, WHITE, (butt4_x + menu_x - 320, butt4_y), butt4_radius)
        if butt4_num == 0:
            pygame.draw.circle(screen, GRAY, (butt4_x + menu_x - 320, butt4_y), butt4_radius - 3)
        if butt4_num == 1:
            pygame.draw.circle(screen, GRAY, (butt4_x + menu_x - 320, butt4_y), butt4_radius, 3)

        butt4_value = (butt4_x - butt4_left_end)/(butt4_right_end - butt4_left_end)*500
        butt4_value_text = menu_font.render("HEIGHT | " + str(round(butt4_value)), True, BLACK)
        butt4_value_rect = butt4_value_text.get_rect(topleft = (butt4_left_end + menu_x - 320, butt4_y - butt5_radius - 20))
        screen.blit(butt4_value_text, butt4_value_rect)

        ratio = butt4_value / radius

##################################################

    game_text = logo_font.render("Spinning_Rect", True, rotated_GRAY)
    game_rect = game_text.get_rect(topleft = (10, 10))
    screen.blit(game_text, game_rect)

    pygame.display.update()

pygame.quit()