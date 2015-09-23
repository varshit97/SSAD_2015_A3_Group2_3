#Imports

import pygame

import random

import time

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class for placing Kong

class placeKong(pygame.sprite.Sprite):

	def __init__(self,x,y):

		super(placeKong,self).__init__()

		self.image=pygame.image.load('rsz_villian.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y

		self.kongSpeed=2

		self.flag=0

	def changeFlag(self,var):

		if var==1:

			self.flag=1

		if var==0:

			self.flag=0

	def getFlag(self):

		return self.flag

	def makeKong(self,x,y):

		self.image=pygame.image.load('rsz_villian.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y

	def getXCoordinate(self):

		return self.rect.x

	def getYCooordinate(self):

		return self.rect.y

	def moveKongRight(self,length):

		length+=3

		self.makeKong(length,120)

	def moveKongLeft(self,length):

		length-=3

		self.makeKong(length,120)

	def moveKong(self,length):

		if length<=200:

			self.moveKongRight(length)

			self.flag=0

		if length>689:

			self.moveKongLeft(length)

			self.flag=1

		if length>200 and length<=689:

			if self.flag==0:

				self.moveKongRight(length)

			if self.flag==1:

				self.moveKongLeft(length)
