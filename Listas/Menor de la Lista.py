lista=[]
for x in range(5):
    valor=int(input("Ingrese Valor: "))
    lista.append(valor)

menor=lista[0]
poscision=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        poscision=x

print("Lista Completa")
print(lista)
print("Menor de la Lista")
print(menor)
print("Posicion del menor en la lista")
print(poscision)