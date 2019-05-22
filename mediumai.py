# Medium difficulty AI game class implementation
# Uses minimax recursive algorithm to determine what column to drop disk in
# Prioritizes making 4 in a row to win and stopping opponent from making 4 in a row
# Otherwise, tries to make 3 in a row as much as it can, if cannot then it drops disks randomly



import connectfour
import easyai
import random
import math
from copy import deepcopy

class MediumAI(easyai.EasyAI):

	def __init__(self, turn, game):
		if (turn == (255,0,0)):
			self.turn = "R"
			self.enemy = "Y"
		else:
			self.turn = "Y"
			self.enemy = "R"
		self.game = deepcopy(game)

	def printTest(self):
		print("hi") 


	def setBoard(self, board):
		self.game.swapBoard(board)


	def copyBoard(self):
		self.boardCopy = deepcopy(self.game.returnBoard())

	def chooseMove(self):

		copyOfGame = deepcopy(self.game)

		result = self.search(copyOfGame, 4, True)
		return result[0]


	def search(self, game, depth, maximizingPlayer):
		if (depth == 0):
			return self.evaluate(game)
		if (maximizingPlayer):
			value = -math.inf
			column = None
			for move in self.findAllPotentialMoves(game):

				newState = deepcopy(game)
				newState.setTurn(self.turn)
				#print ("Before moving: " + newState.currentTurn())
				newState.makeMove(move[1] + 1, self.turn)
				#print ("After moving: " + newState.currentTurn())
				result = self.search(newState, depth-1, False)[1]
				if (result > value):
					value = result
					column = move[1]
					if (result > 19999):
						return (column, value)
			return (column, value)
		else:
			value = math.inf
			column = None
			for move in self.findAllPotentialMoves(game):
				self.move = move[1]
				newState = deepcopy(game)
				newState.setTurn(self.enemy)
				#print ("Before moving: " + newState.currentTurn())
				newState.makeMove(move[1] + 1, self.enemy)
				#print ("After moving: " + newState.currentTurn())
				result = self.search(newState, depth-1, True)[1]
				if (result < value):
					value = result
					column = move[1]
					if (result < -19999):
						return (column, value)
			return (column, value)



	def evaluate(self, game):
		score = 0
		if (game.checkWin(self.turn)):
			score += 20000
		if (game.checkWin(self.enemy)):
			score -= 20000

		if (game.checkThreeInARow(self.turn)):
			score += 2000
		if game.checkPositionColor(1,1,self.turn):
			score += 40
		if game.checkPositionColor(1,1,self.enemy):
			score -= 40
		if (game.checkThreeInARow(self.enemy)):
			score -= 2000
		score += random.choice([1,2,3,4,5,6,7])
		return (None, score)

	def findAllPotentialMoves(self, game):
		listOfAllMoves = []
		for column in range(1,8):
			if game.isValid(column):
				listOfAllMoves.append(game.findPlace(column))
		return listOfAllMoves

"""
	def chooseMove(self):
		theTot = -10000
		theMove = None
		for move in self.findAllPotentialMoves(self.game):
			copyOfGame = deepcopy(self.game)
			copyOfGame.makeMove(move[1]+1, self.turn)
			result = self.search(copyOfGame)
			if result > theTot:
				theTot = result
				theMove = move[1]
		return theMove

	def search(self, game):
		return self.evaluate(game)



	def evaluate(self, game):
		if self.turn == "R":
			opp_player = "Y"
		else:
			opp_player = "R"
		score = 0
		if (game.checkWin(self.turn)):
			score += 15000
		score += random.choice([1,2,3,4,5,6,7])
		return score


"""


	