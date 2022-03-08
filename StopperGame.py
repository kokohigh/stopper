import pygame,sys

pygame.init()
size = width,height = 800, 600
bg_color = 153, 255, 255
speed = [0, 0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("stopper")
ball = pygame.image.load("images/ball0.bmp")
ballrect = ball.get_rect()
fps = 200
fclock = pygame.time.Clock()
still =False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #这里是退出的功能
            sys.exit()
        elif event.type == pygame.KEYDOWN: #这里是加减速
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0] - 1 if speed[0] < 0 else speed[0] + 1
            if event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            if event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if speed[0] == 0 and speed[1] == 0:
                    ballrect = ballrect.move(80,80)
                elif speed[0] != 0 and speed[1] != 0:
                    ballrect = ballrect.move((speed[0]/abs(speed[0]))*80 + speed[0] * 20,(speed[1]/abs(speed[1]))*80 + speed[1] * 20)
                elif speed[0] == 0 and speed[1] != 0:
                    ballrect = ballrect.move(80, (speed[1]/abs(speed[1]))*80 + speed[1] * 20)
                elif speed[0] != 0 and speed[1] == 0:
                    ballrect = ballrect.move((speed[0]/abs(speed[0]))*80 + speed[0] * 20,80)


    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = -speed[0]
        if ballrect.left < 0  and ballrect.left + speed[0] < ballrect.left:
            speed[0] = -speed[0]


    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
                speed[1] = -speed[1]
        if ballrect.top < 0 and ballrect.top + speed[1] < ballrect.top:
                speed[1] = -speed[1]


    screen.fill(bg_color)
    screen.blit(ball,ballrect)
    ballrect = ballrect.move(speed)
    pygame.display.update()
    fclock.tick(fps)

