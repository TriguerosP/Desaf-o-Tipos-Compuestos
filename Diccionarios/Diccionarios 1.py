def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

paises={"Argentina":40000000, "España":46000000, "Brasil":190000000, "Uruguay":34000000}
imprimir(paises)