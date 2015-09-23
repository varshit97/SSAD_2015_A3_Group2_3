#Imports

import pygame

import random

import time

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class for Fireballs

class absorbFireballs(pygame.sprite.Sprite):

	def __init__(self,x,y,w,h):
		
		super(absorbFireballs,self).__init__()		#Calls the super class of the Walls class

		self.image=pygame.Surface([w,h])	#Adjusts the width and height of the wall

		self.image.fill(black)			#Fills the colour to the wall

		self.rect=self.image.get_rect()

		self.rect.x=x				#Adjusts the x coordinate of the wall

		self.rect.y=y				#Adjusts the y coordinate of the wall

	def absorbThem(self,allFireballs):

		listOfBalls=pygame.sprite.spritecollide(self,allFireballs,True)
