import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
pygame.display.flip()

blue=(0,0,255)
def bresenham_line(x1,y1,x2,y2):
	x,y = x1,y1
	dx = float(x2 - x1)
	dy = float(y2 - y1)
	pk = 2*float(dy) - dx
	p = pk
	m = dy/float(dx)
	if m<=1:
		while y <= y2 or x <= x2:
			yk = y
			x = x + 1
			if pk >= 0:
				y = y + 1
			gfxdraw.pixel(screen,round(x),round(y),blue)
			pk = p
			p = pk + 2*dy - 2*dx*(y-yk)
	elif m>1:
		while y <= y2 or x <= x2:
			xk = x
			y = y + 1
			if pk >= 0:
				x = x + 1
			gfxdraw.pixel(screen,round(x),round(y),blue)
			pk = p
			p = pk + 2*dx - 2*dy*(x-xk)


	pygame.display.flip()

bresenham_line(300,200,500,400)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()