#CVCE Cardoso Valencia Carlos Eric
#RHED Romero Huratado Eduardo David
#HBDG Hernandez Bravo David Gustavo

#import os 	#<----- LO ELIMINE PORQUE SOLO SIRVE PARA SISTEMAS WINDOWS [EDRH]

def menu():
	print(' ===================================================')
	print(' ===================================================')
	print(' \n\n\tComplementos.\n\tElige una opcion:\n')
	print(' 1) Decimal -> C1')
	print(' 2) Decimal -> C2')
	print(' 3) C1      -> Decimal')
	print(' 4) C2      -> Decimal')
	print(' 5) Limpiar pantalla')
	print(' 6) Salir del menu')

	opciones = {1:decimal_comp_a1,3:comp_a1_decimal,2:decimal_comp_a2,4:comp_a2_decimal,5:limpiar,6:salir}
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
	print "\nBINARIO"
	print binario
	print "Complemento a 1"
	print complemento_a1
	raw_input("\nPresione 'Intro' para continuar...")
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
	raw_input("\nPresione 'Intro' para continuar...")
	menu()

def decimal_comp_a2():
	d = int(raw_input("Decimal a C2\nIngresa tu numero en base 10: "))
	b = decimal_binario(d)								
	print ("\nBINARIO:")
	print b
	b.reverse()
	a2 = comp_a2(b)
	a2.reverse()
	print ("COMPLEMENTO A 2:")
	print a2
	raw_input("\nPresione 'Intro' para continuar...")
	menu()

def comp_a2_decimal():
	c2 = raw_input("C2 a Decimal\nIngresa tu numero en C2: ")
	c2 = list(c2)		
	c2 = [int(i) for i in c2]

	binario = comp_a1(c2)
	binario.reverse()
	suma = suma_binaria(binario)
	suma.reverse()
	decimal = binario_decimal(suma)
	binario.reverse()
	print "BINARIO "
	print suma	
	print "DECIMAL"
	print decimal
	raw_input("\nPresione 'Intro' para continuar...")
	menu()

def limpiar():
#	os.system('cls')	#<---SOLO FUNCIONA PARA WINDOWS [EDRH]
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")	#<----NO ES BONITA PERO "LIMPIA" [EDRH]
	menu()

def salir():
	print "Hasta pronto!"


#FUNCIONES AUXILIARES ESPECIFICAS
#########################################################################

#De decimal a binario
def decimal_binario(decimal):
	binario = []
	if decimal >= 1:
		aux = decimal

		while decimal != 1:					#Mientras el cociente sea diferente de 1
			residuo = decimal%2
			binario.append(residuo)			
			decimal = (decimal-residuo)/2	#El cociente de la division es el nuevo decimal

		binario.append(1)					#Se agrega un 1 por el metodo		
		
		if (aux < 8) and (aux >= 1):			#Completa el el numero de ceros dependiento del tamano en bits 4/8/16
			for i in range(len(binario),4):
				binario.append(0)
		elif (aux < 255) and (aux >= 16):
			for i in range(len(binario),8):
				binario.append(0)
		elif (aux < 4095) and (aux >= 256):
			for i in range(len(binario),12):
				binario.append(0)
		elif (aux < 65535) and (aux >= 4096):
			for i in range(len(binario),16):
				binario.append(0)	
		binario.reverse()
	else:
		for i in range(0,4):
			binario.append(0)		
	
	return binario

#De binario a decimal
def binario_decimal(binario):
	decimal = 0
	binario.reverse()
	if len(binario)>1:							#Se recorre la cadena binaria y se agrega a la variable decimal el valor 2^i
		for i in range(len(binario)):
			if binario[i] == 1:					
				decimal += 2**i
	else:
		decimal = 0
	return decimal


#TRANSFORMA UN BINARIO A SU C1
def comp_a1(binario):
	complemento_a1 = []
	for i in range(len(binario)):				#Se intercambian unos por ceros y ceros por unos
		if binario[i] == 1:
			complemento_a1.append(0)	
		else:
			complemento_a1.append(1)

	return complemento_a1


#TRANSFORMA UN BINARIO A SU C2
def comp_a2(binario):
	complemento_a2 = []
	aux = 0											#Bandera para indicar desde donde empieza a cambiar 'unos' por 'ceros'
	for i in range(len(binario)):
		if ((binario[i] == 1) and (aux == 0)):		#Si encuentra el primer '1' pone la bandera y no vuelve a ingresar valores a la lista
			aux=(i+1)
			complemento_a2.append(1)
		elif ((binario[i] == 0) and (aux == 0)):	#Si encuentra un '0' sin haber encontrado al 1er '1' ingresa '0' a la lista
				complemento_a2.append(0)
	if aux != 0 :
		for j in range(aux,len(binario)):			#Cambia 'unos' por 'ceros' desde la posicion siguiente donde encontro el 1er 'uno'
			if binario[j] == 1:
				complemento_a2.append(0)
			else:
				complemento_a2.append(1)
	return complemento_a2


#SUMA UN '1' A UNA CIFRA BINARIA
def suma_binaria(b):
	suma = []
	aux = 0
	suma = b

	for i in range(len(b)):					#Ciclo que va revisando la lista y cambia 'unos' por 'ceros', se detiene cuando
		if aux == 0 and suma[i] == 1:		#encuentra el primer 'cero'
			suma[i] = 0
		elif aux == 0 and suma[i]== 0:
			aux+=1
			suma[i] = 1
	return suma

menu()