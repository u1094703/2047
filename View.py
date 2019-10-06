import pygame
pygame.init()
pygame.display.set_caption("2047")
background=pygame.image.load('/Users/Krish/Desktop/color.jpg')

screen = pygame.display.set_mode((400,400))

pygame.display.update()
isBlue=True
done=False
while not done:
    screen.blit(background, (400, 400))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True