"""
19.El dueño de una tienda compra un artículo a un precio determinado.
¿A qué precio debe venderlo para obtener una ganancia del 30% sobre el precio de compra?"

"""

def resultado_ganacia(precio):
    pocentaje = 30 / 100
    ganacia = pocentaje * precio
    return ganacia


def cierre_programa(message):
    print(message)


def mostrar_resultados(precio):

    ganacia = resultado_ganacia(precio=precio)
    print("\n")
    print("="*32)
    print("           RESULTADOS    ")
    print("="*32)
    print(f"Precio del articulo:     ${precio:.2f}")
    print(f"Ganacia:                 ${ganacia:.2f}")
    print("="*32)




def main():
    
    print("="*70)
    print("     BIENVENIDO AL PROGRAMA PARA SABER LA GANACIA DE UN PRODUCTO     ")
    print("="*70)
    while True:
        precio = input("Ingrese el precio del producto: ").strip()

        if precio == "":
            print("ADVERTENCIA\n No se permite campos vacios.")
            continue
        else:
            try:
                precio_decimal = float(precio)
                mostrar_resultados(precio=precio_decimal)
            except ValueError:
                print("Solo se permiten numeros!")
                continue

        print("\n")    
        condicion = input("Desea realizar otra operacion (S/s) para continuar: ")
        if condicion.lower() == "s":
            print("\nReiniciando......")
            continue
        else:
            print("Gracias por usar el programa!")
            break    



if __name__ == "__main__":
    main()

