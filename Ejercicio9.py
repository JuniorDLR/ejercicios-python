"""
9. Algoritmo para calcular el porcentaje de mujeres y varones en un aula

"""


def calculo_porcentaje(cantidadMujer, cantidadHombre):
    total = cantidadMujer + cantidadHombre
    porcentajeMujer = cantidadMujer / total * 100
    porcentajeHombre = cantidadHombre / total * 100
    return porcentajeHombre, porcentajeMujer


def cierre_programa():
    print("\n" + "="*40)
    print("       ¡Gracias por usar el programa!      ")
    print("="*40)


def operacion_intermedia():
    cantidadHombre = verificacion_input("Ingrese la cantidad de hombres: ")
    cantidadMujeres = verificacion_input("Ingrese la cantidad de mujeres: ")
    return calculo_porcentaje(
        cantidadMujer=int(cantidadMujeres),
        cantidadHombre=int(cantidadHombre)
    )


def verificacion_input(mensaje):
    while True:
        cantidad = input(mensaje)
        if cantidad.strip() == "":
            print("No se puede dejar vacío.")
            continue
        elif cantidad.isdigit():
            return cantidad
        else:
            print("Solo se pueden ingresar números.")
            continue


def mostrar_resultado(porcentaje_hombre, porcentaje_mujer):
    print("\n" + "="*40)
    print("            RESULTADOS DEL AULA           ")
    print("="*40)
    print(f"Mujeres: {porcentaje_mujer:.2f}%")
    print(f"Hombres: {porcentaje_hombre:.2f}%")
    print("="*40 + "\n")


def main():
    print("\n" + "="*40)
    print("    CÁLCULO DE PORCENTAJE POR GÉNERO     ")
    print("="*40 + "\n")

    while True:
        resultadoHombre, resultadoMujer = operacion_intermedia()
        mostrar_resultado(resultadoHombre, resultadoMujer)

        condicion = input("¿Desea realizar otro cálculo? (S/s para continuar): ")
        if condicion.lower() == "s":
            print("\nReiniciando...\n")
            continue
        else:
            cierre_programa()
            break


if __name__ == "__main__":
    main()
