import pygame

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Butt_On")
icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\SandBox\\Butt_On_icon.png")
pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont(None, 30)

# 색 상수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (240, 240, 240)
P_BLUE = (147, 214, 237)
BEIGE = (245, 245, 220)

##################################################

# 버튼 1
butt1_x = 100
butt1_y = 100
butt1_width = 30
butt1_height = 30
butt1_num = 0

# 버튼 2
butt2_x = 195
butt2_y = 115
butt2_radius = 15
butt2_num = 0

# 버튼 3
butt3_x = 115
butt3_y = 175
butt3_radius = 15
butt3_num = 0
butt3_left_end = 115
butt3_right_end = 165

# 버튼 4
butt4_x = 295
butt4_y = 175
butt4_radius = 15
butt4_num = 0
butt4_left_end = 245
butt4_right_end = 345

butt4_auto_num = 0
butt4_auto_movex = 0
butt4_speed = 0.01

# 버튼 5
butt5_x = 275
butt5_y = 115
butt5_radius_start = 15
butt5_num = 0
butt5_bigger_time = 1/15
butt5_smaller_time = 1/5
butt5_ratio = 5/3

butt5_time = 0 # x
butt5_radius = 15 # y

##################################################

running = True
while running:
    dt = clock.tick(60)
    screen.fill(BEIGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 버튼 1
            if butt1_x <= mouse[0] <= butt1_x + butt1_width and butt1_y <= mouse[1] <= butt1_y + butt1_height:
                if butt1_num == 0:
                    butt1_num = 1
                elif butt1_num == 1:
                    butt1_num = 0

            # 버튼 2
            if (mouse[0] - butt2_x)**2 + (mouse[1] - butt2_y)**2 <= butt2_radius**2:
                if butt2_num == 0:
                    butt2_num = 1
                elif butt2_num == 1:
                    butt2_num = 0

            # 버튼 3
            if (mouse[0] - butt3_x)**2 + (mouse[1] - butt3_y)**2 <= butt3_radius**2:
                butt3_num = 1

            # 버튼 4
            if (mouse[0] - butt4_x)**2 + (mouse[1] - butt4_y)**2 <= butt4_radius**2:
                butt4_num = 1
            
            # 버튼 5
            if (mouse[0] - butt5_x)**2 + (mouse[1] - butt5_y)**2 <= butt5_radius**2:
                butt5_time = 0
                butt5_num = 1


        if event.type == pygame.MOUSEBUTTONUP:
            # 버튼 3
            butt3_num = 0

            # 버튼 4
            butt4_num = 0
            if butt4_left_end <= butt4_x <= (butt4_left_end + butt4_right_end)/2:
                butt4_auto_num = 1
            elif (butt4_left_end + butt4_right_end)/2 < butt4_x <= butt4_right_end:
                butt4_auto_num = 2

            # 버튼 5
            if butt5_num == 1:
                butt5_time = 0
                butt5_num = 2

    # 마우스
    mouse = pygame.mouse.get_pos()

##################################################

    # 버튼 1
    pygame.draw.rect(screen, P_BLUE, (butt1_x, butt1_y, butt1_width, butt1_height), 3)
    if butt1_num == 1:
        pygame.draw.rect(screen, P_BLUE, (butt1_x, butt1_y, butt1_width, butt1_height))

##################################################

    # 버튼 2
    pygame.draw.circle(screen, P_BLUE, (butt2_x, butt2_y), butt2_radius, 3)
    if butt2_num == 1:
        pygame.draw.circle(screen, P_BLUE, (butt2_x, butt2_y), butt2_radius)

##################################################

    # 버튼 3
    if butt3_num == 1:
        butt3_x = pygame.mouse.get_pos()[0]
        if butt3_x < butt3_left_end:
            butt3_x = butt3_left_end
        elif butt3_x > butt3_right_end:
            butt3_x = butt3_right_end

    pygame.draw.circle(screen, WHITE, (butt3_left_end, butt3_y), butt3_radius + 3) # 아웃라인
    pygame.draw.circle(screen, WHITE, (butt3_right_end, butt3_y), butt3_radius + 3)
    pygame.draw.rect(screen, WHITE, (butt3_left_end, butt3_y - butt3_radius, butt3_right_end - butt3_left_end, 2*butt3_radius), 7)
    pygame.draw.circle(screen, P_BLUE, (butt3_left_end, butt3_y), butt3_radius) # 배경
    pygame.draw.circle(screen, P_BLUE, (butt3_right_end, butt3_y), butt3_radius)
    pygame.draw.rect(screen, P_BLUE, (butt3_left_end, butt3_y - butt3_radius, butt3_right_end - butt3_left_end, 2*butt3_radius))
    
    pygame.draw.circle(screen, WHITE, (butt3_x, butt3_y), butt3_radius, 3)
    if butt3_num == 0:
        pygame.draw.circle(screen, WHITE, (butt3_x, butt3_y), butt3_radius)

##################################################

    # 버튼 4
    if butt4_num == 1:
        butt4_x = pygame.mouse.get_pos()[0]
        if butt4_x < butt4_left_end:
            butt4_x = butt4_left_end
        elif butt4_x > butt4_right_end:
            butt4_x = butt4_right_end
        butt4_auto_movex = 0

        # 자동 움직임
    if butt4_num == 0:
        if butt4_auto_num == 1:
            butt4_auto_movex -= butt4_speed * dt
            butt4_x += butt4_auto_movex
            if butt4_x < butt4_left_end:
                butt4_x = butt4_left_end
                butt4_auto_num = 0
                butt4_auto_movex = 0
        elif butt4_auto_num == 2:
            butt4_auto_movex += butt4_speed * dt
            butt4_x += butt4_auto_movex
            if butt4_x > butt4_right_end:
                butt4_x = butt4_right_end
                butt4_auto_num = 0
                butt4_auto_movex = 0

    pygame.draw.circle(screen, GRAY, (butt4_left_end, butt4_y), butt4_radius + 3) # 아웃라인
    pygame.draw.circle(screen, GRAY, (butt4_right_end, butt4_y), butt4_radius + 3)
    pygame.draw.rect(screen, GRAY, (butt4_left_end, butt4_y - butt4_radius, butt4_right_end - butt4_left_end, 2*butt4_radius), 7)
    pygame.draw.circle(screen, P_BLUE, (butt4_left_end, butt4_y), butt4_radius) # 배경
    pygame.draw.circle(screen, P_BLUE, (butt4_right_end, butt4_y), butt4_radius)
    pygame.draw.rect(screen, P_BLUE, (butt4_left_end, butt4_y - butt4_radius, butt4_right_end - butt4_left_end, 2*butt4_radius))
    pygame.draw.line(screen, GRAY, [(butt4_left_end + butt4_right_end)/2, butt4_y - butt4_radius], [(butt4_left_end + butt4_right_end)/2, butt4_y + butt4_radius - 1])

    pygame.draw.circle(screen, WHITE, (butt4_x, butt4_y), butt4_radius, 3)
    if butt4_num == 0:
        pygame.draw.circle(screen, WHITE, (butt4_x, butt4_y), butt4_radius)

##################################################

    # 버튼 5
    if butt5_num == 1:
        butt5_time += 0.01
        if butt5_time >= butt5_bigger_time:
            butt5_time = butt5_bigger_time
        butt5_radius = ((1 - butt5_ratio)*butt5_radius_start/butt5_bigger_time**2) * (butt5_time - butt5_bigger_time)**2 + butt5_ratio * butt5_radius_start
    elif butt5_num == 2:
        butt5_time += 0.01
        if butt5_time >= butt5_smaller_time:
            butt5_time = butt5_smaller_time
        butt5_radius = ((butt5_ratio - 1)*butt5_radius_start/butt5_smaller_time**2) * (butt5_time - butt5_smaller_time)**2 + butt5_radius_start

    pygame.draw.circle(screen, P_BLUE, (butt5_x, butt5_y), butt5_radius)
    pygame.draw.circle(screen, WHITE, (butt5_x, butt5_y), butt5_radius, 3)

    pygame.display.update()

pygame.quit()