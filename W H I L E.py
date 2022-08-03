import pygame

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("W H I L E")
icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\SandBox\\W H I L E_icon.png")
pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 40)

# 색 상수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (6, 144, 255)
RED = (174, 25, 50)
GREEN = (6, 186, 0)

##################################################

# 좌표    0    1    2    3    4    5    6    7    8
line1 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 0
line2 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 1
line3 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 2
line4 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 3
line5 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 4
line6 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 5
line7 = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # 6
line_lst = [line1, line2, line3, line4, line5, line6, line7] # 윗줄부터 순서대로

class Coordinate:
    def __init__(self, name, location:list):
        self.name = name
        self.location = location
    
    # 배치
    def deploy(self):
        line_lst[self.location[1]].pop(self.location[0]) # O 빼기
        line_lst[self.location[1]].insert(self.location[0], self.name)

    # 삭제
    def delete(self):
        line_lst[self.location[1]].pop(self.location[0])
        line_lst[self.location[1]].insert(self.location[0], "O")

    # 움직임 = 삭제 + 배치
    def move(self, to_x, to_y):
        self.delete()
        self.location = [self.location[0] + to_x, self.location[1] + to_y]
        self.deploy()

    # 적 움직임
    def enemy_move(self, to_x, to_y):
        if self.location[0] < X.location[0]:
            to_x += 1
        elif self.location[0] > X.location[0]:
            to_x -= 1
        if self.location[1] < X.location[1]:
            to_y += 1
        elif self.location[1] > X.location[1]:
            to_y -= 1

        self.move(to_x, to_y)

# 변수
Xmove_x = 0
Xmove_y = 0
Ymove_x = 0
Ymove_y = 0
Yspeed_limit = 0
gameover_msg = "Game Over"
point = 0

##################################################

# 배치
X = Coordinate("X", [4, 3])
X.deploy()
Y = Coordinate("Y", [0, 0])
Y.deploy()
Z1 = Coordinate("Z", [8, 0])
Z1.deploy()
Z1.crash = 0
Z2 = Coordinate("Z", [0, 6])
Z2.deploy()
Z2.crash = 0
Z3 = Coordinate("Z", [8, 6])
Z3.deploy()
Z3.crash = 0

# 이벤트 루프
running = True
while running:
    dt = clock.tick(10) # fps

    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            running = False

        # 키보드 입력
        if event.type == pygame.KEYDOWN: # 누름
            if event.key == pygame.K_d:
                Xmove_x += 1
            elif event.key == pygame.K_a:
                Xmove_x -= 1
            elif event.key == pygame.K_w:
                Xmove_y -= 1
            elif event.key == pygame.K_s:
                Xmove_y += 1

        if event.type == pygame.KEYUP: # 뗌
            if event.key == pygame.K_d or event.key == pygame.K_a:
                Xmove_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                Xmove_y = 0

    # 경계값
    if 0<= X.location[0] + Xmove_x <= 8 and 0<= X.location[1] + Xmove_y <= 6:
        X.move(Xmove_x, Xmove_y)
        
    # 적 움직임
    Yspeed_limit += 1
    if Yspeed_limit % 10 == 0:
        Y.enemy_move(Ymove_x, Ymove_y)

    # 충돌처리
    if X.location == Y.location:
        Y = Coordinate("Y", [X.location[0], X.location[1]])
        Y.deploy()
        gameover_msg = "Terminated"
        running = False

    # 점수처리
    if X.location == Z1.location:
        if Z1.crash == 0:
            Z1.crash = 1
            point += 1
    elif X.location == Z2.location:
        if Z2.crash == 0:
            Z2.crash = 1
            point += 1
    elif X.location == Z3.location:
        if Z3.crash == 0:
            Z3.crash = 1
            point += 1
        
##################################################

    # 화면
    screen.fill((0, 0, 0))

    # 맵
    rect_x = 190
    rect_y = 140
    for line in line_lst:
        for alphabet in line:
            if alphabet == "X":
                COLOR = BLUE
            elif alphabet == "Y":
                COLOR = RED
            elif alphabet == "Z":
                COLOR = GREEN
            else:
                COLOR = WHITE
            alphabet_text = game_font.render(alphabet, True, COLOR)
            alphabet_rect = alphabet_text.get_rect(topleft = (rect_x, rect_y))
            screen.blit(alphabet_text, alphabet_rect)
            rect_x += 30
        rect_x = 190
        rect_y += 30

    # 점수
    point_text = game_font.render(str(point), True, BLUE)
    point_rect = point_text.get_rect(center = (screen_width / 2, 410))
    screen.blit(point_text, point_rect)

    pygame.display.update()

# 게임 오버
gameover_text = game_font.render(gameover_msg, True, RED)
gameover_rect = gameover_text.get_rect(center = (screen_width / 2, 70))
screen.blit(gameover_text, gameover_rect)

pygame.display.update()
pygame.time.delay(3000)
pygame.quit()