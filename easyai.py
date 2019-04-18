import connectfour
import random

class EasyAI(turn, gameBoard):
	def __init__(self):
		self.turn = turn
		self.gameBoard = gameBoard

	def chooseMove(self):
		listOfColumns = [1,2,3,4,5,6,7]
		result = random.choice(listOfColumns)
		while (self.gameBoard.isValid(result) != True):
			result = random.choice(listOfColumns)
		return result
		

	def search(self, gameState, depth, turn):
		pass
	def evaluate(self, gameState, turn):
		pass
