
"""
2. Declara tres variables numéricas y evalúa la siguiente expresión:
(a + b) * c / 2.
Muestra el resultado y explica cómo se evalúa la expresión paso a paso.

"""
def calcular(numeros):

    a = numeros[0]
    b = numeros[1]
    c =  numeros[2]
    resultado  = (a + b) * c / 2
    return resultado


def main():
    
    numeros = []
    for i in range(1,3+1):
        
        while(True):
            dato = input(f"Ingrese el numero {i}: ")
            if dato.strip() == "":
                continue
            else:
                numeros.append(int(dato))
                break

    
    result = calcular(numeros=numeros)
    print(f"El resultado es {result}")         


if __name__ == "__main__":
        main()    