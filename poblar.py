import xlrd
from hospitales import Hospital
from equipo_medico import Arsenalero , Enfermera , Anestesista , Apoyo
from operacion import Operacion , Quirofano
from medico_paciente import Medico
from parameters import cambiar

loc = ("Datos.xlsx")
wb = xlrd.open_workbook(loc)
sheet_hospitales = wb.sheet_by_index(0)
sheet_especialistas_por = wb.sheet_by_index(1)
sheet_grd = wb.sheet_by_index(2)
sheet_costo1 = wb.sheet_by_index(3)
sheet_costo2 = wb.sheet_by_index(4)
sheet_info1 = wb.sheet_by_index(5)

hospitales_of = []
dic_grd = {}
dic_ponderadores = {}

for fila in range(2,7):
	nombre = str(sheet_hospitales.cell_value(fila, 2))
	horas = cambiar(int(sheet_hospitales.cell_value(fila,3)))
	quirofanos = int(sheet_hospitales.cell_value(fila,4))
	anestesis= int(sheet_hospitales.cell_value(fila,5))
	apoy = int(sheet_hospitales.cell_value(fila,6))
	enferme = int(sheet_hospitales.cell_value(fila,7))
	arsena = int(sheet_hospitales.cell_value(fila,8))
	hospitales_of.append(Hospital(nombre,horas,quirofanos,anestesis,apoy,enferme,arsena))

for hospital in hospitales_of:
	for anestesista in range(hospital.num_anestesistas):
		hospital.anestesistas.append(Anestesista())
	for apoyo in range(hospital.num_apoyo):
		hospital.apoyos.append(Apoyo())
	for enfermera in range(hospital.num_enfermera):
		hospital.enfermeras.append(Enfermera())
	for arsenalero in range(hospital.num_arsenaleros):
		hospital.arsenaleros.append(Arsenalero())

for columna in range(2,7):
	nombre = str(sheet_especialistas_por.cell_value(1,columna))
	for hospital in hospitales_of:
		if hospital.nombre == nombre:
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(2,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(3,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(4,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(5,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(6,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(7,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(8,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(9,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(10,columna)))
			hospital.lista_poblar.append(int(sheet_especialistas_por.cell_value(11,columna)))


for hospital in hospitales_of:
	i=1
	for dato in hospital.lista_poblar:
		for numero in range(dato):
			hospital.medicos.append(Medico("GRD"+ str(i)))
		i+=1

for hospital in hospitales_of:
	for i in range(hospital.num_quirofanos):
		hospital.quirofanos.append(Quirofano())

for fila in range(3,13):
	codigo = "GRD"
	id_ = str(sheet_grd.cell_value(fila, 1))
	nombre = str(sheet_grd.cell_value(fila, 2))
	precio = float(sheet_grd.cell_value(fila, 4))
	especialista = int(sheet_grd.cell_value(fila,5))
	anestesita = int(sheet_grd.cell_value(fila,6))
	apoyo = int(sheet_grd.cell_value(fila,7))
	enfermero = int(sheet_grd.cell_value(fila,8))
	arsenalero = int(sheet_grd.cell_value(fila,9))
	dic_grd[id_] = Operacion(id_,nombre,precio)
	dic_grd[id_].personal["medico"] = especialista
	dic_grd[id_].personal["anestesista"] = anestesita
	dic_grd[id_].personal["apoyo"] = apoyo
	dic_grd[id_].personal["enfermero"] = enfermero
	dic_grd[id_].personal["arsenalero"] = arsenalero
	i=1
	while i<11:
		dic_grd[id_].setup["GRD" + str(i)] = float(sheet_grd.cell_value(fila,i+9))
		i+=1

lista_auxx = [4,3,1,1,1]
i=0
for hospital in hospitales_of:
	dic_ponderadores[hospital.nombre] =  lista_auxx[i]
	i+=1





	










		









