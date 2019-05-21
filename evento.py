class Evento:
	def __init__(self,nombre,tiempo,persona = None, quirofano = None, medico = None,enfermeros = None ,arsenaleros = None , apoyos = None ,hospital = None):
		self.nombre = nombre
		self.tiempo = tiempo
		self.persona = persona
		self.quirofano = quirofano 
		self.medico = medico
		self.apoyos = apoyos
		self.enfermeros = enfermeros
		self.arsenaleros = arsenaleros
		self.hospital = hospital