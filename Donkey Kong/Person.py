#Imports

import pygame

import random

import time

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class to be inherited

class Person(pygame.sprite.Sprite):

	def __init__(self,x,y,img):

		super(Person,self).__init__()

		self.image=pygame.image.load(img)

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y

		self.allWalls=[]

		self.allCoins=[]

		self.jumpingState=False

		self.score=0

		self.lives=3
