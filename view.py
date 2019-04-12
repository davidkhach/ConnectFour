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
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		for column in range(0+margin,720,w+margin):
			for row in range(0+margin,840,h+margin):
				pygame.draw.circle(screen, (255,255,255), (row +70, column + 80), 60, 0)
				dropDisk(screen, 0,0, (255,0,0))
				dropDisk(screen, 1,0, (255,255,0))
				dropDisk(screen, 2,0, (255,0,0))
				dropDisk(screen, 3,0, (255,255,0))
				dropDisk(screen, 0,1, (255,255,0))
				dropDisk(screen, 0,2, (255,0,0))
				dropDisk(screen, 0,3, (255,0,0))


		pygame.display.flip()

def dropDisk(screen, row, column, color):
	#if (row == 1 or column == 1):
	#	pygame.draw.circle(screen,(255,0,0), (10 + 70, 10 + 80), 60, 0)
	pygame.draw.circle(screen, color, ((column*130) + 80, (row *130)+90), 60, 0)	

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
