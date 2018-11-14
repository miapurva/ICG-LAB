import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
pygame.display.flip()

blue=(0,0,255)

def draw_circle(xc,yc,x,y):
	gfxdraw.pixel(screen,round(xc+x),round(yc+y),blue)
	gfxdraw.pixel(screen,round(xc-x),round(yc+y),blue)
	gfxdraw.pixel(screen,round(xc+x),round(yc-y),blue)
	gfxdraw.pixel(screen,round(xc-x),round(yc-y),blue)
	gfxdraw.pixel(screen,round(xc+y),round(yc+x),blue)
	gfxdraw.pixel(screen,round(xc-y),round(yc+x),blue)
	gfxdraw.pixel(screen,round(xc+y),round(yc-x),blue)
	gfxdraw.pixel(screen,round(xc-y),round(yc-x),blue)

def bresenham_circle(xc,yc,r):
	d = 3 - (2 * r)
	x = 0
	y = r
	while x <= y:
		draw_circle(xc,yc,x,y)
		x = x + 1
		if d <= 0:
			d = d + (4 * x) + 6
		else:
			y = y - 1
			d = d + 4 * (x - y) + 10
		draw_circle(xc,yc,x,y)

	pygame.display.flip()

bresenham_circle(400,300,200)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()