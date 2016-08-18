def resultado(p,palabra):
	print('\nLa ' + palabra +' de los polinomios:')
	imprimir(poluno)
	imprimir(poldos)
	print('\nDa como resultado:')
	imprimir(p)
	poluno[:] = p[:]
	del poldos[:]

#============================================================================0
def polinomio(poli,n):	#funcion para capturar los coeficientes del polinomio
	del poli[:]
	grado = int(raw_input('\n Ingresa el grado del ' + n + 'polinomio :'))
	print(' Asigna el coeficiente a:')

	for i in range(0,grado+1):
		poli.append(int(raw_input("\tx^" + repr(i) + " : ")))

#============================================================================0
def menu():		#menu del programa
	print(' ===================================================')
	print(' ===================================================')
	print(' \n\n\tOperaciones de polinomios.\n\tElige una opcion:\n')
	print(' 1) Valor en un punto')
	print(' 2) Suma')
	print(' 3) Resta')
	print(' 4) Igualdad')
	print(' 5) Polinomio opuesto')
	print(' 6) Multiplicacion')
	print(' 7) Cambiar polinomio')
	print(' 8) Salir')
	print('\n\tPolinomio Actual:')
	
	imprimir(poluno)

	opcion = {1:valor_pto,2:suma,3:resta,4:igual,5:opuesto,6:multi,7:cambiar,8:salir}
	num = int(raw_input('\nOpcion: '))
	if num <= 0 :
		print('\nEsa opcion no existe, elija una valida.')
		menu()
	elif num >8 :
		print('\nEsa opcion no existe, elija una valida.')
		menu()
	else:
		opcion[num]()

#============================================================================0
def imprimir(p):	#imprime en pantalla el polinomio en forma matematica
	aux=0
	ecuacion=""
	for i in p:
		if aux == 0:
			ecuacion = ecuacion + repr(i)
		elif aux == 1:
			if p[aux] >= 0:
				ecuacion = ecuacion + ' + ' + repr(i) + 'x '
			else:
				ecuacion = ecuacion + ' ' + repr(i) + 'x '
		else:
			if p[aux] >= 0:
				ecuacion = ecuacion + '+ ' + repr(i) + 'x^' + repr(aux) + ' '
			else:
				ecuacion = ecuacion + repr(i) + 'x^' + repr(aux) + ' '
		aux+=1
	print ("\t" + ecuacion)

#============================================================================0
def valor_pto():	#calcular el polinomio en un punto dado
	suma = 0
	exp = 0
	punto = int(raw_input('\nCalcular el polinomio en el punto: '))
	for i in poluno:
		aux = punto ** exp
		exp+=1
		suma = suma + (aux * i) 
	print('\nEl polinomio:')
	imprimir(poluno)
	print('en el punto ' + repr(punto) + ' vale: ' + repr(suma))
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def suma():
	verificar()
	polaux=[]
	aux = 0
	if len(poluno) < len(poldos):
		for i in poldos:
			if aux < len(poluno):
				polaux.append(i + poluno[aux])
			else:
				polaux.append(poldos[aux])
			aux+=1
	
	elif len(poluno) > len(poldos):
		for i in poluno:
			if aux < len(poldos):
				polaux.append(i + poldos[aux])
			else:
				polaux.append(poluno[aux])
			aux+=1
	
	else:
		for i in poluno:
			polaux.append( i + poldos[aux])
			aux+=1

	resultado(polaux,'suma')
	del polaux[:]
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def resta():
	verificar()
	polaux=[]
	aux = 0
	if len(poluno) < len(poldos):
		for i in poldos:
			if aux < len(poluno):
				polaux.append((i*-1) + poluno[aux])
			else:
				polaux.append(poldos[aux]*-1)
			aux+=1
	
	elif len(poluno) > len(poldos):
		for i in poluno:
			if aux < len(poldos):
				polaux.append(i + (poldos[aux]*-1))
			else:
				polaux.append(poluno[aux])
			aux+=1
	
	else:
		for i in poluno:
			polaux.append( i - poldos[aux])
			aux+=1

	resultado(polaux,'resta')
	del polaux[:]
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def igual():
	verificar()
	if poluno == poldos:
		print('\nLos siguientes polinomios:')
		imprimir(poluno)
		imprimir(poldos)
		print('Cumplen con la propiedad de igualdad.')
	else:
		print('\nLos siguientes polinomios:')
		imprimir(poluno)
		imprimir(poldos)
		print('No cumplen la propiedad de igualdad.')
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def opuesto():	#calcular el opuesto del polinomio
	polaux=[]
	for i in poluno:
		polaux.append(-1 * i)
	print('El polinomio opuesto de:')
	imprimir(poluno)
	print('es:')
	imprimir(polaux)
	poluno[:] = polaux
	del polaux[:]
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def multi():
	verificar()
	polaux=[]
	aux = 0
	monomio = 0
	for i in poluno:
		for j in poldos:
			if monomio == 0: 
				polaux.append(0)
			polaux[aux]=((i * j) + polaux[aux])
			aux+=1
		if monomio < (len(poluno) - 1):
			polaux.append(0)
			aux = monomio + 1
		monomio+=1

	resultado(polaux,'multiplicacion')
	del polaux[:]
	raw_input("\nPulsa la tecla 'Enter' para continuar...")
	menu()

#============================================================================0
def salir():
	print('\nHasta pronto!')

#============================================================================0
def cambiar():	#	Cambiar el contenido de los polinomios
	desicion = raw_input('Desea cambiar el polinomio? [y/s] si, [n] no: ')
	if desicion == 'y' or desicion == 's':
		del poluno[:]
		polinomio(poluno,'')
	elif desicion == 'n':
		menu()
	else:
		print('Opcion no valida.')
		menu()

#============================================================================0
def verificar():	#funcion para verificar la existencia del 2do polinomio
	if not poldos:
		polinomio(poldos,'segundo ')

print("\n\tOPERACIONES CON POLINOMIOS DE GRADO 'n'")
print("\n Para comenzar favor de ingresar un polinomio:")

poluno=[]
poldos=[]

polinomio(poluno,'')

menu()