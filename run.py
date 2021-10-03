import pygame
import random
import time
import os
os.chdir("/home/ameena/Documents/python/run")

box_1s = 5
box_2s = 10
score = 1
life = 1
yellow = 255, 255, 102
high_score = 0
flag = True
with open('high_score.txt', 'r') as file:
    high_score = int(file.read())

pygame.init()
win =  pygame.display.set_mode((500,500))
pygame.display.set_caption("maze_game")

class create_character:
    def __init__(self,image_fname,x,y,):
        self.image = pygame.image.load(image_fname)
        self.image_mask = pygame.mask.from_surface(self.image, 50)
        self.x = x
        self.y = y
    def image_blit(self,):
        win.blit(self.image,(self.x, self.y))

    def check_hit(self,target):
        offset_x = self.x - target.x
        offset_y = self.y - target.y
        overlap = target.image_mask.overlap(self.image_mask, (offset_x, offset_y))
        return overlap
def text_show(text, font_size, x, y, color = yellow):
    text_font = pygame.font.Font('OtomanopeeOne-Regular.ttf', font_size)
    textSurface = text_font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    win.blit(textSurface, textRect)

box_1 = create_character("box_1.png", 220,450)
box_b = create_character("box_b.png", 190,400)
box_2 = create_character("box_2.png", 0,random.randint(100,350))
box_2r = create_character("box_2.png", 480,random.randint(100,350))
home = create_character("home.png", 150,0)
        

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == False      : 
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_SPACE] and flag == True:
        box_1.y = box_1.y - box_1s
    if box_1.y < 90:
        box_1.y = 450
        score = score + 1
        life = life + 1
    if flag == True:
        box_2.x = box_2.x + box_2s
    if box_2.x > 500:
        box_2.x = 0
        box_2.y = random.randint(100,350)
    
    if flag == True:
        box_2r.x = box_2r.x - box_2s
    if box_2r.x < 10:
        box_2r.x = 480
        box_2r.y = random.randint(100,350)

    if box_1.check_hit(box_2):
        life = life - 3
        box_1.y = 450
    if box_1.check_hit(box_2r):
        life = life - 3
        box_1.y = 450

    if keys [pygame.K_b]:
        flag = True
        score = 1
        life = 1
        box_2r.x = 480
        box_2r.y = random.randint(100,350)
        box_2.x = 0
        box_2.y = random.randint(100,350)
        box_1.y = 450

    win.fill((0,0,15))
    box_1.image_blit()
    box_b.image_blit()
    box_2.image_blit()
    box_2r.image_blit()
    home.image_blit()
    if score > high_score:
        high_score = score
        with open('high_score.txt', 'w') as file:
            file.write(str(high_score))
    if life < 1:
        life = 0
        flag = False    
        text_show("GAME OVER", 50, 250, 250)
        text_show("up arrow : start game", 20, 250, 180)
        text_show(f"High Score: {str(high_score)}", 20, 250, 320)
    text_show(f"Score : {score}", 15, 60, 20)
    text_show(f"life : {life}", 15, 60, 50)
    pygame.display.update()
    print(pygame.mouse.get_pos())
    print(score)
pygame.quit
    