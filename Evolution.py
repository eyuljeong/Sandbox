import pygame
from random import *

# 초기화
pygame.init()

# 화면 크기
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Evolution")

# FPS
clock = pygame.time.Clock()

# 폰트
Title_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
game_font = pygame.font.Font(None, 25) # 폰트 객체 생성 (폰트, 크기)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
P_BLUE = (147, 214, 237)
RED = (255, 0, 0)

tilesize = 40
tilenumber = 3

size = 7
life = 25
death = 2
initbirthrate = 0.8
birthrate = 0.5
birthrestrict = 0.6

entity_list= []
time = 0

##################################################

class Dots():
    def __init__(self, loc, life, color, leaping):
        self.loc = loc
        self.life = life
        self.color = color
        self.leaping = leaping


    def move(self):
        num = randrange(4)
        if num == 0:
            if self.loc[0] + self.leaping > tilenumber:
                self.loc[0] = tilenumber
            else:
                self.loc[0] = self.loc[0] + self.leaping
        if num == 1:
            if self.loc[0] - self.leaping < 0:
                self.loc[0] = 0
            else:
                self.loc[0] = self.loc[0] - self.leaping
        if num == 2:
            if self.loc[1] + self.leaping > tilenumber:
                self.loc[1] = tilenumber
            else:
                self.loc[1] = self.loc[1] + self.leaping
        if num == 3:
            if self.loc[1] - self.leaping < 0:
                self.loc[1] = 0
            else:
                self.loc[1] = self.loc[1] - self.leaping

    def draw(self):
        pygame.draw.circle(screen, self.color, \
        [screen_width/2 - tilesize*(tilenumber/2-self.loc[0]), screen_height/2 - tilesize*(tilenumber/2-self.loc[1])], size)

for m in range(0, tilenumber):
    for n in range(0, tilenumber):
        if random() > initbirthrate:
            if random() > 0.5:
                entity_list.append(Dots([m, n], life, WHITE, 1))
            else:
                entity_list.append(Dots([m, n], life, RED, 2))
##################################################

# 이벤트 루프
running = True
while running:
    clock.tick(60)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_width/2 + tilesize*tilenumber/2 + 10 < mouse[0] < screen_width/2 + tilesize*tilenumber/2 + 110\
                and screen_height/2 + tilesize*tilenumber/2 - 100 < mouse[1] < screen_height/2 + tilesize*tilenumber/2:
                for entt in entity_list:
                    entt.life = entt.life - death
                    if entt.life <= 0:
                        entity_list.remove(entt)
                    
                    entt.move()
                    
                i = len(entity_list)
                for m in range(i - 1):
                    for n in range(m + 1, i):
                        if entity_list[m].loc == entity_list[n].loc and random() > birthrate and len(entity_list) < tilenumber*tilenumber*birthrestrict:
                            if entity_list[m].color == RED and entity_list[n].color == RED:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                entity_list.append(Dots([x, y], life, RED, 2))

                            if entity_list[m].color == RED and entity_list[n].color == WHITE:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                if random() > 0.5:
                                    entity_list.append(Dots([x, y], life, RED, 2))
                                else:
                                    entity_list.append(Dots([x, y], life, WHITE, 1))
                            if entity_list[m].color == WHITE and entity_list[n].color == WHITE:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                entity_list.append(Dots([x, y], life, RED, 2))

            time += 1

##################################################

    screen.fill(BLACK)

    # world_time 버튼
    pygame.draw.rect(screen, WHITE, [screen_width/2 + tilesize*tilenumber/2 + 10, screen_height/2 + tilesize*tilenumber/2 - 100, 100, 100], 2)

    # 그리드
    for m in range(0, tilesize*tilenumber + 1, tilesize):
        pygame.draw.line(screen, WHITE, [screen_width/2 - tilesize*tilenumber/2 + m, screen_height/2 - tilesize*tilenumber/2], [screen_width/2 - tilesize*tilenumber/2 + m, screen_height/2 + tilesize*tilenumber/2], 1)
    for n in range(0, tilesize*tilenumber + 1, tilesize):
        pygame.draw.line(screen, WHITE, [screen_width/2 - tilesize*tilenumber/2, screen_height/2 - tilesize*tilenumber/2 + n], [screen_width/2 + tilesize*tilenumber/2, screen_height/2 - tilesize*tilenumber/2 + n], 1)

    # 개체
    for entt in entity_list:
        if entt.life > 0:
            entt.draw()

##################################################

    Title_text = Title_font.render("Evolution", True, WHITE)
    Title_rect = Title_text.get_rect(topleft = (60, 60))
    screen.blit(Title_text, Title_rect)

    pygame.draw.line(screen, RED, [60, 90], [90, 90], 2)

    line_text = game_font.render("Tile_Number = {0}".format(tilenumber), True, WHITE)
    line_rect = line_text.get_rect(topleft = (60, 110))
    screen.blit(line_text, line_rect)

    line_text = game_font.render("Tile_Size = {0}".format(tilesize), True, WHITE)
    line_rect = line_text.get_rect(topleft = (60, 135))
    screen.blit(line_text, line_rect)

    line_text = game_font.render("Life = {0}".format(life), True, WHITE)
    line_rect = line_text.get_rect(topleft = (60, 160))
    screen.blit(line_text, line_rect)

    line_text = game_font.render("Death = {0}".format(death), True, WHITE)
    line_rect = line_text.get_rect(topleft = (60, 185))
    screen.blit(line_text, line_rect)

    white = 0
    red = 0
    for entt in entity_list:
        if entt.color == WHITE:
            white += 1
        elif entt.color == RED:
            red += 1

    line_text = game_font.render("White : Red = {0} : {1}".format(white, red), True, WHITE)
    line_rect = line_text.get_rect(topleft = (screen_width/2 + tilesize*tilenumber/2 + 10, screen_height/2 + tilesize*tilenumber/2 - 130))
    screen.blit(line_text, line_rect)     

    line_text = game_font.render("{0} year".format(time), True, WHITE)
    line_rect = line_text.get_rect(topleft = (screen_width/2 + tilesize*tilenumber/2 + 10, screen_height/2 + tilesize*tilenumber/2 - 160))
    screen.blit(line_text, line_rect) 

##################################################

    pygame.display.update() # 화면 다시 그리기

# 종료
pygame.quit()

##################################################

# 결론 : 빨간 개체가 흰 개체보다 생존에 있어서 우월하다.
# 이유 : 활동력이 높다는 것은 상대적으로 공간이 작아지는 것이다. 따라서 인구밀도 높아지고, 번식에 유리한 것이다.

