import pygame
import connectfour
import easyai
import mediumai

#pygame.draw.rect(screen,(255,255,255),[column,row,w,h])
def displayStartScreen():
	background_colour = (255,255,255)
	(width, height) = (1200, 900)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Connect Four')
	screen.fill(background_colour)
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
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
		if pos != None:
			xpos = pos[0]
			ypos = pos[1]
			print (pos)
			if (xpos > 69 and xpos < 519 and ypos > 451 and ypos < 550):
				return "HUMAN"
			elif (xpos > 748 and xpos < 1149 and ypos > 451 and ypos < 550):
				return "AI"
				
			
		pygame.display.flip()

def startMessage(screen, display_width, display_height):
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

def playHumanButton(screen, display_width, display_height):
	pygame.draw.rect(screen, (0,255,0), [750, 450, 400, 100])
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects("Player vs Player", largeText)
	TextRect.center = ((display_width-900),(display_height-400))
	screen.blit(TextSurf, TextRect)


def playAIButton(screen, display_width, display_height):
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 50)
	TextSurf, TextRect = text_objects("Player vs AI", largeText)
	TextRect.center = ((display_width-250),(display_height-400))
	screen.blit(TextSurf, TextRect)

def createGrid(gameMode):
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
	pos = None
	if (gameMode == "AI"):
		ai = easyai.EasyAI((255,0,0), game)
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
		color = None
		clock = pygame.time.Clock()
		if (game.checkDiskCount() == 42):
			displayWinnerMessage(screen, "draw")

		


		
		if (turn == "R"):
			#ai.setBoard(game.returnBoard())
			color = (255, 0, 0)
			displayCurrentTurn(screen, turn)
			if (gameMode == "AI"):
				ai.setBoard(game)
				move = ai.chooseMove()
	
				coordinates = game.makeMove(move+1, turn)



				dropDiskSlowly(screen, move, color,coordinates, clock)


		else:
			color = (255, 255, 0)
		if (pos != None):
			columnChoice = evaluateChoiceByMouseClick(pos)
			if (columnChoice != None):
				coordinates = game.makeMove(columnChoice+1, turn)

				if (coordinates != None):
					dropDiskSlowly(screen, columnChoice, color, coordinates, clock)
					pos = None
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
	return 0

def gameTypeMessage(screen, display_width, display_height, gameType):
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
	playGame = connectfour.ConnectFour()
	playGame.createBoard()
	return playGame


def displayWinnerMessage(screen, turn):
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
	pygame.draw.circle(screen, color, ((column*130) + 80, (row *130)+90), 60, 0)

def dropDiskSlowly(screen, columnChoice, color, coordinates, clock):
	count = 0
	while (count != coordinates[0] + 1):
		clock.tick(6)
		dropDisk(screen, count, columnChoice, color)
		pygame.display.flip()
		dropDisk(screen, count, columnChoice, (255,255,255))
		count+=1
	dropDisk(screen, coordinates[0], columnChoice, color)	

def displayCurrentTurn(screen, turn):
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
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def welcomeMessage(screen, display_width, display_height):
	pygame.font.init()
	largeText = pygame.font.Font(pygame.font.get_default_font(), 35)
	TextSurf, TextRect = text_objects("Connect Four", largeText)
	TextRect.center = ((display_width-130),(display_height-800))
	screen.blit(TextSurf, TextRect)

	pygame.display.update()



#createGrid()
result = displayStartScreen()
if result == "AI":
	createGrid("AI")
else:
	createGrid("HUMAN")