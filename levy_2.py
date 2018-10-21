#Submission by Yutika Kulwe, CED15I017
import sys, pygame, random as rndm, time
import numpy as np
import math
pygame.init()
screen = pygame.display.set_mode((1000,600))
screen.fill((255,255,255))

#colors
saffron=(250,153,7)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)

pi=(22.0/7.0)

def Levys_C_curve(x,y,l,a,n):
	if n>0 :
		l=float(l/math.sqrt(2))
		Levys_C_curve(x,y,l,(a+45),n-1)
		x=x+ l*math.cos((a+45)*(pi/180))
		y=y+ l*math.sin((a+45)*(pi/180))

		Levys_C_curve(x,y,l,(a-45),n-1)
	elif n==0:
		pygame.draw.line(screen, saffron ,[x, y], [x + (l*math.cos(a*(pi/180))), y + (l*math.sin(a*(pi/180)))], 1)



Levys_C_curve(350,200,250,0,14)
pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()