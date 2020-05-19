import pygame.font

from pygame.sprite import Group
from nave import Nave


class TablaPuntaje():
	
	def __init__(self, configuracion_ia, pantalla, estadisticas):
		
		self.pantalla = pantalla
		self.screen_rect = pantalla.get_rect()
		self.configuracion_ia = configuracion_ia
		self.estadisticas = estadisticas
		self.color_texto = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		self.prep_puntaje()
		self.prep_puntaje_alto()
		self.prep_nivel()
		self.prep_naves()
		
	def prep_puntaje(self):
		
		puntaje_redondeado = int(round(self.estadisticas.puntaje, -1))
		puntaje_str = "{:,}".format(puntaje_redondeado)
		string_puntaje = str(self.estadisticas.puntaje)
		self.imagen_puntaje = self.font.render(string_puntaje, True, self.color_texto, self.configuracion_ia.color_pantalla)
		self.rect_puntaje = self.imagen_puntaje.get_rect()
		self.rect_puntaje.right = self.screen_rect.right - 20
		self.rect_puntaje.top = 20
		
	def mostrar_puntaje(self):
		self.pantalla.blit(self.imagen_puntaje, self.rect_puntaje)
		self.pantalla.blit(self.puntaje_alto_image, self.puntaje_alto_rect)
		self.pantalla.blit(self.nivel_image, self.nivel_rect)
		self.naves.draw(self.pantalla)
		
	def prep_puntaje_alto(self):
		puntaje_alto = int(round(self.estadisticas.puntaje_alto , -1))
		
		puntaje_alto_str = "{:,}".format(puntaje_alto)
		self.puntaje_alto_image = self.font.render(puntaje_alto_str, True, self.color_texto, self.configuracion_ia.color_pantalla)
		self.puntaje_alto_rect = self.puntaje_alto_image.get_rect()
		self.puntaje_alto_rect.centerx = self.screen_rect.centerx
		self.puntaje_alto_rect.top = self.rect_puntaje.top
		
	def prep_nivel(self):
		self.nivel_image = self.font.render(str(self.estadisticas.nivel), True, self.color_texto, self.configuracion_ia.color_pantalla)
		self.nivel_rect = self.nivel_image.get_rect()
		self.nivel_rect.right = self.rect_puntaje.right
		self.nivel_rect.top = self.rect_puntaje.bottom + 10
		
	def prep_naves(self):
		self.naves = Group()
		for numero_naves in range(self.estadisticas.naves_restantes):
			nave = Nave(self.configuracion_ia, self.pantalla)
			nave.rect.x = 10 + numero_naves * nave.rect.width
			nave.rect.y = 10
			self.naves.add(nave)
			
		
			
		
		
				
		
			
		
		
		
		
