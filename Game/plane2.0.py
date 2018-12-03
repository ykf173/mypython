import pygame
import time
import random
from pygame.locals import *

isBoom = 0

class MyPlane:

    def __init__(self, screen):
        self.x = 230
        self.y = 570
        self.screen = screen
        self.bulletList = []
        self.delBulletList = []
        self.imageName = "./feiji/hero1.png"

        self.image = pygame.image.load(self.imageName)

    def disPlay(self):

        self.screen.blit(self.image, (self.x, self.y))
        #print(self.bulletList)
        for bullet in self.bulletList:

            if bullet.judge():

                self.delBulletList.append(bullet)
            else:
                bullet.disPlay()
                bullet.move()

        for i in self.delBulletList:

            self.delBulletList.remove(i)
    def moveLeft(self):

        self.x -= 10

    def moveRight(self):

        self.x += 10

    def moveUp(self):

        self.y -= 10

    def moveDown(self):

        self.y += 10

    def check_control(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:

                key_pressed = pygame.key.get_pressed()

                if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                    print("left")
                    if self.x > 0:
                        self.moveLeft()

                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    if self.x < 380:
                        self.moveRight()

                elif event.key == K_w or event.key == K_UP:
                    print('up')
                    if self.y > 0:
                        self.moveUp()

                elif event.key == K_s or event.key == K_DOWN:
                    print('down')
                    if self.y < 576:
                        self.moveDown()

                elif event.key == K_SPACE:
                    print('space')
                    self.bullet()

    def bullet(self):
        newBullet  = Bullet(self.x + 40, self.y - 20, self.screen, "./feiji/bullet.png")

        self.bulletList.append(newBullet)

class Bullet:

    def __init__(self, x, y, screen, img):

        self.x = x
        self.y = y
        self.screen = screen
        self.img = pygame.image.load(img)

    def move(self):

        self.y -= 10

    def enemyMove(self):

        self.y += 2

    def jizhongEnemy(self, enemy):

        if enemy.x < self.x and self.x < enemy.y + 69:

            if enemy.y < self.y < enemy.y + 89:

                print("击中敌机")
                return True
        else:

            return False

    def judge(self):

        if self.y < 0:
            return True
        else:
            return False

    def enemyJudge(self):

        if self.y > 700:
            return True
        else:
            return False

    def disPlay(self):

        self.screen.blit(self.img, (self.x, self.y))

#显示敌机
class EnemyPlane:

    def __init__(self, x, y, screen):

        self.x = x
        self.y = y
        self.num = 0
        self.screen = screen
        self.direction = "right"
        self.boomImg = []
        self.image_num = 0
        self.image_index = 0
        self.imgLen = 0
        self.isBoom = False
        self.image = pygame.image.load("./feiji/enemy1.png")
        self.bulletList = []
        self.delBulletList = []

    def is_boom(self, isBoom):

        self.isBoom = isBoom

    def load_boom_image(self):

        for i in range(4):

            img = "./feiji/enemy" + i + "_down" + i + ".png"

            self.boomImg.append(img)

        self.imgLen = len(self.boomImg)

    def display(self):

        if self.isBoom:
            print("2")
            bomb_image = self.boomImg[self.image_index]
            self.screen.blit(bomb_image, (self.x, self.y))
            self.image_num += 1
            if self.image_num == (self.imgLen + 1):
                self.image_num = 0
                self.image_index += 1

                if self.image_index > (self.imgLen - 1):
                    self.image_index = 5
                    time.sleep(2)
        else:

            self.screen.blit(self.image, (self.x, self.y))
            hero = MyPlane(self.screen)
            #print(hero.bulletList)
            for bullet in hero.bulletList:
                print("3")
                if bullet.jizhongEnemy(self):
                    print("1")
                    self.isBoom = True

        for bullet in self.bulletList:

            if bullet.enemyJudge():

                self.delBulletList.append(bullet)
            else:
                bullet.disPlay()

                bullet.enemyMove()

        for i in self.delBulletList:

            self.delBulletList.remove(i)

    def move(self):

        if self.direction == "right":

            self.x += 1.5

        if self.direction == "left":

            self.x -= 1.5

        if self.x > 410:

            self.direction = "left"

        if self.x < 0:

            self.direction = "right"

    def bullet(self):

        num = random.randint(1, 80)

        if num == 20:
            enemyBullet = Bullet(self.x + 34, self.y + 89, self.screen, "./feiji/bullet1.png")

            self.bulletList.append(enemyBullet)

def main():

    screen = pygame.display.set_mode((480, 700), 0, 32)

    background = pygame.image.load("./feiji/background.png")

    hero = MyPlane(screen)

    enemy = EnemyPlane(0, 0, screen)

    while True:

        screen.blit(background, (0, 0))

        enemy.display()
        enemy.move()
        enemy.bullet()
        hero.disPlay()

        hero.check_control()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":

    main()


