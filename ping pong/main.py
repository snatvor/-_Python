from pygame import *
from random import *
from time import sleep
game = True
finish = True
speed_x = 3
speed_y = 3
#Создание изображения
wd = display.set_mode((800,600))
background =transform.scale(image.load('galaxy.jpg'),(800,600))
platform = transform.scale(image.load('Стена.jfif'),(25,300))
ball = transform.scale(image.load('ball2.png'),(40,40))
# Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = player_image
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'right'
    def reset(self):
        wd.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 5:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed          
class Ball(GameSprite):
    pass
wall_1 = Player(platform,30,150,10)
wall_2 = Player(platform,730,150,10)
ball_rl =Ball(ball,400,300,5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
    if not finish:
        wd.blit(background,(0,0))
        #update
        wall_1.update()
        wall_2.update()
        ball_rl.update()
        #reset
        wall_1.reset()
        wall_2.reset()
        ball_rl.reset()
        #Движение мяча
        ball_rl.rect.x += speed_x
        ball_rl.rect.y += speed_y
        if ball_rl.rect.y > 550 or ball_rl.rect.y < 0 :
            speed_y *= -1
        if sprite.collide_rect(wall_1,ball_rl) or sprite.collide_rect(wall_2,ball_rl):
            speed_x *= -1
        display.update()