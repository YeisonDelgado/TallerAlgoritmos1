def buscarPaquetes(Datos):
    k=0
    cont = 0
    Mice = []
    Elephants = []
    Aux = []
    for i in range(len(Datos)):
        cont += 1

        if Datos[i] <= 10:
            Mice.append(Datos[i])
            k += 1
        else:
            Elephants.append(x[i])
            k += 1

    return "\nLa cantidad total de paquetes de informacion en Kbytes es: "+ str(cont)+"\nLista " \
    "de paquetes Mice ordenada de forma ascendente: "+str(Mice) + \
    "\nLista en orden creciente de paquetes Elephants: " +str(Elephants)

x = [3,5,6,8,10,34,40,50]
print(buscarPaquetes(x))
