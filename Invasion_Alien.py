import sys 
import pygame
from pygame.sprite import Group
from configuracion_IA import Configuracion
from nave import Nave
from alien import Alien
from Estadisticas_del_juego import EstadisticasJuego
from tabla_puntaje import TablaPuntaje
from boton import Boton
import funciones_juego as fj

def correr_juego():
	pygame.init()
	configuracion_ia = Configuracion()
	pantalla = pygame.display.set_mode(
		(configuracion_ia.ancho_pantalla, configuracion_ia.alto_pantalla))
	pygame.display.set_caption("Invasion Alien")
	boton_jugar = Boton(configuracion_ia, pantalla , "Jugar!")
	estadisticas = EstadisticasJuego(configuracion_ia)
	tp = TablaPuntaje(configuracion_ia, pantalla, estadisticas)
	nave = Nave(configuracion_ia, pantalla)
	balas = Group()
	aliens = Group()
	
	fj.crear_flota(configuracion_ia, pantalla, nave, aliens)
	
	while True:
		
		fj.chequear_events(configuracion_ia, pantalla, estadisticas, tp, boton_jugar, nave, aliens, balas)
		if estadisticas.juego_activo:			
			nave.actualizar()
			fj.actualizar_balas(configuracion_ia,pantalla, estadisticas, tp, nave, aliens, balas)	
			fj.actualizar_aliens(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas)			
		fj.actualizar_pantalla(configuracion_ia, pantalla, estadisticas, tp, nave, aliens, balas, boton_jugar)
							
correr_juego()

