"""
20. En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto
anual del hospital se reparte de la siguiente manera:

Urgencias     - 37%
Pediatría     - 42%
Traumatología - 21%

"""
def calculo_presupuesto(presupuesto):
    urgencias = presupuesto * (37 / 100)
    pediatria = presupuesto * (42 / 100)
    traumatologia = presupuesto * (21 / 100)            
    return urgencias, pediatria, traumatologia 


def mostrar_resultados(presupuesto, presupuestoInput):
    urgencias, pediatria, traumatologia = calculo_presupuesto(presupuesto)

    print("="*40)
    print("          RESULTADOS     ")
    print("="*40)
    print("\n")
    print(f"Presupuesto total:         ${int(presupuesto):,}".replace(",", "."))
    print("\n")
    print(f"Para urgencias:            ${urgencias:.2f}")
    print(f"Para pediatría:            ${pediatria:.2f}")
    print(f"Para traumatología:        ${traumatologia:.2f}")
    print("="*40)


def main():
    print("==============================")
    print("     PRESUPUESTO HOSPITAL     ")
    print("==============================")
    
    while True:
        presupuestoInput = input("Ingresa el presupuesto anual del hospital (ej. 1.200.000): ").strip()

        if presupuestoInput == "":
            print("Campo vacío. Debes ingresar un presupuesto.")
            continue

        try:
    
            presupuesto_limpio = presupuestoInput.replace(".", "")
            presupuesto_decimal = float(presupuesto_limpio)

            if presupuesto_decimal <= 0:
                print("El presupuesto debe ser mayor a 0.")
                continue

        except ValueError:
            print("Solo se permiten números.")
            continue

        mostrar_resultados(presupuesto=presupuesto_decimal, presupuestoInput=presupuestoInput)

        condicion = input("¿Desea realizar otro presupuesto? (S/s para continuar): ")
        if condicion.lower() == "s":
            print("\nReiniciando...\n")
            continue
        else:
            print("¡Gracias por usar el programa!")
            break


if __name__ == "__main__":
    main()
