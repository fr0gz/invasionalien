class EstadisticasJuego():
	
	def __init__(self, configuracion_ia):
		
		self.configuracion_ia = configuracion_ia
		self.resetear_estadisticas()
		self.juego_activo = False
		self.puntaje_alto = 0
		
		
	def resetear_estadisticas(self):
		
		self.naves_restantes = self.configuracion_ia.limite_naves
		self.puntaje = 0
		self.nivel = 1	
		
	 
		
