#Imports

from CoinsInGame import *
from DonkeyKong import *

#Class for coins

class printingCoins(pygame.sprite.Sprite):

	def printCoins(self):

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

					listOfCoins.add(coins)

				for i in range(5):

					a.append(x+i)

					a.append(x-i)
					a.append(y+i)
					a.append(y-i)
			yy=yy-120
			a=[]

