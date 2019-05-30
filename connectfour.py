# ConnectFour Game Class
# Implemented the logic for dropping the disks in valid columns/rows
# Implemented detecting winner if 4-in-a-row of the same disk horizontally/vertically/diagonally.
# Can play the game in console by calling playConsoleGame() method.




from copy import deepcopy
class ConnectFour():
	def __init__(self):
		""" Initializes the class object, sets up various helper member variables """
		self.board = []
		self.rows = 6
		self.columns = 7
		self.game_over = False
		self.diskCount = 0
		self.currentPlayer = "R"

	def createBoard(self):
		""" Creates a two-dimensional empty board and assigns said board to self.board member variable """
		for r in range(self.rows):
			self.board.append([])
			for c in range(self.columns):
				self.board[r].append("E")

	def returnBoard(self):
		""" Returns two-dimensional game board """ 
		return self.board
	def swapBoard(self, anotherBoard):
		""" Swaps out board for a copy of another board """
		self.board = deepcopy(anotherBoard)

	def printBoard(self):
		""" Prints out the board in an easy to see manner in the console """
		for r in range(self.rows):
			print(self.board[r])

	def checkDiskCount(self):
		""" Returns total disks, useful for checking for draws """
		return self.diskCount

	def checkGameOver(self):
		""" Returns whether game is over """
		return self.game_over

	def currentTurn(self):
		""" Returns the current player's turn """
		return self.currentPlayer

	def setTurn(self, turn):
		""" Sets the current players turn """
		self.currentPlayer = turn

	def makeMove(self, column, turn):
		""" Drops a disk on the board if column choice is valid """
		if (self.isValid(column)):
			locationCoord = self.findPlace(column)
			self.board[locationCoord[0]][locationCoord[1]] = turn
			self.diskCount+=1
			if self.currentPlayer == "Y":
				self.currentPlayer = "R"
			else:
				self.currentPlayer = "Y"
			return locationCoord
		else:
			return None

	def findPlace(self, column):
		""" Finds the place to drop disk on the board, returns coordinates to that place """
		for i in range(self.rows-1, -1 , -1):
			if (self.board[i][column-1] == "E"):
				return (i, column-1)


	def isValid(self, column):
		""" Returns whether column number to drop disk in is valid """
		if (column > 8 or column < 1):
			return False
		elif (self.board[0][column-1] != "E"):
			return False
		return True

	def playConsoleGame(self):
		""" Allows user to play ConnectFour with another player in the console """
		self.currentPlayer = "R"
		winner = ""
		self.printBoard()
		while (not self.game_over):
			if (self.diskCount == 42):
				print ("Game Over! Draw, No one wins!")
				return
			columnChoice = input("Choose a column: ")
			coordinates = self.makeMove(int(columnChoice), self.currentPlayer)
			self.printBoard()

			if (self.checkWin(self.currentPlayer)):
				winner = self.currentPlayer
				break

			if self.currentPlayer == "Y":
				self.currentPlayer = "R"
			else:
				self.currentPlayer = "Y"
		print("")
		print("Game Over! " + winner + " is the winner!")

	def checkPositionColor(self, row, column, turn):
		return self.board[row-1][column-1] == turn

	def checkThreeInARow(self, turn):
		return self.checkHorizontal(turn, 3) or self.checkVerticalThree(turn) or self.checkDiagonalTopToBottomThree(turn) or self.checkDiagonalBottomToTopThree(turn)
	
	def checkVerticalThree(self, turn):
		safetyCheck = 0
		for r in range(self.rows):
			for c in range(self.columns):
				if (safetyCheck < 2):
					if (self.board[r][c] == turn and self.board[r+1][c] == turn and self.board[r+2][c]):
						return True
			safetyCheck+=1
		return False

	def checkDiagonalTopToBottomThree(self, turn):
		for r in range(self.rows-2):
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r+1][c+1] == turn and self.board[r+2][c+2]):
					return True
		return False

	def checkDiagonalBottomToTopThree(self, turn):
		for r in range(self.rows-1, 1, -1):
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r-1][c+1] == turn and self.board[r-2][c+2] == turn):
					return True
		return False

	def checkWin(self, turn):
		""" Returns whether a player wins or not """
		return self.checkHorizontal(turn, 4) or self.checkVertical(turn) or self.checkDiagonalTopToBottom(turn) or self.checkDiagonalBottomToTop(turn)

	def checkHorizontal(self, turn, consecutiveNumber):
		""" Checks if the current player matches 4 in a row horizontally anywhere in the board """
		for r in self.board:
			count = 0
			for val in r:
				if val == turn:
					count+=1
				else:
					count = 0
				if count == consecutiveNumber:
					return True
		return False

	def checkVertical(self, turn):
		""" Checks if the current player matches 4 in a row vertically anywhere in the board """
		safetyCheck = 0
		for r in range(self.rows):
			for c in range(self.columns):
				if (safetyCheck < 3):
					if (self.board[r][c] == turn and self.board[r+1][c] == turn and self.board[r+2][c] == turn and self.board[r+3][c] == turn):
						return True
			safetyCheck+=1
		return False

	def checkDiagonalTopToBottom(self, turn):
		""" Checks if the current player matches 4 in a row diagonally from top to bottom (\) anywhere in the board """
		for r in range(self.rows-3):
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r+1][c+1] == turn and self.board[r+2][c+2] == turn and self.board[r+3][c+3] == turn):
					return True
		return False

	def checkDiagonalBottomToTop(self, turn):
		""" Checks if the current player matches 4 in a row diagonally from bottom to top (/) anywhere in the board """
		for r in range(self.rows-1, 2, -1):
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r-1][c+1] == turn and self.board[r-2][c+2] == turn and self.board[r-3][c+3] == turn):
					return True
		return False

	def testWin(self):
		""" Function used for testing given specific board situations """
		if self.checkWin(self.currentPlayer):
			print ("WIN")

	def makeBoardWinDiagonal(self, row, column, turn):
		""" Used to test if diagonal winning is working correctly """
		self.board[row][column] = turn
		self.board[row+1][column+1] = turn
		self.board[row+2][column+2] = turn
		self.board[row+3][column+3] = turn







class IncorrectMove(Exception):
	""" Exception class for invalid moves """
	pass

