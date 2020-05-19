class Configuracion():
	"""Una clase que almacena la config. de Invasion Alien"""
	
	def __init__(self):
		self.ancho_pantalla=800
		self.alto_pantalla=600
		self.color_pantalla=(230,230,230)
		self.factor_velocidad_nave = 1.5
		self.limite_naves = 3
		
		#Configuracion de la bala
		self.factor_velocidad_bala = 3
		self.ancho_bala = 3
		self.alto_bala = 15
		self.color_bala = 60, 60, 60
		self.balas_permitidas = 3
		
		self.factor_velocidad_alien = 1
		self.velocidad_descenso_flota = 10
		self.direccion_flota = 1
		
		self.escala_aceleracion = 1.1
		self.escala_puntaje = 1.5
		self.inicializar_configuracion_dinamica()
		
	def inicializar_configuracion_dinamica(self):
		self.factor_velocidad_nave = 1.5
		self.factor_velocidad_bala = 1.5	
		self.factor_velocidad_alien = 1
		self.direccion_flota = 1
		self.puntos_alien = 10
		
	def inc_velocidad(self):
		
		self.factor_velocidad_nave *= self.escala_aceleracion
		self.factor_velocidad_alien *= self.escala_aceleracion
		self.factor_velocidad_bala *= self.escala_aceleracion
		self.puntos_alien *=  int(self.puntos_alien * self.escala_puntaje)
		print(self.puntos_alien) 
		
		
			
		
			
