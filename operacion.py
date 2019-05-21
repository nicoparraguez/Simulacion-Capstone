class Operacion:
	def __init__(self,grd,nombre,costo_privado):
		self.grd = grd
		self.nombre = nombre
		self.costo_privado = costo_privado
		self.personal = {}
		self.setup = {}

class Quirofano:
	def __init__(self):
		self.estado = False
		self.equipo_asignado = {}
		self.operacion_actual = None
		self.numero_operaciones = 0