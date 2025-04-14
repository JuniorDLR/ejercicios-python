"""
17. Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula
siguiente:

masa = presion * volumen / (0.37 * (temperatura +460))

"""

def calcular_masa(presion, volumen, temperatura):
    masa = presion * volumen / (0.37 * (temperatura + 460))
    return masa

def cierre_programa():
    print("Gracias por usar el programa!")



def mostrar_resultados(datos_masa):
    presion = datos_masa["presion"]
    volumen = datos_masa["volumen"]
    temperatura = datos_masa["temperatura"]
    
    masa = calcular_masa(presion=presion,volumen=volumen,temperatura=temperatura)

    print("="*20)
    print("     RESULTADOS     ")
    print("="*20)
    print(f"Presion:     {presion}")
    print(f"Volumen:     {volumen}")
    print(f"Temperatura: {temperatura}")
    print("="*20)
    print(f"MASA: {masa:.2f}")
    print("="*20)

def main():

    campos = ["presion","volumen","temperatura"]
    
    
    while True:
            datos_masa = {}
            
            for campo in campos:
                dato = input(f"Ingrese el dato para {campo}: ").strip()

                if dato == "":
                    print("Campo vacio. Debes de ingresar un valor!")
                    continue
                else:
                    try:
                        dato_decimal = float(dato)
                        datos_masa[campo] = dato_decimal
                    
                    except ValueError:
                        print("Solo se permite numeros!")
                        continue    
    
            mostrar_resultados(datos_masa=datos_masa)
            

            condicion = input("Desea realizar otra operacion (S/s) para continuar: ").strip()
            if condicion.lower() == "s":
                print("\nReiniciando.....")
                continue
            else:
                cierre_programa()
                break    







if __name__ == "__main__":
    main()

