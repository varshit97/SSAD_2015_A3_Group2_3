#Imports

import pygame

import random

import time

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class to place princess

class placePrincess(pygame.sprite.Sprite):

	def __init__(self,x,y):

		super(placePrincess,self).__init__()

		self.image=pygame.image.load('rsz_1princess.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y
