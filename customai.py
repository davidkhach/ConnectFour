# Custom AI class for players to create their own AI (assumes minimax implementation)
# Easy to use, all that is needed is the custom evaluation function determined by the user
# If you don't want to use minimax, override chooseMove(self) method from MediumAI, make sure to return a column number
# To use your custom AI, modify line 149 in view.py from "ai = mediumai.MediumAI(secondTurnColor, game)" to "ai = customai.CustomAI(secondTurnColor, game)"




import connectfour
import mediumai
import random
import math
from copy import deepcopy

class CustomAI(mediumai.MediumAI):
	def __init__(self, turn, game):
		super().__init__(turn, game)

	def chooseMove(self):
		""" Define your choose move function here to return a valid move. Game helper functions you can consider using: game.isValid(column), check connectfour.py for more details """

		return 0



	def evaluate(self, game):
		""" Create your custom evaluation function here, return type must be (None, score) """
		score = 0
		pass

