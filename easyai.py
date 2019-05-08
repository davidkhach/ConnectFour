# Easy Difficulty AI Class
# Plays against a human
# Chooses which column to drop randomly



import connectfour
import random

class EasyAI():
	def __init__(self, turn, gameBoard):
		""" Initializes what color the AI is playing as and stores the board information """
		self.turn = turn
		self.gameBoard = gameBoard

	def setBoard(self, board):
		""" Swaps out the current gameboard with another """
		self.gameBoard = board

	def chooseMove(self):
		""" Returns a random column to drop disk in as long as it is valid (not full) """
		listOfColumns = [0,1,2,3,4,5,6]
		result = random.choice(listOfColumns)
		while (self.gameBoard.isValid(result+1) != True):
			result = random.choice(listOfColumns)
		return result
