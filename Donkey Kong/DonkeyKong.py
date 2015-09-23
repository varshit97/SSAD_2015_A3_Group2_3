#Imports

import pygame

import random

import time

from Walls import *

from Person import *

from PlayerIsHero import *

from CoinsInGame import *

from ladderPlacement import *

from placePrincess import *

from placeKong import *

from moveFireballs import *

from absorbFireballs import *

from printMessage import *

from printingCoins import *

from buttonOnScreen import *

#Colours

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

green=(0, 128, 0)

#light_green=(0,255,0)

orange=(255, 153, 0)

light_orange=(255, 184, 77)

light_red=(255, 71, 25)

light_blue=(153, 255, 204)
light_green=(77, 255, 77)	
#Variables


def mainGameLoop():

	gameExit=False	

	#Starts the init function in pygame

	pygame.init()


	#Variables

	gameCanvas=pygame.display.set_mode([1500,1000])		#Make a canvas on which we can draw

	gameCanvas.fill(black)					#Fills the colour to the background

	clock=pygame.time.Clock()				#Used for frames per second


	#Sprite Groups to check collision

	listOfWalls=pygame.sprite.Group()

	listOfWallsAndHero=pygame.sprite.Group()

	listOfCoins=pygame.sprite.Group()

	listOfLadders=pygame.sprite.Group()

	princessPlace=pygame.sprite.Group()

	kongPlace=pygame.sprite.Group()

	lifeGroup=pygame.sprite.Group()

	fireballGroup=pygame.sprite.Group()


	#Building the walls

	ceiling=Walls(140,40,1200,25)

	wall1=Walls(115,40,25,860)

	floor=Walls(115,900,1250,25)

	wall2=Walls(1340,40,25,860)


	#Building the floors

	leftFloor11=Walls(140,180,165,25)

	leftFloor12=Walls(330,180,275,25)

	leftFloor13=Walls(630,180,100,25)

	rightFloor11=Walls(560,300,345,25)

	rightFloor12=Walls(930,300,430,25)

	leftFloor21=Walls(140,420,440,25)

	leftFloor22=Walls(605,420,150,25)

	rightFloor21=Walls(400,540,370,25)

	rightFloor22=Walls(795,540,370,25)

	leftFloor31=Walls(140,660,370,25)

	leftFloor32=Walls(535,660,450,25)

	rightFloor31=Walls(405,780,405,25)

	rightFloor32=Walls(835,780,510,25)

	#Putting the walls in the sprite list to check collision

	listOfWalls.add(ceiling,wall1,floor,wall2,leftFloor11,leftFloor12,leftFloor13,rightFloor11,leftFloor21,rightFloor12,leftFloor22,rightFloor21,rightFloor22,leftFloor31,leftFloor32,rightFloor31,rightFloor32)

	#Positioning the ladders

	ladder1=ladderPlacement(805,780)

	ladder2=ladderPlacement(505,660)

	ladder3=ladderPlacement(765,540)

	ladder4=ladderPlacement(575,420)

	ladder5=ladderPlacement(900,420)

	ladder6=ladderPlacement(900,300)

	ladder7=ladderPlacement(600,180)

	ladder8=ladderPlacement(300,300)

	ladder9=ladderPlacement(300,180)

	#Putting the ladders in the sprite list to check collision	

	listOfLadders.add(ladder1,ladder2,ladder3,ladder4,ladder5,ladder6,ladder7,ladder8,ladder9)

	#Positioning the princess

	princess=placePrincess(140,120)

	princessPlace.add(princess)

	#Printing the coins on the canvas

	a=[]

	yy=900

	for j in range(125,900,120):

		for _ in range(20):

			y1=yy-65

			y2=yy-40

			x=random.randint(130,1300)

			y=random.randint(y1,y2)

			if x not in a and y not in a:

				coins=coinsInGame(x,y)
				if len(pygame.sprite.spritecollide(coins,listOfLadders,False))==0 and len(pygame.sprite.spritecollide(coins,princessPlace,False))==0:
					listOfCoins.add(coins)				#Adding coins to the sprite list

			for i in range(5):					#Removing the overlapping

				a.append(x+i)
				a.append(x+i+20)

				a.append(x-i)
				a.append(x-i-20)

				a.append(y+i)
				a.append(y+i+20)

				a.append(y-i)
				a.append(y-i-20)
		yy=yy-120

		a=[]
					

	#Positioning the Kong

	kong=placeKong(180,120)

	kongPlace.add(kong)


	#Print the message on the screen

	text=printMessage()

	
	#Making the hero

	hero=PlayerIsHero(145,870,'rsz_hero2_1.png')


	#Making the fireballs

	fireballAbsorber=absorbFireballs(145,870,40,50)

	PlayerIsHero.allWalls=listOfWalls


	#Adding the walls and hero to the same sprite list for simplification

	listOfWallsAndHero.add(ceiling,wall1,floor,wall2,leftFloor11,leftFloor12,leftFloor13,rightFloor11,rightFloor12,leftFloor21,leftFloor22,rightFloor21,rightFloor22,leftFloor31,leftFloor32,rightFloor31,rightFloor32,hero)


	#Main loop for execution

	#Variables

	startKong=190

	count=0

	move=0

	flagup=0

	pygame.mixer.music.load('music.mp3')

	
	pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)

	
	pygame.mixer.music.play()


	#While loop for the game with frames per second
	while not gameExit:

		if startKong<160:						#Condition for the Kong

			startKong=160

			kong.changeFlag(0)

		gameCanvas.fill(green)						#Filling the canvas always and drawing again

		clock.tick(30)							#Frames per second

		text.message(str(hero.getScore()),red,gameCanvas,200,950)	#Message to be displayed

		if len(pygame.sprite.spritecollide(hero,listOfLadders,False))>0:#Method to identify the events

			tempstate=pygame.key.get_pressed()

			if tempstate[pygame.K_w]:

				hero.changeInstant(0,-5)
			elif tempstate[pygame.K_s]:

				hero.checkLadderAndWalls(listOfLadders,listOfWalls)

		for event in pygame.event.get():				#Method to identify the events

			if event.type==pygame.constants.USEREVENT:

				pygame.mixer.music.load('music.mp3')

				pygame.mixer.music.play()

			if event.type==pygame.KEYDOWN:

				if event.key==pygame.K_a:			#For moving right

					hero.changePosition(-5,0)		

				if event.key==pygame.K_d:			#For moving left

					hero.changePosition(5,0)

				if event.key==pygame.K_q:

					pygame.quit()
					quit()

			if event.type==pygame.KEYUP:

					if event.key==pygame.K_a:

						hero.changePosition(5,0)

					if event.key==pygame.K_d:

						hero.changePosition(-5,0)

			else:

				if event.type==pygame.QUIT:			#For quiting

					gameExit=True	

				if event.type==pygame.KEYDOWN:

					if event.key==pygame.K_SPACE:		#For jumping

						hero.changeFlag(0)

						hero.heroJump(listOfWallsAndHero,listOfLadders)

		listOfWallsAndHero.update()

		hero.printPlayer(listOfWalls)					#Checking for walls

		kong.moveKong(startKong)					#Moving the Kong

		hero.consumeCoins(listOfCoins,listOfWalls)			#For hero to take the coins

		listOfWallsAndHero.draw(gameCanvas)				#Drawing the hero and walls

		listOfCoins.draw(gameCanvas)					#Drawing the coins

		listOfLadders.draw(gameCanvas)					#Drawing the ladders

		princessPlace.draw(gameCanvas)					#Drawing the princess

		kongPlace.draw(gameCanvas)					#Drawing the Kong

		if startKong<689 and kong.getFlag()==0:				#Conditions for the Kong

			startKong+=3

			if startKong==689:

			 	kong.changeFlag(1)

		if startKong>200 and kong.getFlag()==1:

	  		startKong-=3

			if startKong==190:

			 	kong.changeFlag(0)

		if count%60==0:							#Condition for the Fireballs

			fireballs=moveFireballs(startKong,130)

			fireballGroup.add(fireballs)

		touchFireball=hero.heroDeath(fireballGroup)

		for balls in fireballGroup:

			balls.emitFireBalls(listOfWalls)

			balls.movingBalls(listOfWalls,listOfLadders)

		x1=1200								#Condition to decrease the lives of the player

		for _ in range(hero.getLives()):

			gameCanvas.blit(pygame.image.load('rsz_1heart1.png'),[x1,950])

			x1+=50

		if touchFireball==1:						#Resetting the player's position

		 	if move<3:

				hero.changeHeroPosition(145,870)

				move+=1

			if move==3:

				gameExit=True

		heroWins=hero.heroWins(princessPlace)

		if heroWins==1:

		 	flagup=1

			break

		fireballGroup.draw(gameCanvas)

		fireballAbsorber.absorbThem(fireballGroup)

		count+=1

		pygame.display.flip()

	gameCanvas.fill(green)

	if flagup==1:								     #Text to show after the game is finished
		
		text.message("Score : "+str(hero.getScore()),black,gameCanvas,600,500)

		text.message("You Win",black,gameCanvas,600,700)

	else:
		text.message("You Win",black,gameCanvas,600,700)

		text.message("Score : "+str(hero.getScore()),black,gameCanvas,600,500)


	pygame.display.flip()								#Updates everything
	
	time.sleep(3)								#Waits for you to see the score

	pygame.quit()								#Quits the pygame.init() function

	quit()									#Quits the window


def firstScreen():

	pygame.init()

	clock=pygame.time.Clock()						#Used for frames per second

	gameExit=False

	text=printMessage()

	gameCanvas=pygame.display.set_mode([1500,900])				#Make a canvas on which we can draw

	gameCanvas.fill(black)							#Fills the colour to the background
	button=Button()

	while not gameExit:

		clock.tick(30)

		gameCanvas.fill(green)

		gameCanvas.blit(pygame.image.load('DK1.png'),[200,60])

		x=button.makeButton("Play",1260,400,200,100,orange,light_orange,gameCanvas)

		y=button.makeButton("Quit",1260,600,200,100,orange,light_orange,gameCanvas)


		if x==1:

			return 1

		if y==2:

			pygame.quit()

			quit()

		else:

			for event in pygame.event.get():				#Method to identify the events

	
				if event.type==pygame.QUIT:				#For quiting

						gameExit=True

		pygame.display.flip()							#Updates everything

	pygame.quit()									#Quits the pygame.init() function

	quit()										#Quits the window
	
y=firstScreen()

if y==1:

	mainGameLoop()
