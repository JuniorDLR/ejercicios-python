"""
16. Pide una edad actual y muestra qué edad tendrá el usuario dentro de 5, 10 y 20 años.
"""

def mostrar_resultados(edad):
    edad_5 = edad + 5
    edad_10 = edad + 10
    edad_20 = edad + 20

    print("="*20)
    print("     RESULTADOS     ")
    print("="*20)
    print(f"Edad actual:      {edad}")
    print(f"Edad en 5 años:   {edad_5}")
    print(f"Edad en 10 años:  {edad_10}")
    print(f"Edad en 20 años:  {edad_20}")
    print("="*20)

def cierre_programa(message):
    print(message)

def main():
    
    while True:
        edad = input("Ingrese su edad actual: ").strip()

        if edad == "":
            print("Campo vacio, intenta de nuevo!")
            continue
        else:
            try:
                edad_convertida = int(edad)
                if edad_convertida >=1 and edad_convertida <=100:
                    mostrar_resultados(edad_convertida)
                else:
                    print("Solo debes de ingresar 3 digitos!") 
                    continue   
            except ValueError:
                print("solo se permiten numeros!")
                continue


        condicion = input("Quieres realizar de nuevo el calculo (S/s) para continuar: ")
        if condicion.lower() == "s":
            print("\nReiniciando.....")
            continue
        cierre_programa(message="Gracias por usar el programa!")
        break


if __name__ == "__main__":
    main()