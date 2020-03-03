"""Classes for MacGyver Labyrinth game"""

import pygame
from pygame.locals import *
from constants import *
from random import *

class Level():
	"""This class will generate the sprites and will find the empty ones 
	where the 3 objects will be generated"""
	
	def __init__(self, file_level):
		self.file_level = file_level
		self.structure = 0
		self.elements_list = []
	
	def genererate_level(self):
		"""This method generates the content depending on the file content.
		We create a general list containing a list for each line to show."""
		# We go through each line of the list
		with open(self.file_level, "r") as file:
			structure_level = []	#empty list
			#We go through each line of the file
			for line in file:
				line_level = []
				#We go through each sprite contained in each line
				for sprite in line:
					#We ignore the end of each line
					if sprite != '\n':
						#We add the sprite to the list
						line_level.append(sprite)
				#We add the line to the list
				structure_level.append(line_level)
			#We save the structure
			self.structure = structure_level

	#def find_holes
	
		

	def display_level(self, canvas):
		"""This method shows the sprites"""
		wall = pygame.image.load(wall_pic).convert()
		departure = pygame.image.load(start_pic).convert()
		arrival = pygame.image.load(finish_pic).convert_alpha()
		#We go through the list level
		line_nb = 0
		for line in self.structure:
			case_nb = 0
			for sprite in line:
				#Calculating the position of each sprite (in pixels)
				x = case_nb * sprite_size
				y = line_nb * sprite_size
				if sprite == 'w':          #w = Wall
					canvas.blit(wall, (x,y))
				elif sprite == 's':        #s = Start
					canvas.blit(departure, (x,y))
				elif sprite == 'e':        #e = Ending
					canvas.blit(arrival, (x,y))
				case_nb += 1
			line_nb += 1

#class Element_Game


#class Character
