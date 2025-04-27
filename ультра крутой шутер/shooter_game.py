#Создай собственный Шутер!
from pygame import *
from random import *
from time import sleep
h = 0
g = 0
surv = 3
# clock = time.Clock()
# fps = 10
sp_r = random
run = True
finish = False
wd = display.set_mode((800,600))
display.set_caption('Лабbринт')
background =transform.scale(image.load('galaxy.jpg'),(800,600))
player = transform.scale(image.load('rocket.png'),(10,20))
ufo =transform.scale(image.load('ufo.png'),(790,690))
bullet = transform.scale(image.load('bullet.png'),(5,10))
asteroid = transform.scale(image.load('asteroid.png'),(790,690))
# 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound =mixer.Sound('fire.ogg')
void = mixer.Sound('space.ogg')
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
bullets = sprite.Group()
class Rocket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        eys_pressed = key.get_pressed()
        if keys_pressed[K_a] and  self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and  self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and  self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and  self.rect.y < 450:
            self.rect.x += self.speed 
    def fire(self):
        Bul = bullet('bullet.png',self.rect.centerx,self.rect.top,15)
        bullets.add(Bul)
class Enemy(GameSprite):
    def update(self):
        global h 
        if self.rect.y >= 600:   
            self.rect.x = randint(0,600)
            self.rect.y = 0
            h += 1
        if self.rect.y <= 600:
            self.rect.y += self.speed  

class bullet(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image),(10,10))
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png',randint(0,600),1,3)
    monsters.add(enemy)
R = Rocket('rocket.png',400,490,10)
font.init()
font1 = font.Font(None,36)
while run:
    void.play()
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif g >=200:
            wd.blit(text_line3,(400,300))
            finish = True
        elif h >=15:
            finish = True
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                R.fire()
                fire_sound.play()
    if not finish:
        wd.blit(background,(0,0))
        R.update()
        sprites_list = sprite.groupcollide(monsters,bullets,True,True)
        for c in sprites_list:
            g += 1
            enemy = Enemy('ufo.png',randint(0,600),1,3)
            monsters.add(enemy)
        text_line =font1.render('Пропущено:'+str(h),1,(230,200,1))
        text_line2 =font1.render('Счёт:'+str(g),1,(230,200,1))
        text_line3 = font1.render('Ты выйграл',1,(200,200,1))
        monsters.update()
        bullets.update()
        wd.blit(text_line,(100,100))
        wd.blit(text_line2,(100,80))
        bullets.draw(wd)
        R.reset()
        monsters.draw(wd)
        # clock.tick(fps)
        time.delay(5)
        display.update()
    else:
        wd.blit(text_line3,(400,300))
        finish = False
        h = 0
        g = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()

        sleep(4)
        
        for i in range(1, 6):
            monster = Enemy('ufo.png', randint(80, 700 - 80), -40, randint(3, 5))
            monsters.add(monster)
