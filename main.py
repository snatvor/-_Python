from pygame import *
from random import *
from time import sleep
game = True
finish = False
#Создание изображения
wd = display.set_mode((800,600))
background =transform.scale(image.load('galaxy.jpg'),(800,600))
platform = transform.scale(image.load('Стена.jfif'),(10,150))
ball = transform.scale(image.load('ball.png'),(30,30))
# Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'right'
    def reset(self):
        wd.blit(self.image,(self.rect.x,self.rect.y))
class platform_1(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 5:
            self.rect.y += self.speed
class platform_2(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed
class Ball(GameSprite):
    pass
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    wd.blit(background,(0,0))
    display.update()