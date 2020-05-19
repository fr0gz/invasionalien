import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
	
	def __init__(self, configuracion_ia, pantalla, nave):
		super(Bala, self).__init__()
		self.pantalla = pantalla
		
		self.rect = pygame.Rect(0, 0, configuracion_ia.ancho_bala, configuracion_ia.alto_bala)
		self.rect.centerx = nave.rect.centerx
		self.rect.top = nave.rect.top
		
		self.y = float(self.rect.y)
		
		self.color = configuracion_ia.color_bala
		self.factor_velocidad = configuracion_ia.factor_velocidad_bala
		
	def update(self):
		self.y -= self.factor_velocidad
		self.rect.y = self.y
		
	def dibujar_bala(self):
		pygame.draw.rect(self.pantalla, self.color, self.rect)		
