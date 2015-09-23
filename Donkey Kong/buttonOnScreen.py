#Imports

from printMessage import *

#Class for creating buttons

class Button():

	def __init__(self):

		self.black=(0,0,0)

	def makeButton(self,msg,x,y,w,h,c1,c2,gameCanvas):
	
		text=printMessage()

		cursor=pygame.mouse.get_pos()

		mousePressed=pygame.mouse.get_pressed()

		if x+w>cursor[0]>x and y+h>cursor[1]>y:

			pygame.draw.rect(gameCanvas,c2,[x,y,w,h])

			if mousePressed[0]==1 and msg=="Play":

				return 1

			elif mousePressed[0]==1 and msg=="Quit":

				return 2

			elif mousePressed[0]==1 and msg=="Again":

				return 3

		else:

			pygame.draw.rect(gameCanvas,c1,[x,y,w,h])

		text.messageOnButton(msg,self.black,x,y,w,h,gameCanvas)		
