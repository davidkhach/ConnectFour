import connectfour
import easyai
from copy import deepcopy

class MediumAI(easyai.EasyAI):

	def __init__(self, turn, game):
		self.turn = turn
		self.game = game
		self.gameCopy = game
		self.boardCopy = []
		if (self.turn == "R"):
			self.enemyTurn = "Y"
		else:
			self.enemyTurn = "R"


	def copyBoard(self):
		self.boardCopy = deepcopy(self.game.returnBoard())

	def chooseMove(self):
		topScore = -100000
		chosenMove = None
		allMoves = self.findAllPotentialMoves()
		self.gameCopy = connectfour.ConnectFour()
		self.gameCopy.swapBoard(self.boardCopy)
		for move in allMoves:
			self.gameCopy.makeMove(move[1], self.turn)
			result = self.search(3)
			if (result > topScore):
				topScore = result
				chosenMove = move[1]
		return chosenMove


	def search(self, depth):
		pass

	def evaluate(self):
		score = 0
		if (self.gameCopy.checkWin(self.turn)):
			score += 10000
		if (self.gameCopy.checkWin(self.enemyTurn)):
			score -= 10000
		return score



	def findAllPotentialMoves(self):
		listOfAllMoves = []
		for column in range(1,8):
			if self.game.isValid(column):
				listOfAllMoves.append(self.game.findPlace(column))
		return listOfAllMoves
			

