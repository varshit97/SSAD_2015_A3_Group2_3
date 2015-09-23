#Imports

import pygame

import random

import time

from Person import *

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

#Class for the player

class PlayerIsHero(Person):

	heroChangeX=0					#Initial change in the x-coordinate of the hero

	heroChangeY=0					#Initial change in the y-coordinate of the hero

	flag=1

	count=0

	def changeFlag(self,var):

		if var==1:

			self.flag=1

		if var==0:

			self.flag=0

	def getFlag(self):

		return self.flag

	def changeCount(self):

		count+=1

	def setPosition(self,x,y):

		self.rect.x=x

		self.rect.y=y
	
	def getXCoordinate(self):

		return self.rect.x

	def getYCoordinate(self):

		return self.rect.y

	def changePosition(self,x,y):			#Changes the position of the hero

		self.heroChangeX+=x

		self.heroChangeY+=y

	def changeInstant(self,x,y):

		self.changeFlag(0)

		self.rect.x=self.rect.x+x

		self.rect.y=self.rect.y+y

		self.changeFlag(1)

	def printPlayer(self,allWalls):			#Prints the correct position of the hero without hitting the walls etc.

		if self.flag==0:

			if self.heroChangeY==0:

				self.heroChangeY=1

			else:

			     	self.heroChangeY+=1

			if self.rect.y>=1000-self.rect.height and self.heroChangeY>=0:
			
				self.rect.y=1000-self.rect.height

		if self.flag==1 or self.flag==0:

			self.rect.y+=self.heroChangeY

			listOfHeroHitsWall=pygame.sprite.spritecollide(self,allWalls,False)

			for blockHero in listOfHeroHitsWall:

				if self.heroChangeY>0:

					self.rect.bottom=blockHero.rect.top

				else:

					self.rect.top=blockHero.rect.bottom

				if self.flag==0:

					self.heroChangeY=0

			self.rect.x+=self.heroChangeX

			listOfHeroHitsWall=pygame.sprite.spritecollide(self,allWalls,False)

			for blockHero in listOfHeroHitsWall:

				if self.heroChangeX>0:

					self.rect.right=blockHero.rect.left

				else:

					self.rect.left=blockHero.rect.right

	def heroJump(self,allWalls,allLadders):
		
		self.rect.y+=3
		
		listOfWalls=pygame.sprite.spritecollide(self,allWalls,False)

		listofLadders=pygame.sprite.spritecollide(self,allLadders,False)

		self.rect.y-=3

		if len(listOfWalls)>0 or self.rect.bottom<=1000 or len(listofLadders)>0:
		
			self.heroChangeY-=10

	def consumeCoins(self,allCoins,allWalls):

		listOfHeroHitsCoins=pygame.sprite.spritecollide(self,allCoins,True)

		if len(listOfHeroHitsCoins)>0:

			self.score+=5

	def getScore(self):
		if self.score>0:
			return self.score
		else:
			return 0
		
	def checkLadderAndWalls(self,allLadders,allWalls):

		self.rect.y+=3

		if len(pygame.sprite.spritecollide(self,allLadders,False))>0 and len(pygame.sprite.spritecollide(self,allWalls,False))==0:

			self.rect.y-=3
			
			self.changeInstant(0,5)

		elif len(pygame.sprite.spritecollide(self,allLadders,False))>0 and len(pygame.sprite.spritecollide(self,allWalls,False))>0:

			self.rect.y-=3

		elif len(pygame.sprite.spritecollide(self,allLadders,False))>0:

			self.rect.y-=3

			self.changeInstant(0,5)

	def heroDeath(self,allFireballs):

		listOfHeroHitsFireballs=pygame.sprite.spritecollide(self,allFireballs,True)

		if len(listOfHeroHitsFireballs)>0:

			x=self.touchedFireball(1)

			self.score-=25

			self.lives-=1

		else:
		
			x=self.touchedFireball(0)

		return x

	def touchedFireball(self,var):

		if var==1:

			return 1
			
		else:
		
			return 0

	def changeHeroPosition(self,x,y):

		self.rect.x=x

		
		self.rect.y=y

	def getLives(self):

		return self.lives

	def heroWins(self,princess):

		heroMeetsPrincess=pygame.sprite.spritecollide(self,princess,False)

		if len(heroMeetsPrincess)>0:

			return 1	
