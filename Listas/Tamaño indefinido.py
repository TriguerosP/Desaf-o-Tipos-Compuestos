lista=[]
valor=int(input("Ingresa el valor (0 para finalizar)"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresa el valor (0 para finalizar)"))

print("Tamaño de Lista")
print(len(lista))