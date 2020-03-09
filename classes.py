"""Classes for MacGyver Labyrinth game"""

import pygame
from pygame.locals import *
from constants import *
from random import randint

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

	def find_holes(self):
		"""This method finds all available holes in the Labyrinth"""
		#We go through the list level
		holes_list = []
		line_nb = 0
		for line in self.structure:
			case_nb = 0
			for sprite in line:
				#Calculating the position of each sprite (in pixels)
				x = case_nb * sprite_size
				y = line_nb * sprite_size
				if sprite == 'h':
					coord = (x, y)
					holes_list.append(coord)
				case_nb += 1
			line_nb += 1
		#Generating 3 random coordinates for our elements and saving them in a list
		elements_list = []
		for i in range(3):
			hole = randint(0, len(holes_list)-1)
			coord_hole = holes_list[hole]
			elements_list.append(coord_hole)
			del holes_list[hole]
		self.elements_list = elements_list
		

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

class Element_Game():
	"""This class creates an element to be picked up by the character"""
	def __init__(self, picture, coord_hole):
		self.picture = pygame.image.load(picture).convert_alpha()
		self.coord_hole = coord_hole
		self.x_pos = self.coord_hole[0]
		self.y_pos = self.coord_hole[1]


class Character():
	"""This class creates MacGyver character and makes him move"""
	#Initializing main character
	def __init__(self, moving, structure):
		#Sprite of the character
		self.structure = structure
		self.moving = pygame.image.load(moving).convert_alpha()
		#Position of the character in cases and pixels
		self.x_case = 0
		self.y_case = 0
		self.x = 0
		self.y = 0

	def move_character(self, move):
		"""This method allows the character to move in any direction"""
		#Moving to the right
		if move == 'right':
			#Verifying the character stays in the earea
			if self.x_case < (sprite_nb_by_side - 1):
				#Checking the sprite is not a wall
				if self.structure[self.y_case][self.x_case+1] != 'w':
					#Moving one case ahead
					self.x_case += 1
					#Calculating the real position in pixel
					self.x = self.x_case * sprite_size
			
		#Moving to the left
		if move == 'left':
			if self.x_case > 0:
				if self.structure[self.y_case][self.x_case-1] != 'w':
					self.x_case -= 1
					self.x = self.x_case * sprite_size

		#Moving up
		if move == 'up':
			if self.y_case > 0:
				if self.structure[self.y_case-1][self.x_case] != 'w':
					self.y_case -= 1
					self.y = self.y_case * sprite_size

		#Moving down
		if move == 'down':
			if self.y_case < (sprite_nb_by_side - 1):
				if self.structure[self.y_case+1][self.x_case] != 'w':
					self.y_case += 1
					self.y = self.y_case * sprite_size


