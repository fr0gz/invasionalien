import sys
from time import sleep
import pygame
from bala import Bala
from alien import Alien

def chequear_events_keydown(event, configuracion_ia, pantalla, nave, balas):
	if event.key == pygame.K_RIGHT:		
		nave.mover_derecha = True
	elif event.key == pygame.K_LEFT:
		nave.mover_izquierda = True
	elif event.key == pygame.K_SPACE:
		disparar_bala(configuracion_ia, pantalla, nave, balas)
	elif event.key == pygame.K_q:
		sys.exit()	
					
def disparar_bala(configuracion_ia, pantalla, nave, balas):
	if len(balas) < configuracion_ia.balas_permitidas:			
			nueva_bala = Bala(configuracion_ia, pantalla, nave)
			balas.add(nueva_bala)
					
										
def chequear_events_keyup(event, nave):
	if event.key == pygame.K_RIGHT:
		nave.mover_derecha = False
	elif event.key == pygame.K_LEFT:
		nave.mover_izquierda = False
			
def chequear_events(configuracion_ia, pantalla, estadisticas, tp, boton_jugar, nave, aliens, balas):
	"""Responde a eventos de tecleo y click de teclado"""
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()		
		elif event.type == pygame.KEYDOWN:
			chequear_events_keydown(event, configuracion_ia, pantalla, nave, balas)					
		elif event.type == pygame.KEYUP:
			chequear_events_keyup(event, nave)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			chequear_boton_jugar(configuracion_ia, pantalla, estadisticas, tp, boton_jugar, nave, aliens, balas, mouse_x, mouse_y)
			
def chequear_boton_jugar(configuracion_ia, pantalla, estadisticas, tp, boton_jugar, nave, aliens, balas, mouse_x, mouse_y):
	
	boton_cliqueado = boton_jugar.rect.collidepoint(mouse_x, mouse_y)
	if boton_cliqueado and not estadisticas.juego_activo:
		configuracion_ia.inicializar_configuracion_dinamica()
		pygame.mouse.set_visible(False)
		if boton_jugar.rect.collidepoint(mouse_x, mouse_y):
			estadisticas.resetear_estadisticas()
			estadisticas.juego_activo = True
			
			tp.prep_puntaje()
			tp.prep_puntaje_alto()
			tp.prep_nivel()
			tp.prep_naves()
		
			aliens.empty()
			balas.empty()
		
			crear_flota(configuracion_ia, pantalla, nave, aliens)
			nave.centrar_nave()						
			
def actualizar_pantalla(configuracion_ia, pantalla,estadisticas, tp, nave, aliens, balas, boton_jugar):
	pantalla.fill(configuracion_ia.color_pantalla)
	for bala in balas.sprites():
		bala.dibujar_bala()
	nave.blitme()
	aliens.draw(pantalla)	
	tp.mostrar_puntaje()	
	if not estadisticas.juego_activo:
		boton_jugar.dibujar_boton()
	pygame.display.flip()
		
def actualizar_balas(configuracion_ia,pantalla, estadisticas, tp, nave, aliens, balas):
	balas.update()
	for bala in balas.copy():
		if bala.rect.bottom <= 0:
			balas.remove(bala)
	chequear_colisiones_bala_alien(configuracion_ia, pantalla, estadisticas, tp, nave, aliens, balas)		
			

def chequear_colisiones_bala_alien(configuracion_ia, pantalla, estadisticas, tp, nave, aliens, balas):
	colisiones = pygame.sprite.groupcollide(balas, aliens, True, True)
	
	if colisiones:
		for aliens in colisiones.values():
			estadisticas.puntaje += configuracion_ia.puntos_alien * len(aliens)
			tp.prep_puntaje()
		chequear_puntaje_alto(estadisticas, tp)	 
	
	if len(aliens) == 0:
		balas.empty()
		configuracion_ia.inc_velocidad()
		estadisticas.nivel += 1
		tp.prep_nivel()
		crear_flota(configuracion_ia, pantalla, nave, aliens)
	

def tener_numero_aliens(configuracion_ia, ancho_alien):
	
	espacio_disponible_x = configuracion_ia.ancho_pantalla - 2 * ancho_alien
	numero_aliens_x = int(espacio_disponible_x / (2 * ancho_alien))
	return numero_aliens_x

def tener_numero_filas(configuracion_ia, alto_nave, alto_alien):
	espacio_disponible_y = (configuracion_ia.alto_pantalla - (3 * alto_alien) - alto_nave)
	numero_filas = int(espacio_disponible_y / (2 * alto_alien))
	return numero_filas	
	
def crear_alien(configuracion_ia, pantalla, aliens, numero_alien, numero_filas):
	
	alien = Alien(configuracion_ia, pantalla)
	ancho_alien = alien.rect.width
	alien.x = ancho_alien + 2 * ancho_alien * numero_alien
	alien.rect.x = alien.x 
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_filas
	aliens.add(alien)
						
def crear_flota(configuracion_ia, pantalla, nave, aliens):
	
	alien = Alien(configuracion_ia, pantalla)
	numero_aliens_x = tener_numero_aliens(configuracion_ia, alien.rect.width)
	numero_filas = tener_numero_filas(configuracion_ia, nave.rect.height, alien.rect.height)
	
	for numero_fila in range(numero_filas):
		for numero_alien in range(numero_aliens_x):
			crear_alien(configuracion_ia, pantalla, aliens, numero_alien, numero_fila)

def chequear_aliens_piso(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas):
	screen_rect = pantalla.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			impacto_nave(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas)
			break
			
def actualizar_aliens(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas):
	chequear_bordes_flota(configuracion_ia, aliens)
	aliens.update()
	
	if pygame.sprite.spritecollideany(nave, aliens):
		impacto_nave(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas)
		
	chequear_aliens_piso(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas)	
			
def chequear_bordes_flota(configuracion_ia, aliens):
	for alien in aliens.sprites():
		if alien.chequear_borde():
			cambiar_direccion_flota(configuracion_ia, aliens)
			break

def cambiar_direccion_flota(configuracion_ia, aliens):
	for alien in aliens.sprites():
		alien.rect.y += configuracion_ia.velocidad_descenso_flota
	configuracion_ia.direccion_flota*= -1
	
def impacto_nave(configuracion_ia, estadisticas, tp, pantalla, nave, aliens, balas):
	
	if estadisticas.naves_restantes > 0:
		estadisticas.naves_restantes -= 1
		 	
		tp.prep_naves()
		aliens.empty()
		balas.empty()
	
		crear_flota(configuracion_ia, pantalla, nave, aliens)
		nave.centrar_nave()
	
		sleep(0.5)
		
	else:
		 estadisticas.juego_activo = False
		 pygame.mouse.set_visible(True)
		 
def chequear_puntaje_alto(estadisticas, tp):
	if estadisticas.puntaje > estadisticas.puntaje_alto:
		estadisticas.puntaje_alto = estadisticas.puntaje
		tp.prep_puntaje_alto()	
		
		
			 	
		
	
	
	
	
						
		
	
		
			
								

