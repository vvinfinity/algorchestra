#Create your own shooter


from random import randint
import pygame as gm

class GameSprite(gm.sprite.Sprite):
    def __init__(self, img, x, y, weidth, height, speed):
        gm.sprite.Sprite.__init__(self)
        self.img = gm.transform.scale(gm.image.load(img), (weidth, height))
        self.image = gm.transform.scale(gm.image.load(img), (weidth, height))
        self.speed = speed

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        w.blit(self.img, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys = gm.key.get_pressed()
        if keys[gm.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[gm.K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def shoot(self):
        bullet = fire("bullet.png", self.rect.centerx, self.rect.top , 15, 20, -10)
        bulletss.add(bullet)


class enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint( 80, 620)
            self.rect.y = 0
            lost += 1

class fire(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()





rocket = player("rocket.png", 5, 400, 80, 100, 10)       
obstacle = gm.sprite.Group()
for i in range(1, 6):
    monsters = enemy("ufo.png", randint(80, 620), 0, 80, 50, randint(1, 3))
    obstacle.add(monsters)

score = 0
lost = 0

class enemy(GameSprite):
       def update(self):
           self.rect.y += self.speed
           global lost


gm.init()
w = gm.display.set_mode((700, 500))
gm.display.set_caption("SHOOOOOt")
bg = gm.transform.scale(gm.image.load("galaxy.jpg"), (700, 500))



fps = gm.time.Clock()

bulletss = gm.sprite.Group()
gm.font.init()
f1 = gm.font.Font(None, 80)
win = f1.render("MISSION COMPLETEd", True, (15, 255, 255))
lose = f1.render("Looose", True, (180, 0, 0))



gm.mixer.init()
gm.mixer.music.load("fire.ogg")
gm.mixer.music.set_volume(0.5)
gm.mixer.music.play(loops=True)
finish = False
score = 0
while True:
    for e in gm.event.get():
        if e.type == gm.QUIT:
            break
        elif e.type == gm.KEYDOWN:
            if e.key == gm.K_SPACE:
                s = gm.mixer.Sound("fire.ogg")
                s.play()
                rocket.shoot()

    if not finish:
        w.blit(bg, (0,0))
        rocket.update()
        obstacle.update()
        rocket.reset()
        obstacle.draw(w)
        bulletss.update()
        bulletss.draw(w)
        font2 = gm.font.Font(None, 36)
        missed = font2.render(f"Missed: {lost}", 1, gm.Color("White"))
        w.blit(missed, (10, 50))
        scored = font2.render(f"Scored: {score}", 1, gm.Color("White"))
        w.blit(scored, (10, 20))
        colides = gm.sprite.groupcollide(obstacle, bulletss, True, True)
        for c in colides:
            score += 1
            monster = enemy("ufo.png", randint(80, 620), 0, 80, 50, randint(1,5))
            monsters.add(obstacle)
        
        if gm.sprite.spritecollide(rocket, obstacle, False) or lost >= 5:
            finish = True
            game = "lose"
        if score >= 5:
            finish = True
            game = "win"
    else:
        if game == "win":
            w.blit(win, (50, 200))
        else:
            w.blit(lose, (200, 200))


    gm.display.update()
    fps.tick(60)