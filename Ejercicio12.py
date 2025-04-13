"""
12. Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), calcula cuánto
dejar de propina

"""

def calcular_porcentaje(porcentaje):
    return porcentaje / 100


def calcular_propina(porcentaje,total):
    return total * porcentaje


def es_float(dato):
    try:
        float(dato)
        return True
    except ValueError:
        return False
    

def verificar_input(message,tipo):

    while True:
        dato = input(message).strip()

        if dato == "":
            print(f"Campo vacio. Debes de ingresar el {tipo}")
            continue
        if not es_float(dato):
            print(f"Debes de ingresar un {tipo} valido")
            continue
        return float(dato)
    

def cierre_programa():
    print("\n" + "="*40)
    print("       ¡Gracias por usar el programa!      ")
    print("="*40)



def intermediario():
    totalCuenta = verificar_input(message="Ingrese el total de cuenta: ",tipo="total de la cuenta")
    porcentajePropina = verificar_input(message="Ingresa el porcentaje de la propina: ",tipo="porcentaje de la propina")
    porcentajeCalculo = calcular_porcentaje(porcentajePropina)
    propina = calcular_propina(porcentaje=porcentajeCalculo,total=totalCuenta) 
    mostrar_resultados(totalCuenta,porcentajePropina,propina)   

def mostrar_resultados(totalCuenta, porcentajePropina, propina):
    print("="*30)
    print("   RESULTADO PROPINA")
    print("="*30)
    print(f"Porcentaje propina: {porcentajePropina:.0f}%")
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar: ${totalCuenta+propina:.2f}")
    print("="*30)
def main():
    
    while True:
        intermediario()
        condicion = input("¿Deseas realizar otro cálculo de propina? (S/s para continuar): ")


        if condicion.lower() == "s":
            print("\nReiniciando...\n")
            continue
        cierre_programa()
        break
        



if __name__ == "__main__":
    main()    