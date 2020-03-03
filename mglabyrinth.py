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

#Canvas title
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
				level.find_holes()
			
				#Adding the 3 elements
				object1 = level.elements_list[0]
				element1 = Element_Game("Images/tube.png", object1)
				canvas.blit(element1.picture, (element1.x_pos, element1.y_pos))
				level.structure[int(element1.y_pos/30)][int(element1.x_pos/30)] = 'tube'

				object2 = level.elements_list[1]
				element2 = Element_Game("Images/syringe.png", object2)
				canvas.blit(element2.picture, (element2.x_pos, element2.y_pos))
				level.structure[int(element2.y_pos/30)][int(element2.x_pos/30)] = 'syringe'

				object3 = level.elements_list[2]
				element3 = Element_Game("Images/ether.png", object3)
				canvas.blit(element3.picture, (element3.x_pos, element3.y_pos))
				level.structure[int(element3.y_pos/30)][int(element3.x_pos/30)] = 'ether'

				#Integrating the structure to Character class
				mcgyver = Character("Images/MacGyver.png", level.structure)
				canvas.blit(mcgyver.moving, (mcgyver.x, mcgyver.y))

			
			#Moving the character
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					mcgyver.move_character('right')
				elif event.key == K_LEFT:
					mcgyver.move_character('left')
				elif event.key == K_UP:
					mcgyver.move_character('up')
				elif event.key == K_DOWN:
					mcgyver.move_character('down')
				
				#Displaying the new position and the 3 elements after each move
				canvas.blit(background, (0,0))
				level.display_level(canvas)
				canvas.blit(element1.picture, (element1.x_pos, element1.y_pos))
				canvas.blit(element2.picture, (element2.x_pos, element2.y_pos))
				canvas.blit(element3.picture, (element3.x_pos, element3.y_pos))
				canvas.blit(mcgyver.moving, (mcgyver.x, mcgyver.y))
				pygame.display.flip()	   
				
			#Picking up each element and move it to bottom:
			if level.structure[mcgyver.y_case][mcgyver.x_case] == 'tube':
				first = True
				element1 = Element_Game("Images/transparent.png", object1)
				canvas.blit(element1.picture, (element1.x_pos, element1.y_pos))
				found_pic1 = pygame.image.load("Images/tube.png").convert()
				canvas.blit(found_pic1, (150, 480))
				pygame.display.flip()
			
			
			if level.structure[mcgyver.y_case][mcgyver.x_case] == 'syringe':
				second = True
				element2 = Element_Game("Images/transparent.png", object2)
				canvas.blit(element2.picture, (element2.x_pos, element2.y_pos))
				found_pic2 = pygame.image.load("Images/syringe.png").convert()
				canvas.blit(found_pic2, (210, 480))
				pygame.display.flip()
				
			
			if level.structure[mcgyver.y_case][mcgyver.x_case] == 'ether':
				third = True
				element3 = Element_Game("Images/transparent.png", object3)
				canvas.blit(element3.picture, (element3.x_pos, element3.y_pos))
				found_pic3 = pygame.image.load("Images/ether.png").convert()
				canvas.blit(found_pic3, (260, 480))
				pygame.display.flip()
			
			#Victory -> back to welcome screen
			if level.structure[mcgyver.y_case][mcgyver.x_case] == 'e':
				won = pygame.image.load(won_pic).convert()
				canvas.blit(won, (0,0))
			pygame.display.flip()	

pygame.quit()
















































