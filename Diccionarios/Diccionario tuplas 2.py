def cargar():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=input("Ingrese la fecha en formato dd/mm/aa: ")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad en formato hh:mm ")
            actividad=input("Ingese la descripcion de la actividad ")
            lista.append((hora,actividad))
            continua2=input("Ingresa otra actividad para la misma fecha  [s/n]")
        agenda[fecha]=lista
        continua1=input("Ingresa otra fecha [s/n] ")
    return agenda

def imprimir(agenda):
    print("Listado completo de la agenda: ")
    for fecha in agenda:
        print("Para la fecha: ",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consulta_fecha(agenda):
    fecha=input("Ingrese la fecha de desea consultar: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para esa fecha")

agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)