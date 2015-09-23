#Imports

import pygame

import random

import time

#Class for printing messages

class printMessage():

	def __init__(self):

		self.font1=pygame.font.Font(None,45)

	def message(self,message,colour,gameCanvas,x,y):

		text=self.font1.render(message,True,colour)

		gameCanvas.blit(text,[x,y])

	def makeSurfaces(self,msg,colour):

		buttonSurface=self.font1.render(msg,True,colour)

		return buttonSurface,buttonSurface.get_rect()

	def messageOnButton(self,msg,colour,x,y,w,h,gameCanvas):
		textSurface,textRect=self.makeSurfaces(msg,colour)
		textRect.center=(x+(w/2),y+(h/2))
		gameCanvas.blit(textSurface,textRect)

