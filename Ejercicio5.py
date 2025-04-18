"""
5. Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15%
de 200?

"""

def calcular_porcentaje(numero):
    porcentaje = 25
    return (porcentaje/100) * numero

def mostrar_resultados(numero):
    
    resultado = calcular_porcentaje(numero=numero)
    print(f"El porcentaje de {numero} es: {resultado:.0f}")

def main():
    
    while True:
        while(True):

            numero = input("Ingrese un numero para calcular el porcentaje: ")
        
            if numero.strip() == '':
                print('Campo vacio. Debes de ingresar un numero')
                continue
            else:
                try:
                    numero_entero = int(numero)
                    mostrar_resultados(numero=numero_entero)
                    break
                except ValueError:
                    print('Solo se permiten numeros!')
                    continue

        condicion =  input("¿Deseas realizar otra operación? (S/s): ")

        if condicion.lower() == "s":
            continue
        else:
            print("Gracias por usar el programa!")
            break


        

if __name__ == "__main__":
    main()    