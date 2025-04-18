"""
6. Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual,
calcule su edad actual y su edad en 10 años.

"""
from datetime import datetime
def calcular_edad(nacimiento,ano_actual):

    edad_actual =  ano_actual - nacimiento
    edad_futura = edad_actual + 10
    return  edad_actual , edad_futura


def main():

    ano_actual = datetime.now().year

    while(True):
        nacimiento  = input("Ingrese su  ano de nacimiento: ")
        
        if not nacimiento.isdigit():
            print("\n")
            print("Solo se permite numeros")
            continue
        elif len(nacimiento) == 4:
            edad_actual,edad_futura = calcular_edad(nacimiento=int(nacimiento),ano_actual=ano_actual)
            print(f"La edad actual es {edad_actual}\nLa edad en 10 años es: {edad_futura}")

        else:
            print("\n")
            print("Ingrese un año de nacimiento valido.")
            continue

        condicion = input("Desea realizar otra edad futura: (S/s) ")

        if condicion.lower() == "s":
            continue
        else:
            print("Gracias por usar el programa!")
            break





if __name__ == "__main__":
    main()

