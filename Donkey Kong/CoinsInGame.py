#Imports

import pygame

import random

import time


#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)


#Class for coins

class coinsInGame(pygame.sprite.Sprite):

	def __init__(self,x,y):

		super(coinsInGame,self).__init__()

		self.image=pygame.image.load('rsz_coins.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y
