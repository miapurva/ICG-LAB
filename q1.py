#Submission by Yutika Kulwe, CED15I017, IIITDM Kancheepuram
import sys,pygame
from pygame import gfxdraw
import  math
pygame.init()
screen = pygame.display.set_mode((1200,700))
screen.fill((255,255,255))
pygame.display.flip()
#colors
saffron=(250,153,7)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)

offset =60
for i in range(0,5):
	for j in range(0,20):
		pygame.draw.circle(screen,black,(30+offset*j,30+offset*i),30,3)


pygame.display.flip()

running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()    

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
