import sys,pygame
from pygame import gfxdraw
import  math
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((1000,600))
screen.fill((255,255,255))

#colors
cream=(255,160,122)
dark_cream=(233,150,122)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
firebrick=(178,34,34)

def nameplate():
	pygame.draw.polygon(screen,cream,[(20,60),(920,60),(920,90),(20,90)])
	pygame.draw.line(screen,cream,(140,120),(800,120),3)
	pygame.draw.line(screen,cream,(20,90),(140,120),4)
	pygame.draw.line(screen,cream,(920,90),(800,120),3)

	pygame.display.flip()

def sidewalls():
	#left
	pygame.draw.polygon(screen,dark_cream,[(110,rear_wall_y_end),(110,110),(50,100),(50,320)])
	#right
	pygame.draw.polygon(screen,dark_cream,[(820,rear_wall_y_end),(820,110),(880,100),(880,320)])

	pygame.display.flip()

front_wall_y_end=300
rear_wall_y_end=280
roof_x_start=20
roof_x_end=920
roof_y_end=120
roof_y_start=90
centre_x=470
centre_y=60
breadth=45
length=30
slant=30
offset=3

def upperlines():

	pygame.draw.polygon(screen,dark_cream,[(centre_x-8.5*breadth,roof_y_start),(centre_x-8.5*breadth-slant,roof_y_start),(centre_x-8.5*length,roof_y_end),(centre_x-8.5*length+slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x-6.5*breadth,roof_y_start),(centre_x-6.5*breadth-slant,roof_y_start),(centre_x-6.5*length,roof_y_end),(centre_x-6.5*length+slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x-4.5*breadth,roof_y_start),(centre_x-4.5*breadth-slant,roof_y_start),(centre_x-4.5*length,roof_y_end),(centre_x-4.5*length+slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x-2.5*breadth,roof_y_start),(centre_x-2.5*breadth-slant,roof_y_start),(centre_x-2.5*length,roof_y_end),(centre_x-2.5*length+slant,roof_y_end)])
	
	pygame.draw.polygon(screen,dark_cream,[(centre_x-0.5*breadth,roof_y_start),(centre_x-0.5*breadth-slant,roof_y_start),(centre_x-0.5*length,roof_y_end),(centre_x-0.5*length+slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x+0.5*breadth,roof_y_start),(centre_x+0.5*breadth+slant,roof_y_start),(centre_x+0.5*length,roof_y_end),(centre_x+0.5*length-slant,roof_y_end)])
	
	pygame.draw.polygon(screen,dark_cream,[(centre_x+2.5*breadth,roof_y_start),(centre_x+2.5*breadth+slant,roof_y_start),(centre_x+2.5*length,roof_y_end),(centre_x+2.5*length-slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x+4.5*breadth,roof_y_start),(centre_x+4.5*breadth+slant,roof_y_start),(centre_x+4.5*length,roof_y_end),(centre_x+4.5*length-slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x+6.5*breadth,roof_y_start),(centre_x+6.5*breadth+slant,roof_y_start),(centre_x+6.5*length,roof_y_end),(centre_x+6.5*length-slant,roof_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x+8.5*breadth,roof_y_start),(centre_x+8.5*breadth+slant,roof_y_start),(centre_x+8.5*length,roof_y_end),(centre_x+8.5*length-slant,roof_y_end)])
	
	pygame.display.flip()

def front_walls():
	pygame.draw.polygon(screen,firebrick,[(centre_x-0.5*breadth,roof_y_end-30),(centre_x+0.5*breadth,roof_y_end-30),(centre_x+0.5*breadth,front_wall_y_end),(centre_x-0.5*breadth,front_wall_y_end)])
	pygame.draw.polygon(screen,cream,[(centre_x-0.5*breadth,((roof_y_end-front_wall_y_end)/2)+280-10),(centre_x+0.5*breadth,((roof_y_end-front_wall_y_end)/2)+280-10),(centre_x+0.5*breadth,((roof_y_end-front_wall_y_end)/2)+280+10),(centre_x-0.5*breadth,((roof_y_end-front_wall_y_end)/2)+280+10)])
	pygame.draw.polygon(screen,cream,[(centre_x-6*breadth-10,roof_y_end-30),(centre_x-6*breadth+slant,roof_y_end-30),(centre_x-6*breadth+slant,front_wall_y_end),(centre_x-6*breadth-10,front_wall_y_end)])
	pygame.draw.polygon(screen,cream,[(centre_x+6*breadth+10,roof_y_end-30),(centre_x+6*breadth-slant,roof_y_end-30),(centre_x+6*breadth-slant,front_wall_y_end),(centre_x+6*breadth+10,front_wall_y_end)])
	pygame.draw.polygon(screen,cream,[(centre_x-0.5*breadth,front_wall_y_end-5),(centre_x+0.5*breadth,front_wall_y_end-5),(centre_x+0.5*breadth,front_wall_y_end+5),(centre_x-0.5*breadth,front_wall_y_end+5)])


def rear_walls():
	pygame.draw.polygon(screen,dark_cream,[(centre_x-5*breadth,roof_y_end),(centre_x-5*breadth+slant,roof_y_end),(centre_x-5*breadth+slant,rear_wall_y_end),(centre_x-5*breadth,rear_wall_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(centre_x+5*breadth,roof_y_end),(centre_x+5*breadth-slant,roof_y_end),(centre_x+5*breadth-slant,rear_wall_y_end),(centre_x+5*breadth,rear_wall_y_end)])

def boxes():
	pygame.draw.polygon(screen,firebrick,[(0,180),(0,320),(90,320),(90,180)])
	pygame.draw.polygon(screen,firebrick,[(970,180),(970,320),(850,320),(850,180)])
	pygame.draw.polygon(screen,cream,[(0,320),(90,320),(90,300),(0,300)])
	pygame.draw.polygon(screen,cream,[(970,320),(850,320),(850,300),(970,300)])
	pygame.draw.polygon(screen,cream,[((centre_x-7*breadth+slant+25),190),((centre_x-7*breadth+slant+25),front_wall_y_end),(90,front_wall_y_end),(90,190)])
	pygame.draw.polygon(screen,cream,[((centre_x+7*breadth-slant-25),190),((centre_x+7*breadth-slant-25),front_wall_y_end),(850,front_wall_y_end),(850,190)])

	pygame.draw.polygon(screen,dark_cream,[(90,320),(90,front_wall_y_end),(100,rear_wall_y_end),(100,front_wall_y_end)])
	pygame.draw.polygon(screen,dark_cream,[(850,320),(850,front_wall_y_end),(840,rear_wall_y_end),(840,front_wall_y_end)])
	#pygame.draw.polygon(screen,cream,[(90,rear_wall_y_end),(90,front_wall_y_end),((centre_x-7*breadth+slant+25),front_wall_y_end),((centre_x-7*breadth+slant+25),rear_wall_y_end)])
	#pygame.draw.polygon(screen,cream,[(850,rear_wall_y_end),(850,front_wall_y_end),((centre_x+7*breadth-slant-25),front_wall_y_end),((centre_x+7*breadth-slant-25),rear_wall_y_end)])
	
def join_walls():
	#upper
	pygame.draw.polygon(screen,cream,[(centre_x-6*breadth+slant,((front_wall_y_end-roof_y_end)/2)+120),(centre_x-6*breadth+slant,((front_wall_y_end-roof_y_end)/2)+120-25),(centre_x-5*breadth+slant,((rear_wall_y_end-roof_y_end)/2)+120),(centre_x-5*breadth+slant,((rear_wall_y_end-roof_y_end)/2)+120+20)])
	pygame.draw.polygon(screen,cream,[(centre_x+6*breadth-slant,((front_wall_y_end-roof_y_end)/2)+120),(centre_x+6*breadth-slant,((front_wall_y_end-roof_y_end)/2)+120-25),(centre_x+5*breadth-slant,((rear_wall_y_end-roof_y_end)/2)+120),(centre_x+5*breadth-slant,((rear_wall_y_end-roof_y_end)/2)+120+20)])
	#lower
	pygame.draw.polygon(screen,cream,[(centre_x-5*breadth+slant,rear_wall_y_end),(centre_x-6*breadth+slant,front_wall_y_end),(centre_x-6*breadth+slant,front_wall_y_end-15),(centre_x-5*breadth+slant,rear_wall_y_end-15)])
	pygame.draw.polygon(screen,cream,[(centre_x+5*breadth-slant,rear_wall_y_end),(centre_x+6*breadth-slant,front_wall_y_end),(centre_x+6*breadth-slant,front_wall_y_end-15),(centre_x+5*breadth-slant,rear_wall_y_end-15)])

def floorwall():
	pygame.draw.polygon(screen,dark_cream,[(0,rear_wall_y_end-15),(0,front_wall_y_end-15),(centre_x-6*breadth+slant,front_wall_y_end-15),(centre_x-5*breadth+slant,rear_wall_y_end-15)])
	pygame.draw.polygon(screen,dark_cream,[(970,rear_wall_y_end-15),(970,front_wall_y_end-15),(centre_x+6*breadth-slant,front_wall_y_end-15),(centre_x+5*breadth-slant,rear_wall_y_end-15)])

def windows():
	pygame.draw.polygon(screen,white,[(centre_x-7.7*breadth,206),(centre_x-7.7*breadth,268.7),((centre_x-7*breadth+slant+10),268.7),((centre_x-7*breadth+slant+10),206)])
	pygame.draw.polygon(screen,white,[(centre_x+7.7*breadth,206),(centre_x+7.7*breadth,268.7),((centre_x+7*breadth-slant-10),268.7),((centre_x+7*breadth-slant-10),206)])

def gate():
	pygame.draw.polygon(screen,cream,[(centre_x-1*breadth,front_wall_y_end),(centre_x-1*breadth+offset,front_wall_y_end),(centre_x-1*breadth+offset,230),(centre_x-1*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+1*breadth,front_wall_y_end),(centre_x+1*breadth-offset,front_wall_y_end),(centre_x+1*breadth-offset,230),(centre_x+1*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x-1.5*breadth,front_wall_y_end),(centre_x-1.5*breadth+offset,front_wall_y_end),(centre_x-1.5*breadth+offset,230),(centre_x-1.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x-2*breadth,front_wall_y_end),(centre_x-2*breadth+offset,front_wall_y_end),(centre_x-2*breadth+offset,230),(centre_x-2*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x-2.5*breadth,front_wall_y_end),(centre_x-2.5*breadth+offset,front_wall_y_end),(centre_x-2.5*breadth+offset,230),(centre_x-2.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x-3*breadth,front_wall_y_end),(centre_x-3*breadth+offset,front_wall_y_end),(centre_x-3*breadth+offset,230),(centre_x-3*breadth,230)])	
	pygame.draw.polygon(screen,cream,[(centre_x-3.5*breadth,front_wall_y_end),(centre_x-3.5*breadth+offset,front_wall_y_end),(centre_x-3.5*breadth+offset,230),(centre_x-3.5*breadth,230)])	
	pygame.draw.polygon(screen,cream,[(centre_x-4*breadth,front_wall_y_end),(centre_x-4*breadth+offset,front_wall_y_end),(centre_x-4*breadth+offset,230),(centre_x-4*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+1.5*breadth,front_wall_y_end),(centre_x+1.5*breadth-offset,front_wall_y_end),(centre_x+1.5*breadth-offset,230),(centre_x+1.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+2*breadth,front_wall_y_end),(centre_x+2*breadth-offset,front_wall_y_end),(centre_x+2*breadth-offset,230),(centre_x+2*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+2.5*breadth,front_wall_y_end),(centre_x+2.5*breadth-offset,front_wall_y_end),(centre_x+2.5*breadth-offset,230),(centre_x+2.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+3*breadth,front_wall_y_end),(centre_x+3*breadth-offset,front_wall_y_end),(centre_x+3*breadth-offset,230),(centre_x+3*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+3.5*breadth,front_wall_y_end),(centre_x+3.5*breadth-offset,front_wall_y_end),(centre_x+3.5*breadth-offset,230),(centre_x+3.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+4*breadth,front_wall_y_end),(centre_x+4*breadth-offset,front_wall_y_end),(centre_x+4*breadth-offset,230),(centre_x+4*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x-4.5*breadth,front_wall_y_end),(centre_x-4.5*breadth-offset,front_wall_y_end),(centre_x-4.5*breadth-offset,230),(centre_x-4.5*breadth,230)])
	pygame.draw.polygon(screen,cream,[(centre_x+4.5*breadth,front_wall_y_end),(centre_x+4.5*breadth-offset,front_wall_y_end),(centre_x+4.5*breadth-offset,230),(centre_x+4.5*breadth,230)])
	
	pygame.draw.polygon(screen,cream,[(centre_x-0.55*breadth,front_wall_y_end),(centre_x-5.27*breadth,front_wall_y_end),(centre_x-5.27*breadth,230),(centre_x-0.55*breadth,230)],6)
	pygame.draw.polygon(screen,cream,[(centre_x+0.55*breadth,front_wall_y_end),(centre_x+5.27*breadth,front_wall_y_end),(centre_x+5.27*breadth,230),(centre_x+0.55*breadth,230)],6)


sidewalls()
upperlines()
rear_walls()
nameplate()
floorwall()
front_walls()

join_walls()

boxes()
windows()
gate()


myfont = pygame.font.SysFont('Times New Roman', 22)
newfont=pygame.font.SysFont('Times New Roman', 15)
text_in=newfont.render('IN', False, (0, 0, 0))
text_out=newfont.render('OUT', False, (0, 0, 0))
textsurface = myfont.render('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY DESIGN AND MANUFACTURING', False, (0, 0, 0))
screen.blit(textsurface,(43,67))
screen.blit(text_in,(centre_x-7*breadth+slant+20,200))
screen.blit(text_out,(centre_x+7*breadth-45-slant,200))
pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()