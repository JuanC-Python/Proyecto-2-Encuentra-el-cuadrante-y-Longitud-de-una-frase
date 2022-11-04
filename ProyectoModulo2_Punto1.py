# #Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta
# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))

cadena = input("Ingrese un palabra \n")
##print(len(cadena))
Lista_Cadena = list(cadena)
##print(Lista_Cadena)
cuenta_letras = 0
for i in Lista_Cadena:
    cuenta_letras += 1
##print(cuenta_letras)
if cuenta_letras >= 4 and cuenta_letras<= 8:
    print("la palabra es correcta")
if cuenta_letras < 4:
    print(f"Hacen falta letras, Solo tiene {cuenta_letras} letras")
if cuenta_letras > 8:
    print(f"Sobran letras Tiene {cuenta_letras} letras")  
    ##################################################################################333