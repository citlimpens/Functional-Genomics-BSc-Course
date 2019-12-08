
#!/usr/bin/python

#Cilalli Limpens

#ejercicio 2 tarea


print "Escribe la secuencia de ADN: ", 
cadena = raw_input();
cadena2 = ''

for ciclos in range(0, len(cadena)):
	if cadena[ciclos] == 'A':
		cadena2 += 'T'
	elif cadena[ciclos] == 'T':
		cadena2 += 'A'
	elif cadena[ciclos] == 'C':
		cadena2 += 'G'
	elif cadena[ciclos] == 'G':
		cadena2 += 'C'

cadenaf = cadena2[::-1]
print cadena 
print cadenaf

if cadenaf == cadena:
	print "la secuencia es palindromica"
else:
	print "la secuencia NO es palindromica"