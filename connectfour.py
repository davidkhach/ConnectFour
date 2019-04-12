class ConnectFour():
	def __init__(self):
		self.board = []
		self.rows = 6
		self.columns = 7
		self.game_over = False
		self.diskCount = 0
		self.currentPlayer = ""

	def createBoard(self):
		for r in range(self.rows):
			self.board.append([])
			for c in range(self.columns):
				self.board[r].append("E")

	def printBoard(self):
		for r in range(self.rows):
			print(self.board[r])

	def makeMove(self, column, turn):
		if (self.isValid(column)):
			locationCoord = self.findPlace(column)
			self.board[locationCoord[0]][locationCoord[1]] = turn
			self.diskCount+=1
			return locationCoord
		else:
			raise IncorrectMove("Please select a valid column to drop your disc")

	def findPlace(self, column):
		for i in range(self.rows-1, -1 , -1):
			if (self.board[i][column-1] == "E"):
				return (i, column-1)


	def isValid(self, column):
		if (column > 8 or column < 1):
			return False
		elif (self.board[0][column-1] != "E"):
			return False
		return True

	def playConsoleGame(self):
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


	def checkWin(self, turn):
		return self.checkHorizontal(turn) or self.checkVertical(turn) or self.checkDiagonalTopToBottom(turn) or self.checkDiagonalBottomToTop(turn)

	def checkHorizontal(self, turn):
		for r in self.board:
			count = 0
			for val in r:
				if val == turn:
					count+=1
				else:
					count = 0
				if count == 4:
					return True
		return False

	def checkVertical(self, turn):
		safetyCheck = 0
		for r in range(self.rows):
			for c in range(self.columns):
				if (safetyCheck < 3):
					if (self.board[r][c] == turn and self.board[r+1][c] == turn and self.board[r+2][c] == turn and self.board[r+3][c] == turn):
						return True
			safetyCheck+=1
		return False

	def checkDiagonalTopToBottom(self, turn):
		for r in range(self.rows-3):
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r+1][c+1] == turn and self.board[r+2][c+2] == turn and self.board[r+3][c+3] == turn):
					return True
		return False

	def checkDiagonalBottomToTop(self, turn):
		for r in range(self.rows-1, 2, -1):
			print (r)
			for c in range(self.columns-3):
				if (self.board[r][c] == turn and self.board[r-1][c+1] == turn and self.board[r-2][c+2] == turn and self.board[r-3][c+3] == turn):
					return True
		return False









class IncorrectMove(Exception):
	pass

if __name__ == '__main__':
	runGame = ConnectFour()
	runGame.createBoard()
	runGame.playConsoleGame()

