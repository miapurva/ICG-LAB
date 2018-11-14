import sys,pygame
from pygame import gfxdraw
import  math
pygame.init()
screen = pygame.display.set_mode((1000,600))
screen.fill((255,255,255))

#colors
saffron=(250,153,7)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)

def start_position():
	#face
	pygame.draw.circle(screen,black,(500,150),60,5)
	pygame.draw.line(screen,black,(500,210),(500,380),5)
	#left leg
	pygame.draw.line(screen,black,(500,380),(410,500),5)
	pygame.draw.line(screen,black,(410,500),(380,500),5)
	#right leg
	pygame.draw.line(screen,black,(500,380),(590,500),5)
	pygame.draw.line(screen,black,(590,500),(620,500),5)
	
	#left hand
	pygame.draw.line(screen,black,(500,250),(440,250),5)
	pygame.draw.line(screen,black,(440,250),(400,300),5)
	#right hand
	pygame.draw.line(screen,black,(500,250),(560,250),5)
	pygame.draw.line(screen,black,(560,250),(520,300),5)

	pygame.display.flip()
	pygame.time.wait(500)
	screen.fill((255,255,255))
	
def mediate1():
	#face
	pygame.draw.circle(screen,black,(500,150),60,5)
	pygame.draw.line(screen,black,(500,210),(500,380),5)
	#left leg
	pygame.draw.line(screen,black,(500,380),(440,500),5)
	pygame.draw.line(screen,black,(440,500),(410,500),5)
	#right leg
	pygame.draw.line(screen,black,(500,380),(560,500),5)
	pygame.draw.line(screen,black,(560,500),(590,500),5)
	
	#left hand
	pygame.draw.line(screen,black,(500,250),(440,250),5)
	pygame.draw.line(screen,black,(440,250),(400,200),5)
	#right hand
	pygame.draw.line(screen,black,(500,250),(560,250),5)
	pygame.draw.line(screen,black,(560,250),(520,200),5)

	pygame.display.flip()
	pygame.time.wait(500)
	screen.fill((255,255,255))

def mediate2():
	pygame.draw.circle(screen,black,(500,150),60,5)
	pygame.draw.line(screen,black,(500,210),(500,380),5)
	#left leg
	pygame.draw.line(screen,black,(500,380),(410,500),5)
	pygame.draw.line(screen,black,(410,500),(380,500),5)
	#right leg
	pygame.draw.line(screen,black,(500,380),(590,500),5)
	pygame.draw.line(screen,black,(590,500),(620,500),5)
	
	#left hand
	pygame.draw.line(screen,black,(500,250),(440,250),5)
	pygame.draw.line(screen,black,(440,250),(480,200),5)
	#right hand
	pygame.draw.line(screen,black,(500,250),(560,250),5)
	pygame.draw.line(screen,black,(560,250),(600,200),5)

	pygame.display.flip()
	pygame.time.wait(500)
	screen.fill((255,255,255))

def end():
	#face
	pygame.draw.circle(screen,black,(500,150),60,5)
	pygame.draw.line(screen,black,(500,210),(500,380),5)
	#left leg
	pygame.draw.line(screen,black,(500,380),(440,500),5)
	pygame.draw.line(screen,black,(440,500),(410,500),5)
	#right leg
	pygame.draw.line(screen,black,(500,380),(560,500),5)
	pygame.draw.line(screen,black,(560,500),(590,500),5)
	#left hand
	pygame.draw.line(screen,black,(500,250),(440,250),5)
	pygame.draw.line(screen,black,(440,250),(480,300),5)
	#right hand
	pygame.draw.line(screen,black,(500,250),(560,250),5)
	pygame.draw.line(screen,black,(560,250),(600,300),5)

	pygame.display.flip()
	pygame.time.wait(500)
	screen.fill((255,255,255))

for i in range(500):
	start_position()
	mediate1()
	mediate2()
	end()

start_position()

for i in range(100):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()