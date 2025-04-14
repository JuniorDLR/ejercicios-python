"""
18.Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos
de ejercicio, si la fórmula es:
N.Pulsaciones = 220 - Edad / 10

"""


def decifrar_pulsaciones(edad):
    return (220 - edad) / 10

def mostrar_resultados(edad):

    pulsacion = decifrar_pulsaciones(edad=edad)
    print(f"{pulsacion:.0f} pulsaciones por 10 segundos.")
    

def main():
    print("="*80)
    print("     PROGRAMA PARA SABER EL NUMERO DE PULSACIONES POR CADA 10 SEGUNDOS     ")
    print("="*80)
    while True:
        edad = input("Ingrese una edad: ").strip()

        if edad == "":
            print("Campo vacio. Debes de agregar un dato!")
            continue
        else:
            try:
                edad_entero = int(edad)
                mostrar_resultados(edad_entero)
            except ValueError:
                print("Solo se permiten numeros!")
                continue
        print("\n")
        condicion = input("Desea realizar otra operacion (S/s) para continuar: ")
        if condicion.lower() == "s":
            print("\nReiniciando....")
            continue
        else:
            print("Gracias por usar el programa!")
            break




if __name__ == "__main__":
    main()