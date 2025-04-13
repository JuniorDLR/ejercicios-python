"""
11.Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el
nombre del producto y precio final luego de aplicar el descuento
"""

def aplicar_descuento(precio, porcentaje):
    return precio * (porcentaje / 100)

def es_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_texto(cadena):
    return cadena.replace(" ", "").isalpha()

def verificacion_input(message, tipo="texto"):
    while True:
        dato = input(message).strip()
        if dato == "":
            print("Campo vacío, reintente de nuevo.")
            continue

        if tipo == "texto":
            if not es_texto(dato):
                print("Solo se permiten letras.")
                continue
            return dato

        if tipo == "numero":
            if not es_float(dato):
                print("Solo se permiten números (usa punto para decimales).")
                continue
            return float(dato)

def mostrar_resultados(nombre, precio, descuento, total_pagar):
    print("="*30)
    print("   RESULTADO DEL DESCUENTO")
    print("="*30)
    print(f"Producto: {nombre}")
    print(f"Precio original: ${precio:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar: ${total_pagar:.2f}")
    print("="*30)

def cierre_programa():
    print("\n" + "="*40)
    print("       ¡Gracias por usar el programa!      ")
    print("="*40)

def conversion_intermedia():
    nombre = verificacion_input("Ingrese el nombre del producto: ", tipo="texto")
    precio = verificacion_input("Ingrese el precio del producto: ", tipo="numero")
    porcentaje = verificacion_input("Ingrese el porcentaje de descuento: ", tipo="numero")

    descuento = aplicar_descuento(precio, porcentaje)
    total_pagar = precio - descuento
    mostrar_resultados(nombre, precio, descuento, total_pagar)

def main():
    while True:
        conversion_intermedia()
        condicion = input("¿Desea realizar otro cálculo? (S/s para continuar): ")
        if condicion.lower() == "s":
            print("\nReiniciando...\n")
            continue
        else:
            cierre_programa()
            break

if __name__ == "__main__":
    main()
