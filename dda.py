import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
pygame.display.flip()

blue=(0,0,255)

def dda(x1,y1,x2,y2):
	x,y = x1,y1
	m = (y2 - y1)/float(x2 - x1)
	while y <= y2 :
		gfxdraw.pixel(screen,round(x),round(y),blue)
		x = x + 1
		y = y + m
	pygame.display.flip()

dda(300,200,500,400)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()