import connectfour
import random

class EasyAI():
	def __init__(self, turn, gameBoard):
		self.turn = turn
		self.gameBoard = gameBoard

	def chooseMove(self):
		listOfColumns = [0,1,2,3,4,5,6]
		result = random.choice(listOfColumns)
		while (self.gameBoard.isValid(result+1) != True):
			result = random.choice(listOfColumns)
		return result
		

	def search(self, depth):
		pass
	def evaluate(self):
		pass
