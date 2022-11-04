#Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál de los 4 
# cuadrantes se encuentra el punto. El programa debe verificar que ninguna coordenada sea 0. 
# Por ejemplo
# Ingrese X: 4
# Ingrese Y: -5
# El punto se encuentra en el cuadrante IV.
# (X,Y): (+,+) => Cuad. I; (-,+) => Cuad. II; (-,-) => Cuad. III; (+,-) => Cuad. IV  
while True:
    coordenada_x = int(input ("Ingrese el valor de la coordenada X \n"))
    coordenada_y = int(input ("Ingrese el valor de la coordenada Y \n"))
    lista_coordenadas = []
    lista_coordenadas.append(coordenada_x)
    lista_coordenadas.append(coordenada_y)
    #print(lista_coordenadas)    
    if lista_coordenadas[0] > 0 and lista_coordenadas[1] > 0:
        print(f"El punto {lista_coordenadas} se encuentra en el cuadrante I")  
    elif lista_coordenadas[0] < 0 and lista_coordenadas[1] > 0:
        print(f"El punto {lista_coordenadas} se encuentra en el cuadrante II")  
    elif lista_coordenadas[0] < 0 and lista_coordenadas[1] < 0:
        print(f"El punto {lista_coordenadas} se encuentra en el cuadrante III")    
    elif lista_coordenadas[0] > 0 and lista_coordenadas[1] < 0:
        print(f"El punto {lista_coordenadas} se encuentra en el cuadrante IV")   
    elif lista_coordenadas[0] == 0 or lista_coordenadas[1] == 0:
        print("Las coordenadas no pueden ser cero, por favor ingrese nuevamente los datos")
        continue
      
    break
################################################################################################
################################################################################################