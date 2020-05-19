import pygame.font

class Boton():
	
	def __init__(self, configuracion_ia, pantalla, msg):
		self.pantalla = pantalla
		self.screen_rect = pantalla.get_rect()
		
		self.ancho, self.alto = 200, 50
		
		self.color_boton = (0, 255, 0)
		self.color_texto = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		self.rect = pygame.Rect(0, 0, self.ancho, self.alto)
		self.rect.center = self.screen_rect.center
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.color_texto, self.color_boton)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def dibujar_boton(self,):
		self.pantalla.fill(self.color_boton, self.rect)
		self.pantalla.blit(self.msg_image, self.msg_image_rect)
				
		
