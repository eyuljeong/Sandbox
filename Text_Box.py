import pygame

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Text_Box")
# icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\SandBox\\Butt_On_icon.png")
# pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont("consolas", 30)

# 색 상수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
P_BLUE = (147, 214, 237)
BEIGE = (245, 245, 220)
BEIGE2 = (215, 215, 190)

##################################################

text_box_pos = [200, 200, 240, 40]
text_box_num = 0
text = ""

backspace_num = 0
backspace_int = 0

##################################################

running = True
while running:
    dt = clock.tick(60)
    screen.fill(P_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_box_pos[0] < mouse[0] < text_box_pos[0] + text_box_pos[2] and\
            text_box_pos[1] < mouse[1] < text_box_pos[1] + text_box_pos[3]:
                text_box_num = 1
            else:
                text_box_num = 0

        if event.type == pygame.KEYDOWN:
            if text_box_num == 1:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    backspace_num = 1
                    start_ticks = pygame.time.get_ticks()
                else:
                    text += event.unicode

        if event.type == pygame.KEYUP:
            backspace_num = 0


    mouse = pygame.mouse.get_pos()

    if backspace_num == 1:
        backspace_int += 1
        pressed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if 0.5 <= pressed_time <= 1.5:
            if backspace_int % 9 == 0:
                text = text[:-1]
        elif pressed_time > 1.5:
            if backspace_int % 3 == 0:
                text = text[:-1]

##################################################

    if text_box_num == 0:
        pygame.draw.rect(screen, BEIGE, text_box_pos)
    elif text_box_num == 1:
        pygame.draw.rect(screen, BEIGE2, text_box_pos)
    pygame.draw.rect(screen, WHITE, text_box_pos, 2)

    text_text = game_font.render(text, True, BLACK)
    text_rect = text_text.get_rect(bottomleft = (text_box_pos[0] + 5, text_box_pos[1] + text_box_pos[3] - 5))
    screen.blit(text_text, text_rect)

    pygame.display.update()

pygame.quit()