from poblar import hospitales_of , dic_grd , dic_ponderadores
from medico_paciente import Paciente
from evento import *
from parameters import *
from random import randint , choice , normalvariate
import numpy as np

#hospitales_of lista de los hospitales
#dic_grd diccionario con info de los grd


class Hospitaland:

	Texto = "{} |{} | {} | {}\n"
	
	with open("log.txt", "w", encoding="UTF-8") as file:
		file.write("Bienvenido A Hospitaland\n")
		file.write("\n\n")



	def __init__(self,limite):
		self.eventos = []
		self.metodos = {"comenzar_dia":self.comenzar_dia, "terminar_primera_operacion":self.terminar_primera_operacion,"terminar_dia" : self.terminar_dia }
		self.limite = limite
		self.dia = 1
		self.tiempo_actual = 0
		self.tiempo_maximo = 720
		self.hospitales = hospitales_of
		self.dic_grd = dic_grd
		self.gasto = 0
		self.privado = 0
		self.operado = 0
		self.esperando = 0
		self.privado_dic = {"GRD1":0 ,"GRD2":0 ,"GRD3":0 ,"GRD4":0 ,"GRD5":0 ,"GRD6":0 ,"GRD7":0 ,"GRD8":0 ,"GRD9":0 ,"GRD10":0  }

	def escribir_evento(self,dia,minuto,paciente,hospital):
		with open("log.txt", mode="a", encoding="UTF-8") as file:
			file.write(self.Texto.format(dia,minuto,paciente,hospital))

	def comenzar_dia(self,evento):
		i=0
		lista_aux = [CR_GRD1,CR_GRD2,CR_GRD3,CR_GRD4,CR_GRD5,CR_GRD6,CR_GRD7,CR_GRD8,CR_GRD9,CR_GRD10]
		lista_gen = []
		lista_personas = []
		while i <10 :
			a = np.random.poisson(lista_aux[i])
			lista_gen.append(a)
			i+=1
		valor = 1
		for numero in lista_gen:
			a = 1
			lista_aux2 = []
			while a<numero:
				lista_aux2.append(Paciente("GRD"+str(valor)))
				a+=1
			valor+=1			
			lista_personas.append(lista_aux2)
		for lista in lista_personas:
			cantidad = len(lista)
			parte1 = cantidad //10
			parte2 = cantidad % 10
			contador = 0
			for nombre in dic_ponderadores:
				for hospital in self.hospitales:
					if hospital.nombre == nombre:
						i=1
						while i<parte1 * dic_ponderadores[nombre]+ 1:
							persona = lista.pop()
							hospital.pacientes.append(persona)
							i+=1
						if dic_ponderadores[nombre] == 1:
							contador +=1
							numero = randint(*(0,parte2))
							parte2-=numero
							j=1
							if contador<3:
								while j<numero+1:
									persona = lista.pop()
									hospital.pacientes.append(persona)
									j+=1
							else:
								for b in range(parte2):
									persona = lista.pop()
									hospital.pacientes.append(persona)

		self.primera_operacion()
		self.eventos.append(Evento("terminar_dia",self.tiempo_maximo))

		
		

	def terminar_dia(self,evento):
		if self.dia < self.limite:
			self.escribir_evento(self.dia,self.tiempo_actual,"aa","bb")
			self.setear()
			self.update()
			self.eventos = []
			self.dia +=1
			self.tiempo_actual = 0
			self.eventos.append(Evento("comenzar_dia",0))

		else:
			for hospital in self.hospitales:
				self.esperando += len(hospital.pacientes)



	def primera_operacion(self):
		for hospital in self.hospitales:
			i=0
			while self.se_puede_operar_apoyos(hospital) and i<30:
				persona = choice(hospital.pacientes)
				if self.grd_se_puede_medico(hospital, persona.grd) and self.grd_se_puede_equipo(hospital,persona.grd) and self.grd_se_puede_quirofano(hospital):
					index = hospital.pacientes.index(persona)
					hospital.pacientes.pop(index)
					medico = self.devolver_medico(hospital,persona.grd)
					apoyos = self.devolver_apoyos(hospital,self.dic_grd[persona.grd].personal["apoyo"])
					enfermeros = self.devolver_enfermeras(hospital,self.dic_grd[persona.grd].personal["enfermero"])
					arsenaleros = self.devolver_arsenaleros(hospital,self.dic_grd[persona.grd].personal["arsenalero"])
					quirofano = self.devolver_quirofano(hospital)
					self.escribir_evento(self.dia,self.tiempo_actual,persona.grd,hospital.nombre)
					self.eventos.append(Evento("terminar_primera_operacion",self.tiempo_actual + persona.tiempo_op,medico = medico,persona = persona, quirofano = quirofano,enfermeros = enfermeros,arsenaleros = arsenaleros , apoyos = apoyos , hospital= hospital))
				i+=2









	def terminar_primera_operacion(self,evento):
		self.escribir_evento(self.dia,evento.tiempo,evento.persona.id,evento.hospital.nombre)
		evento.quirofano.numero_operaciones+=1
		evento.quirofano.operacion_actual = evento.persona.grd
		evento.quirofano.estado = False
		evento.medico.estado = False
		for apoyo in evento.apoyos:
			apoyo.estado = False
		for enfermera in evento.enfermeros:
			enfermera.estado = False
		for arsenalero in evento.arsenaleros:
			arsenalero.estado = False
		evento.quirofano.numero_operaciones +=1
		self.operado +=1
		self.operaciones_loop(evento.hospital)


	def operaciones_loop(self,hospital):
		lista = self.devolver_grd_posibles(hospital)
		while len(lista)>0:
			grd_e= choice(lista)
			index1 = lista.index(grd_e)
			lista.pop(index1)
			lista_aux = list(filter(lambda x : x.grd == grd_e,hospital.pacientes))
			while len(lista_aux)>0:
				paciente = choice(lista_aux)
				index2 = lista_aux.index(paciente)
				lista_aux.pop(index2)
				quirofano = self.devolver_quirofano(hospital)
				if quirofano != 0:
					if self.tiempo_actual + paciente.tiempo_op + self.devolver_setup(quirofano,grd_e) <= hospital.horas and self.grd_se_puede_medico(hospital,grd_e) and self.grd_se_puede_equipo(hospital,grd_e):
						index3 = hospital.pacientes.index(paciente)
						hospital.pacientes.pop(index3)
						medico = self.devolver_medico(hospital,paciente.grd)
						apoyos = self.devolver_apoyos(hospital,self.dic_grd[paciente.grd].personal["apoyo"])
						enfermeros = self.devolver_enfermeras(hospital,self.dic_grd[paciente.grd].personal["enfermero"])
						arsenaleros = self.devolver_arsenaleros(hospital,self.dic_grd[paciente.grd].personal["arsenalero"])
						self.escribir_evento(self.dia,self.tiempo_actual,paciente.id,hospital.nombre)
						self.eventos.append(Evento("terminar_primera_operacion",self.tiempo_actual + paciente.tiempo_op + self.devolver_setup(quirofano,grd_e),medico = medico,persona = paciente, quirofano = quirofano,enfermeros = enfermeros,arsenaleros = arsenaleros , apoyos = apoyos , hospital= hospital))



	
	def devolver_setup(self,quirofano,grd):
		if quirofano.operacion_actual != None:
			return cambiar(self.dic_grd[quirofano.operacion_actual].setup[grd])
		return 0

	def setear(self):
		for hospital in self.hospitales:
			for element in hospital.medicos:
				element.estado = False
			for element in hospital.anestesistas:
				element.estado = False
			for element in hospital.arsenaleros:
				element.estado = False
			for element in hospital.apoyos:
				element.estado = False
			for element in hospital.enfermeras:
				element.estado = False
			for element in hospital.quirofanos:
				element.estado = False
	def update(self):
		for hospital in self.hospitales:
			for element in hospital.pacientes:
				element.tiempo_max -=1
				if element.tiempo_max < 0 :
					index = hospital.pacientes.index(element)
					hospital.pacientes.pop(index)
					self.gasto += self.dic_grd[element.grd].costo_privado
					self.privado_dic[element.grd]+=1
					self.privado +=1








		

		

	def devolver_grd_posibles(self,hospital):
		a = 0
		b = 0 
		c = 0
		for element in hospital.arsenaleros:
			if element.estado == False:
				a+=1
		for element in hospital.enfermeras:
			if element.estado ==False:
				b+=1
		for element in hospital.apoyos:
			if element.estado ==False:
				c+=1
		
		lista = []
		for element in self.dic_grd:
			if self.dic_grd[element].personal["arsenalero"] <=a and self.dic_grd[element].personal["enfermero"] <=b and self.dic_grd[element].personal["apoyo"] <=c :
				lista.append(element)
				
		return lista



	










	def se_puede_operar_apoyos(self,objeto):
		arsenaleros1 = 1
		apoyos1 = 1
		enfermeras1 = 2
		ap = 0
		bp = 0
		cp = 0
		for element in objeto.arsenaleros:
			if element.estado == False:
				ap+=1
		for element in objeto.enfermeras:
			if element.estado == False:
				bp+=1
		for element in objeto.apoyos:
			if element.estado == False:
				cp+=1
		if cp<apoyos1 or bp<enfermeras1 or ap<arsenaleros1:
			return False
		
		return True

	def grd_se_puede_medico(self,hospital,grd):
		for element in hospital.medicos:
			if element.grd == grd:
				if element.estado == False:
					return True
		return False

	def grd_se_puede_equipo(self,hospital,grd):
		a = 0
		b = 0
		c = 0
		for element in hospital.arsenaleros:
			if element.estado ==False:
				a+=1
		for element in hospital.enfermeras:
			if element.estado ==False:
				b+=1
		for element in hospital.apoyos:
			if element.estado == False:
				c+=1
		if a>=self.dic_grd[grd].personal["arsenalero"] and b>= self.dic_grd[grd].personal["enfermero"] and c>=self.dic_grd[grd].personal["apoyo"]:
			return True
		return False

	def grd_se_puede_quirofano(self,hospital):
		for element in hospital.quirofanos:
			if element.estado == False:
				return True
		else:
			return False
	def devolver_medico(self,hospital,grd):
		for element in hospital.medicos:
			if element.grd == grd:
				element.estado = True
				return element

	def devolver_enfermeras(self,hospital,numero):
		i=0
		lista = []
		for element in hospital.enfermeras:
			if element.estado == False:
				element.estado = True
				lista.append(element)
				i+=1
			if numero == i :
				return lista
	def devolver_apoyos(self,hospital,numero):
		i=0
		lista = []
		for element in hospital.apoyos:
			if element.estado == False:
				element.estado = True
				lista.append(element)
				i+=1
			if numero == i :
				return lista
	def devolver_arsenaleros(self,hospital,numero):
		i=0
		lista = []
		for element in hospital.arsenaleros:
			if element.estado == False:
				element.estado = True
				lista.append(element)
				i+=1
			if numero == i :
				return lista
	def devolver_quirofano(self,hospital):
		for element in hospital.quirofanos:
			if element.estado == False:
				element.estado = True
				return element
		return 0









	def run(self):
		self.eventos.append(Evento("comenzar_dia", self.tiempo_actual))
		while self.eventos and self.tiempo_actual <= self.tiempo_maximo:
			self.eventos.sort(key=lambda evento: evento.tiempo)
			evento = self.eventos.pop(0)
			self.tiempo_actual = evento.tiempo
			if evento.tiempo <= self.tiempo_maximo:
				self.metodos[evento.nombre](evento)



if __name__ == '__main__':
	a = Hospitaland(30)
	a.run()
	print(a.gasto,a.privado,a.operado,a.esperando)
	print(a.privado_dic)




