"""
7. Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una
variable auxiliar para hacerlo.
"""

def intercambio_valores(variable1,variable2):
    intercambio = variable1
    variable1 = variable2
    variable2 = intercambio
    return variable1, variable2

def main():

    lista = []
    for i in range(1,2+1):
    
        while(True):
            dato = input(f"Ingrese el dato {i}: ")
            if dato.strip() == "":
                continue
            else:
                lista.append(int(dato))
                break
    resultado1, resultado2 = intercambio_valores(variable1=lista[0],variable2=lista[1])
    print("="*25)
    print(f"DATOS ANTES DEL INTERCAMBIO")
    print("="*25)
    print(f"Variable1: {lista[0]} - variable2: {lista[1]}")
    print("\n")
    print("="*25)
    print(f"DATOS DESPUES DEL INTERCAMBIO")
    print("="*25)
    print(f"Variable1: {resultado1} - variable2: {resultado2}")


if __name__ == "__main__":
    main()