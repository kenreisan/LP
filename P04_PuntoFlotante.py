# -*- coding: 850 -*-
#CVCE Cardoso Valencia Carlos Eric
#HBDG Hernandez Bravo David Gustavo
#RHED Romero Huratado Eduardo David


def main():
	print ("\n\n\t\tCONVERTIDOR DE FORMATO")
	print ("\n Este programa transforma numeros decimales a numeros en")
	print (" formato de almacenamiento binario (simple precisión) y")
	print (" viceversa. Basados en el estándar IEEE 754.\n")


#	try:	#<------ESTA DESACTIVADO PARA QUE MUESTRE LOS ERRORES DE EJECUCION,
			#		HAY QUE ACTIVARLO PARA LA VERSION FINAL Y TODO ESTE BLOQUE
			#		AGREGARLE UNA INDENTACION
	

	numero = float(raw_input(" Ingresa tu numero: "))
	
	if numero < 0 :
		signo = '1'
		numero = (numero * -1)

	else:
		signo = '0'

	if numero == 0 :
		ieee = '00000000000000000000000000000000'

	else:

		decimales = float(numRacional(str(numero)))
		enteros = int(numEntero(str(numero)))

		decBin = calcFlotante(decimales)
		entBin = calcBinario(enteros)

		expDec = exponente(entBin,decBin)
		expBin = calcBinario(expDec)

		mant = calcMantisa(entBin,decBin)
		ieee = puntoFlotante(signo,expBin,mant)
	print (' El numero ' + repr(numero) + ' se representa como:')
	print ("\n S[  EX  ][       MANTISA       ]")
	print (' ' + ieee)

#	CODIGO QUE 'CACHA' ERRORES, ACTIVARLO EN LA FUNCION FINAL:

#	except IOError:
#		print"\nError de entrada/salida."
#	
#	except:
#		print"\nEl numero que ingreso no tiene formato valido.\nIntentelo nuevamente.\n"
#	main()

#=======================================================================================
def numRacional(n):	#divide el numero de la parte etera
	ptos = 0
	decimal = ''

	for i in range(len(n)):		#busca la posicion del punto
		if n[i] == '.':
			ptos=i

	for j in range(ptos,len(n)):
		decimal = (decimal + n[j])

	return decimal

#=======================================================================================
def numEntero(n):	#divide el numero de la parte decimal
	ptos = 0
	entero = ''
	for i in range(len(n)):
		if n[i] == '.':
			ptos=i

	for k in range(0,ptos):
		entero = (entero + n[k])

	return entero

#=======================================================================================
def calcFlotante(f):	#Transforma la parte fraccionaria en binaria
	racional = ''
	i = 0
	while (f>0.0):
		i+=1
		f=f*2
		racional = racional + numEntero(str(f))
		if f>=1 :
			f=f-1

	return racional

#=======================================================================================
def calcBinario(decimal):	#Transforma numeros decimales enteros en binario
	binario = ''
	if decimal >= 1:
		aux = decimal

		while decimal != 1:					#Mientras el cociente sea diferente de 1
			residuo = decimal%2
			binario = str(residuo) + binario
			decimal = (decimal-residuo)/2	#El cociente de la division es el nuevo decimal

		binario = '1' + binario					#Se agrega un 1 por el metodo		
		
		if (aux < 8) and (aux >= 1):			#Completa el el numero de ceros dependiento del tamano en bits 4/8/16
			for i in range(len(binario),4):
				binario = '0' + binario
		elif (aux < 255) and (aux >= 16):
			for i in range(len(binario),8):
				binario = '0' + binario
		elif (aux < 4095) and (aux >= 256):
			for i in range(len(binario),12):
				binario = '0' + binario
		elif (aux < 65535) and (aux >= 4096):
			for i in range(len(binario),16):
				binario = '0' + binario

	else:
		for i in range(0,4):
			binario = binario + '0'
	
	return binario

#=======================================================================================
def exponente(binario,flotante):	#Calcula el exponente del flotante
	desplazamiento = 0
	for i in range(0,len(binario)):	#Busca el primer 'uno' en el binario del entero
		if (binario[i] == '1' and desplazamiento == 0) :
			desplazamiento = len(binario) - (i+1)
			#i=len(binario)

	if desplazamiento == 0 :		#Busca el primer 'uno' en el binario de la parte racional
		for j in range(0,len(flotante)):
			if (flotante[j] == '1' and desplazamiento == 0) :
				desplazamiento = (j+1) * -1
				#j=len(flotante)

	return (desplazamiento + 127)

#=======================================================================================
def calcMantisa(m1,m2):		#Arma la mantisa a 23 bits
	premantisa = ''
	mantisa = ''
	a = 0
	b = 0

	for x in range(0,len(m1)):		#Busca el primer 'uno' del binario del entero
		if (m1[x]=='1' and a == 0):
			a = x+1

	for y in range(0,len(m2)):		#Busca el primer 'uno' del binario del raconal
		if (m2[y]=='1' and b == 0):
			b = y

	if (a > 0):						#Si el numero entero es diferente de 'cero' entonces concatena
		for k in range(a,len(m1)):	#el binario del numero entero y de su parte racional
			premantisa = premantisa + str(m1[k])
		premantisa = premantisa + str(m2)
	
	else:							#Si el numero entero es 'cero' solo concatena el numero binario
		for i in range(b,len(m2)):	#de la parte recional
			premantisa = premantisa + str(m2[i])

	if len(premantisa) > 23 :		#Si el numero de bits es mayor de 23 solo copia los primeros 23
		for i in range(0,23):
			mantisa = mantisa + premantisa[i]
	else:							#Si el numero de bits es menor a 23 copia los bits existentes y rellena con 'ceros'
		for j in range(0,len(premantisa)):
			mantisa = mantisa + premantisa[j]
		for k in range(len(premantisa),23):
			mantisa = mantisa + '0'

	return mantisa

#=======================================================================================
def puntoFlotante(s,e,m):	#Concatena los valores para armar el numero flotante 
	notacion = ''
	notacion = notacion + str(s) + str(e) + str(m)
	return notacion

main()