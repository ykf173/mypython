import pygame
import time
from pygame.locals import *

def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    #自己的飞机
    myplane = pygame.image.load("./feiji/hero1.png")

    #x,y是自己飞机的坐标
    x = 0
    y = 0

    # 3. 把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))

        #显示自己的飞机
        screen.blit(myplane, (x, y))
        #获取事件
        for event in pygame.event.get():

            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:

                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x -= 10

                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 10

                elif event.key== K_w or event.key == K_UP:
                    print('up')
                    y -= 10

                elif event.key == K_s or event.key == K_DOWN:
                    print('down')
                    y += 10

                elif event.key == K_SPACE:
                    print('space')


        # 更新需要显示的内容
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":

    main()

