def ordenarPaquetes(Datos):
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
        for j in range(len(Mice)-1):
            if Mice[j] <= Mice[j+1]:
                Aux = Mice[j]
                Mice[j] = Mice[j+1]
                Mice[j+1] = Aux
    return "\nLa cantidad total de paquetes de informacion en Kbytes es: "+ str(cont)+"\nLista " \
    "de paquetes Mice ordenada de forma ascendente: "+str(Mice[::-1]) + \
    "\nLista en orden arbitrario de paquetes Elephants: " +str(Elephants)

x = [25,50,10,6,8,12,45,98,35,9,10,3,4]
print(ordenarPaquetes(x))
