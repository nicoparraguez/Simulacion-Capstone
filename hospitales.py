class Hospital:
	def __init__(self,nombre,horas,num_quirofanos,anes,apoy,enfe,arse):
		self.nombre = nombre
		self.horas = horas
		self.num_quirofanos = num_quirofanos
		self.num_anestesistas = anes
		self.num_apoyo = apoy
		self.num_enfermera = enfe
		self.num_arsenaleros = arse
		self.lista_poblar = []
		self.medicos = []
		self.anestesistas = []
		self.arsenaleros =[]
		self.apoyos = []
		self.quirofanos = []
		self.enfermeras = []
		self.pacientes =[]
