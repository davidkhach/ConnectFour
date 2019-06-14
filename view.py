# Pygame View of Connect Four
# Fully functioning GUI, simply follow the directions on screen after running
# Choosing a column is as simple as clicking anywhere within a column
# Disks will slowly drop until they land


import pygame
import connectfour
import easyai
import mediumai
import customai
import time

def displayStartScreen():
	""" Displays screen for user to pick game mode, vs AI or vs Human """
	background_colour = (0,179,0)
	(width, height) = (1200, 900)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Connect Four')
	screen.fill(background_colour)
	pygame.draw.rect(screen, (102, 204, 255), [0, 0, 1200, 350])
	pygame.draw.rect(screen, (255,0,0), [70, 450, 450, 100])
	startMessage(screen, 1200, 900)
	playHumanButton(screen, 1200, 900)
	playAIButton(screen, 1200, 900)
	running = True
	pos = None
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				return "END"
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
		if pos != None:
			xpos = pos[0]
			ypos = pos[1]
			if (xpos > 69 and xpos < 519 and ypos > 451 and ypos < 550):
				return "HUMAN"
			elif (xpos > 748 and xpos < 1149 and ypos > 451 and ypos < 550):
				return "AI"
				
			
		pygame.display.flip()

def startMessage(screen, display_width, display_height):
	""" Displays gamemode choice message on screen """
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 80)
	TextSurf, TextRect = text_objects("Connect Four", largeText)
	TextRect.center = ((display_width/2),(display_height-700))
	screen.blit(TextSurf, TextRect)

	largeText2 = pygame.font.Font(pygame.font.get_default_font(), 20)
	TextSurf2, TextRect2 = text_objects("(Click which gamemode you want to play!)", largeText2)
	TextRect2.center = ((display_width/2),(display_height-640))
	screen.blit(TextSurf2, TextRect2)

	pygame.display.update()

def displayAIDifficultyScreen():
	""" Displays three buttons for AI difficulties """
	background_colour = (175,2,255)
	(width, height) = (1200, 900)
	screen = pygame.display.set_mode((width, height))
	screen.fill(background_colour)
	pygame.display.set_caption('Choose the AIs Difficulty!')
	pygame.draw.rect(screen, (58,175,103), [50, 150, 1100, 100])
	displayAIText(screen, 1200, 900)
	#pygame.draw.rect(screen, (102, 204, 255), [0, 0, 1200, 350])
	pygame.draw.rect(screen, (255,250,2), [100, 450, 280, 100])
	pygame.draw.rect(screen, (255,0,0), [460, 650, 280, 100])
	pygame.draw.rect(screen, (255,150,2), [850, 450, 280, 100])
	displayDifficultyOnButton(screen, "Easy", 1200, 900, 960, 400)
	displayDifficultyOnButton(screen, "Medium", 1200, 900, 200, 400)
	displayDifficultyOnButton(screen, "Hard", 1200, 900, 600, 200)
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 20)
	TextSurf, TextRect = text_objects("(Coming Soon)", largeText)
	TextRect.center = ((width/2),(height-165))
	screen.blit(TextSurf, TextRect)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				return "END"
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if pos != None:
					xpos = pos[0]
					ypos = pos[1]
					if (xpos > 99 and xpos < 379 and ypos > 449 and ypos < 551):
						return "EASY"
					elif (xpos > 849 and xpos < 1131 and ypos > 449 and ypos < 551):
						return "MEDIUM"

		pygame.display.flip()

	# To be completed
def displayAIText(screen, display_width, display_height):
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 80)
	TextSurf, TextRect = text_objects("Choose the AIs Difficulty", largeText)
	TextRect.center = ((display_width/2),(display_height-700))
	screen.blit(TextSurf, TextRect)

def displayDifficultyOnButton(screen, difficulty, display_width, display_height, x, y):
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects(difficulty, largeText)
	TextRect.center = ((display_width-x),(display_height-y))
	screen.blit(TextSurf, TextRect)



def playHumanButton(screen, display_width, display_height):
	""" Displays button to click to play against a human """
	pygame.draw.rect(screen, (0,255,0), [750, 450, 400, 100])
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects("Player vs Player", largeText)
	TextRect.center = ((display_width-900),(display_height-400))
	screen.blit(TextSurf, TextRect)


def playAIButton(screen, display_width, display_height):
	""" Displays button to click to play against an AI """
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects("Player vs AI", largeText)
	TextRect.center = ((display_width-250),(display_height-400))
	screen.blit(TextSurf, TextRect)

def chooseDiskColor():
	""" Displays screen for user to pick their disk color by clicking """
	background_colour = (204, 204, 255)
	(width, height) = (1200, 900)
	red = (255, 0, 0)
	yellow = (255, 255, 0)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Choose your color (You always goes first!)')
	screen.fill(background_colour)
	pygame.draw.circle(screen, yellow, (800, 400), 90, 0)
	pygame.draw.circle(screen, red, (400, 400), 90, 0)
	running = True

	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects("Choose your color!", largeText)
	TextRect.center = ((width/2),(height-800))
	screen.blit(TextSurf, TextRect)

	largeText = pygame.font.Font(pygame.font.get_default_font(), 40)
	TextSurf, TextRect = text_objects("(You will always make the first move)", largeText)
	TextRect.center = ((width/2),(height-700))
	screen.blit(TextSurf, TextRect)

	pos = None
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				return "END"
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()

		if (pos != None):
			xpos = pos[0]
			ypos = pos[1]
			if (xpos > 310 and xpos < 491 and ypos > 310 and ypos < 491):
				return "R"
			elif (xpos > 710 and xpos < 890 and ypos > 310 and ypos < 491 ):
				return "Y"

		pygame.display.flip()


def createGrid(gameMode, turn, difficulty):
	""" Displays gamemode and handles the game logic until there is a winner/draw """
	firstTurn = turn
	if (firstTurn == "R"):
		firstTurnColor = (255,0,0)
		secondTurnColor = (255,255,0)
	else:
		firstTurnColor = (255,255,0)
		secondTurnColor = (255,0,0)
	background_colour = (0,0,0)
	(width, height) = (1200, 900)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Connect Four')
	screen.fill(background_colour)
	margin = 10
	w = 120
	h = 120

	line_width = 10
	pygame.draw.rect(screen, (0,255,0), [width-270, 0, width-270, height-70])
	pygame.draw.rect(screen, (255, 200, 0), [0,height-70, width, height-70])

	pygame.draw.rect(screen, (0,0,255), [0,0,width - 270,line_width])
	# bottom line
	pygame.draw.rect(screen, (0,0,255), [0,height - 80,width-270,line_width])
	# left line
	pygame.draw.rect(screen, (0,0,255), [0,0,line_width, height-80])
	# right line
	pygame.draw.rect(screen, (0,0,255), [width-270,0,line_width, height-70])
	running = True
	welcomeMessage(screen, width,height)
	gameTypeMessage(screen, width, height, gameMode)
	game = startGame()
	game.setTurn(firstTurn)
	pos = None
	if (gameMode == "AI"):
		if (difficulty == "MEDIUM"):
			ai = mediumai.MediumAI(secondTurnColor, game)
		elif (difficulty == "EASY"):
			ai = easyai.EasyAI(secondTurnColor, game)
	for column in range(0+margin,720,w+margin):
		for row in range(0+margin,840,h+margin):
			pygame.draw.circle(screen, (255,255,255), (row +70, column + 80), 60, 0)
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()

		turn = game.currentTurn()
		displayCurrentTurn(screen, turn)
		color = None
		clock = pygame.time.Clock()
		if (game.checkDiskCount() == 42):
			displayWinnerMessage(screen, "draw")

		if (turn == "R"):
			color = (255, 0, 0)
		else:
			color = (255,255,0)

		
		if (firstTurn == turn):

			if (pos != None):
				columnChoice = evaluateChoiceByMouseClick(pos)
				if (columnChoice != None):
					coordinates = game.makeMove(columnChoice+1, turn)
					

					if (coordinates != None):
						dropDiskSlowly(screen, columnChoice, color, coordinates, clock)
						pos = None
		else:
			ai.setBoard(game.returnBoard())
			displayCurrentTurn(screen, turn)
			if (gameMode == "AI"):
				move = ai.chooseMove()
	
				coordinates = game.makeMove(move+1, turn)



				dropDiskSlowly(screen, move, color,coordinates, clock)


		if (game.checkWin(turn)):

			displayWinnerMessage(screen, turn)
			quit = False
			while (quit == False):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						quit = True
			running = False
		
		displayCurrentTurn(screen, turn)


		pygame.display.flip()

def gameTypeMessage(screen, display_width, display_height, gameType):
	""" Displays which gamemode you are playing """
	if (gameType == "HUMAN"):
		result = "Player"
	else:
		result = "AI"
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 20)
	TextSurf, TextRect = text_objects("(Player vs " + result + ")", largeText)
	TextRect.center = ((display_width-130),(display_height-750))
	screen.blit(TextSurf, TextRect)

	pygame.display.update()

def startGame():
	""" Returns a connectfour game object """
	playGame = connectfour.ConnectFour()
	playGame.createBoard()
	return playGame


def displayWinnerMessage(screen, turn):
	""" Displays message showing which player won """
	if (turn == "R"):
		winner = "Red Player"
	else:
		winner = "Yellow Player"
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 48)
	if (turn != "draw"):
		TextSurf, TextRect = text_objects("Game Over! " + winner + " Wins!", largeText)
		pygame.display.set_caption("Game Over! " + winner + " Wins!")
	else:
		TextSurf, TextRect = text_objects("Game Over! (Draw) No One Wins!", largeText)
		pygame.display.set_caption("Game Over! (Draw) No One Wins!")
	TextRect.center = ((600),(862))
	screen.blit(TextSurf, TextRect)
	pygame.display.update()


def evaluateChoiceByMouseClick(position):
	""" Calculates which column the human player clicks on and returns the column number """
	columnToDrop = None
	pixelToColumn = {0: [22, 136], 1: [152, 266], 2: [282, 396], 3: [412, 526], 4: [542, 656], 5: [672, 786], 6: [802, 916]}
	xpos = position[0]
	ypos = position[1]
	if (ypos < 801 and ypos > 15):
		for (key, value) in pixelToColumn.items():
			if (xpos > value[0] and xpos < value[1]):
				columnToDrop = key
				return columnToDrop

	
def dropDisk(screen, row, column, color):
	""" Drops a disk on specified row and column """
	pygame.draw.circle(screen, color, ((column*130) + 80, (row *130)+90), 60, 0)

def dropDiskSlowly(screen, columnChoice, color, coordinates, clock):
	""" Drops the disk slowly from the very top until landing on another disk or bottom of board """
	count = 0
	while (count != coordinates[0] + 1):
		clock.tick(6)
		dropDisk(screen, count, columnChoice, color)
		pygame.display.flip()
		dropDisk(screen, count, columnChoice, (255,255,255))
		count+=1
	dropDisk(screen, coordinates[0], columnChoice, color)	

def displayCurrentTurn(screen, turn):
	""" Displays the current turn color on the right side of the screen """
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 23)
	TextSurf, TextRect = text_objects("Current Player's Turn", largeText)
	TextRect.center = ((1070),(600))
	screen.blit(TextSurf, TextRect)
	pygame.draw.circle(screen, (0, 0, 0), (1070, 700), 60, 10)

	if (turn == "R"):
		pygame.draw.circle(screen, (255, 0, 0), (1070, 700), 55, 0)
	else:
		pygame.draw.circle(screen, (255, 255, 0), (1070, 700), 55, 0)
	pygame.display.update()

def text_objects(text, font):
	""" Creates a text object for displaying messages/text blocks """
	textSurface = font.render(text, True, (0,0,0))
	return textSurface, textSurface.get_rect()

def welcomeMessage(screen, display_width, display_height):
	""" Displays welcome message on screen """
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 35)
	TextSurf, TextRect = text_objects("Connect Four", largeText)
	TextRect.center = ((display_width-130),(display_height-800))
	screen.blit(TextSurf, TextRect)

	pygame.display.update()



if __name__ == "__main__":
	
	result = displayStartScreen()
	if (result != "END"):
		playerChoice = chooseDiskColor()
		if (playerChoice != "END"):
			if result == "AI":
				difficulty = displayAIDifficultyScreen()
				if (difficulty != "END"):
					createGrid("AI", playerChoice, difficulty)
			elif result == "HUMAN":
				createGrid("HUMAN", playerChoice, None)