import pygame
from pygame.sprite import Sprite

class Nave(Sprite):
	
	def __init__(self, configuracion_ia, pantalla):
		
		super(Nave, self).__init__()
		self.pantalla = pantalla
		self.configuracion_ia = configuracion_ia
		
		self.image = pygame.image.load("imagenes/nave.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = pantalla.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		
		self.mover_derecha = False
		self.mover_izquierda = False
		
	def blitme(self):
		self.pantalla.blit(self.image, self.rect)
		
	def actualizar(self):
		
		if self.mover_derecha and self.rect.right < self.screen_rect.right:
			self.center += self.configuracion_ia.factor_velocidad_nave
							
		if self.mover_izquierda and self.rect.left > 0:
			self.center -= self.configuracion_ia.factor_velocidad_nave
			
		self.rect.centerx = self.center
		
	def centrar_nave(self):
		self.center = self.screen_rect.centerx				
