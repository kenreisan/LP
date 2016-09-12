def main():
	try:
		num = float(raw_input("Ingresa tu numero: "))
		dec = int(numDecimal(str(num)))
		ent = int(numEntero(str(num)))
		print "Entero:"
		print ent
		print "Decimal:"
		print dec

	except IOError:
		print"\nError de entrada/salida."
	
	except:
		print"\nEl numero que ingreso no tiene formato valido.\nIntentelo nuevamente.\n"
		main()

#=======================================================================================
def numDecimal(n):	#divide el numero de suparte etera
	ptos = 0
	decimal = ''

	for i in range(len(n)):		#busca la posicion del punto
		if n[i] == '.':
			ptos=i

	for j in range(ptos+1,len(n)):
		decimal = (decimal + n[j])

	return decimal

#=======================================================================================
def numEntero(n):	#divide el numero de suparte decimal
	ptos = 0
	entero = ''
	for i in range(len(n)):
		if n[i] == '.':
			ptos=i

	for k in range(0,ptos):
		entero = (entero + n[k])

	return entero

main()