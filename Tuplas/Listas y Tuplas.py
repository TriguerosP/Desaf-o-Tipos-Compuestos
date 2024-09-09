fechatupla1=(25, 12, 2016)
print("Imprimomos la primer tupla")
print(fechatupla1)

fechalista=list(fechatupla1)
print("Imprimimos la lista que se copio de la tupla anterior ")
print(fechalista)

fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)

fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se escogio de la lista")
print(fechatupla2)