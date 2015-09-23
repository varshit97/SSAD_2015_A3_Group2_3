#Imports

import pygame

import random

import time

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class for Fireballs

class moveFireballs(pygame.sprite.Sprite):

	changeX=0

	changeY=0

	def __init__(self,x,y):

		super(moveFireballs,self).__init__()

		self.image=pygame.image.load('rsz_1fire.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y

		self.flag=0

	def makeFireBalls(self,x,y):

		self.image=pygame.image.load('rsz_fire.png')

		self.image.set_colorkey(black)

		self.rect=self.image.get_rect()

		self.rect.x=x

		self.rect.y=y

	def changeInstant(self,x,y):

		self.changeX+=x

		self.changeY+=y

	def emitFireBalls(self,allWalls):

		self.rect.y+=self.changeY

		fireballHitsWall=pygame.sprite.spritecollide(self,allWalls,False)

		for ball in fireballHitsWall:

			if self.changeY>0:

		       		self.rect.bottom=ball.rect.top

	 		else:

       				self.rect.top=self.rect.bottom		

		self.rect.x+=self.changeX

		fireballHitsWall=pygame.sprite.spritecollide(self,allWalls,False)

		for ball in fireballHitsWall:

			if self.changeX>0:

		       		self.rect.right=ball.rect.left

	 		else:

       				self.rect.left=self.rect.right

	def gravityForBall(self):

		self.changeInstant(0,1)

	def movingBalls(self,allWalls,allLadders):

		self.rect.y+=4

		if len(pygame.sprite.spritecollide(self,allWalls,False))==0:

			self.gravityForBall()

		if self.flag==0:

			self.rect.x+=4

			self.rect.y-=15

			if len(pygame.sprite.spritecollide(self,allWalls,False))>0:

				self.flag=1

				self.rect.x-=4

			self.rect.y+=15

		if self.flag==1:

			self.rect.x-=4

			self.rect.y-=15

			if len(pygame.sprite.spritecollide(self,allWalls,False))>0:

				self.flag=0

				self.rect.x+=4

			self.rect.y+=15

		self.rect.y-=4
