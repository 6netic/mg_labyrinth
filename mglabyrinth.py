"""
Labyrinth game with MacGyver Character
You must move the character to reach the guardian BUT you must catch the 3 elements before
Python Script
Files : mglabyrinth.py, classes.py, constantes.py and n1 file.
"""

# Encoding lines utf-8
# -*- coding: utf8 -*-

# Importing needed modules
import pygame
from pygame.locals import *
from constants import *
from classes import *

#Initializing PyGame
pygame.init()

#Opening PyGame Canvas
canvas = pygame.display.set_mode((canvas_side_size, canvas_side_size + 60))

# Canvas title
pygame.display.set_caption(canvas_title)

#Showing Welcome screen
welcome = pygame.image.load(welcome_pic).convert()
canvas.blit(welcome, (0, 0))
pygame.display.flip()


#MAIN LOOP
running = True
while running:
	
	pygame.time.Clock().tick(30)
	
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			running = False
		
		elif event.type == KEYDOWN:
			if event.key == K_F1:
				first, second, third = False, False, False
				canvas.fill((0, 0, 0))
				pygame.display.update()
				#Loading the background
				background = pygame.image.load(background_pic).convert()
				canvas.blit(background, (0,0))
				
				level = Level('n1')
				level.genererate_level()
				level.display_level(canvas)
				#level.find_holes()
			
				#Adding the 3 elements
				

				#Integrating the structure to Character class
				

			
			#Moving the character
			
				
				#Displaying the new position and the 3 elements after each move
					   
				
			#Picking up each element and move it to bottom:
			
			
			#Victory -> back to welcome screen
			
				#Game is lost!
				
							#Game is won
							
				
					
			pygame.display.flip()
	
pygame.quit()
















































