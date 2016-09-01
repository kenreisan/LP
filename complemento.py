#CVCE Cardoso Valencia Carlos Eric
#RHED Romero Huratado Eduardo David
#HBDG Hernandez Bravo David Gustavo

import os

def menu():
	print(' ===================================================')
	print(' ===================================================')
	print(' \n\n\tComplementos.\n\tElige una opcion:\n')
	print(' 1) Decimal a binario complemento_a1')
	print(' 2) Binario complemento_a1 a decimal')
	print(' 3) Decimal a binario complemento_a2')
	print(' 4) Binario complemento_a2 a decimal')
	print(' 5) Limpiar pantalla')
	print(' 6) Salir del menu')

	opciones = {1:decimal_comp_a1,2:comp_a1_decimal,3:decimal_comp_a2,4:comp_a2_decimal,5:limpiar,6:salir}
	opcion = input('\nOpcion: ')

	try:
		opciones[opcion]()
	except:
		print (" Esa opcion no existe. elige una opcion valida")
		menu()
	

#FUNCIONES DEL MENU
#########################################################################

def decimal_comp_a1():
	decimal = input("Numero decimal: ")
	binario = decimal_binario(decimal)
	complemento_a1 = comp_a1(binario)
	print "BINARIO"
	print binario
	print "Complemento a 1"
	print complemento_a1
	menu()

	
def comp_a1_decimal():
	binario_c1 = raw_input("Binario complemento_a1:")
	binario_c1 = list(binario_c1)					#Conversiona una lista
	binario_c1 = [int(i) for i in binario_c1]		#Lista de enteros
	binario = comp_a1(binario_c1)					#Regreso al binario (intercambiar ceros por unos y unos por ceros)
	decimal = binario_decimal(binario)

	binario.reverse()
	print "BINARIO "
	print binario	
	print "DECIMAL"
	print decimal
	menu()

def decimal_comp_a2():
	d = int(raw_input("Binario a complemento a 2\nIngresa tu numero en base 10: "))
	b = decimal_binario(d)
	print ("BINARIO:")
	print b
	a1 = comp_a1(b)
	a1.reverse()
	a2 = comp_a2(a1)
	a2.reverse()
	print ("COMPLEMENTO A 2:")
	print a2
	menu()

def comp_a2_decimal():
	return 0

def limpiar():
	os.system('cls')

def salir():
	print " "


##########################################

#De decimal a binario
def decimal_binario(decimal):
	binario = []

	while decimal != 1:					#Mientras el cociente sea diferente de 1
		residuo = decimal%2
		binario.append(residuo)			
		decimal = (decimal-residuo)/2	#El cociente de la division es el nuevo decimal

	binario.append(1)					#Se agrega un 1 por el metodo		
	binario.reverse()
	
	return binario

#De binario a decimal
def binario_decimal(binario):
	decimal = 0
	binario.reverse()
	#Se recorre la cadena binaria y se agrega a la variable decimal el valor 2^i
	for i in range(len(binario)):
		if binario[i] == 1:					
			decimal += 2**i

	return decimal

def comp_a1(binario):
	complemento_a1 = []
	for i in range(len(binario)):
		#Se intercambian unos por ceros y ceros por unos
		if binario[i] == 1:
			complemento_a1.append(0)	
		else:
			complemento_a1.append(1)

	return complemento_a1

def comp_a2(binario):
	complemento_a2 = []
	aux = 0				#Bandera para indicar desde donde empieza a cambiar 'unos' por 'ceros'
	for i in range(len(binario)):
		if ((binario[i] == 1) and (aux == 0)):		#Si encuentra el primer '1' pone la bandera y no vuelve a ingresar valores a la lista
			aux=(i+1)
			complemento_a2.append(1)
		elif ((binario[i] == 0) and (aux == 0)):	#Si encuentra un '0' sin haber encontrado al 1er '1' ingresa '0' a la lista
				complemento_a2.append(0)
	for j in range(aux,len(binario)):		#Cambia 'unos' por 'ceros' desde la posicion siguiente donde encontro el 1er 'uno'
		if binario[j] == 1:
			complemento_a2.append(0)
		else:
			complemento_a2.append(1)
	return complemento_a2

menu()