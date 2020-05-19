import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	
	def __init__(self, configuracion_ia, pantalla):
		super(Alien, self).__init__()
		self.pantalla = pantalla
		self.configuracion_ia = configuracion_ia
		
		self.image = pygame.image.load("imagenes/alien.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = pantalla.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.pantalla.blit(self.image, self.rect)
	
	def chequear_borde(self):
		rect_pantalla = self.pantalla.get_rect()
		if self.rect.right >= rect_pantalla.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def update(self):
		self.x += (self.configuracion_ia.factor_velocidad_alien * self.configuracion_ia.direccion_flota)
		self.rect.x = self.x
		
	
				 	
			
