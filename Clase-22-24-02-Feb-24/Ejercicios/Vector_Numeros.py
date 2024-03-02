lista = [1,5,-8,-23, 4,9,-56,0]
lista_positiva = []
lista_negativa = []
for i in lista:
    if i > 0:
        lista_positiva.append(i)
    elif i == 0:
        print('Este numero no es ni positivo ni negativo ==> ' + str(i))
    else:
        lista_negativa.append(i)
print('Estos son los numeros positivos ==> ' + str(lista_positiva))
print('Estos son los numeros negativos ==> ' + str(lista_negativa))