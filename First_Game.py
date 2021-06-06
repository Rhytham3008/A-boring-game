
import pygame
pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game")

x = 100
y = 50
width = 55
height = 45
vel = 25

play = True

while play:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y = y - vel
    if keys[pygame.K_LEFT]:
        x = x - vel

    if keys[pygame.K_RIGHT]:
        x = x + vel

    if keys[pygame.K_DOWN]:
        y = y + vel
        
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0),(x, y, width, height))
    pygame.display.update()

pygame.quit()
