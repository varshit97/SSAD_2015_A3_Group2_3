import pygame
import random
import time
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
class Walls(pygame.sprite.Sprite):
	#Constructor
	def __init__(self,x,y,w,h):
		super(Walls,self).__init__()		#Calls the super class of the Walls class
		self.image=pygame.Surface([w,h])	#Adjusts the width and height of the wall
		self.image.fill(red)			#Fills the colour to the wall
		self.rect=self.image.get_rect()
		self.rect.x=x				#Adjusts the x coordinate of the wall
		self.rect.y=y				#Adjusts the y coordinate of the wall

