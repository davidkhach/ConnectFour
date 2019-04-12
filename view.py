import pygame
import connectfour

#pygame.draw.rect(screen,(255,255,255),[column,row,w,h])
def createGrid():
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
	game = startGame()
	pos = None
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
		if (turn == "R"):
			color = (255, 0, 0)
		else:
			color = (255, 255, 0)
		if (pos != None):
			columnChoice = evaluateChoiceByMouseClick(pos)
			coordinates = game.makeMove(columnChoice+1, turn)
			dropDisk(screen, coordinates[0], columnChoice, color)
			#if (game.checkWin(turn)):
			#	running = False;
			pos = None

				# x goes from 22 to 136 for first column, + 130 to 22 and 136 for next column, Y ranges from: 21 to 800
		
		displayCurrentTurn(screen, turn)
		#displayCurrentTurn(screen, "Y")

		pygame.display.flip()


def startGame():
	playGame = connectfour.ConnectFour()
	playGame.createBoard()
	return playGame




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



createGrid()
