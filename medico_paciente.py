from random import randint , triangular
from parameters import cambiar

class Medico:
	def __init__(self,grd):
		self.grd = grd
		self.estado = False

class Paciente:
	contador_paciente = 0
	def __init__(self,grd):
		self.id = self.contador_paciente
		self.grd = grd
		self._tiempo_max = None
		self.tiempo_op = self.devolver_tiempo()
		self.caracter = None
		Paciente.contador_paciente +=1
		self.devolver_max()



	def devolver_tiempo(self):
		if self.grd == "GRD1":
			return cambiar(randint(*(5,9)))
		if self.grd == "GRD2":
			return cambiar(randint(*(2,5)))
		if self.grd == "GRD3":
			return cambiar(int(triangular(2,5,7)))
		if self.grd == "GRD4":
			return cambiar(randint(*(1,3)))
		if self.grd == "GRD5":
			return cambiar(int(triangular(3,4,6)))
		if self.grd == "GRD6":
			return cambiar(randint(*(1,5)))
		if self.grd == "GRD7":
			return cambiar(int(triangular(1,2,4)))
		if self.grd == "GRD8":
			return cambiar(int(triangular(1,3,4)))
		if self.grd == "GRD9":
			return cambiar(int(triangular(2,6,3)))
		if self.grd == "GRD10":
			return cambiar(randint(*(1,3)))

	def devolver_max(self):
		if self.grd == "GRD1":
			self.tiempo_max = (randint(*(0,2)))
			return cambiar(randint(*(0,2)))
		if self.grd == "GRD2":
			self.tiempo_max = (randint(*(1,5)))
			return cambiar(randint(*(1,5)))
		if self.grd == "GRD3":
			self.tiempo_max = (randint(*(1,7)))
			return cambiar(randint(*(1,7)))
		if self.grd == "GRD4":
			self.tiempo_max = (randint(*(1,9)))
			return cambiar(randint(*(1,9)))
		if self.grd == "GRD5":
			self.tiempo_max = (randint(*(2,12)))
			return cambiar(randint(*(2,12)))
		if self.grd == "GRD6":
			self.tiempo_max = (randint(*(2,14)))
			return cambiar(randint(*(2,14)))
		if self.grd == "GRD7":
			self.tiempo_max = (randint(*(2,16)))
			return cambiar(randint(*(2,16)))
		if self.grd == "GRD8":
			self.tiempo_max = (randint(*(3,19)))
			return cambiar(randint(*(3,19)))
		if self.grd == "GRD9":
			self.tiempo_max = (randint(*(3,21)))
			return cambiar(randint(*(3,21)))
		if self.grd == "GRD10":
			self.tiempo_max = (randint(*(3,23)))
			return cambiar(randint(*(3,23)))

	@property
	def tiempo_max(self):
		return self._tiempo_max
	@tiempo_max.setter
	def tiempo_max(self,p):
		self._tiempo_max = p
	
   
   	



