"""
22. Algoritmo que calcule el salario de un trabajador de la siguiente manera:

El trabajador cobra un precio fijo por hora y se le descuenta el 5% en concepto de impuesto sobre la renta.
El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio por hora.
Como salida, debe mostrar el nombre del trabajador, el sueldo bruto, el descuento por renta y el salario a pagar.

"""


def calcular_salario(mapaInfo):
    nombreTrabajador = mapaInfo["el nombre del trabajador"]
    horasTrabajadas = mapaInfo["las horas trabajadas"]
    precioPorHora = mapaInfo["el precio por hora"]
    
    sueldoBruto = precioPorHora * horasTrabajadas
    impuesto = sueldoBruto * (5 / 100)
    salario = sueldoBruto - impuesto
    
    return nombreTrabajador,sueldoBruto,impuesto,salario




def mostrar_resultados(mapaInfo):

    nombreTrabajador,sueldoBruto,impuesto,salario = calcular_salario(mapaInfo)

    print("="*20)
    print("     RESULTADOS     ")
    print("="*20)
    print(f"Nombre del trabajador:        {nombreTrabajador}")
    print(f"Sueldo bruto:                ${sueldoBruto}")
    print(f"Impuesto por renta:          ${impuesto}")
    print(f"Salario:                     ${salario}")
    print("="*20)

def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_entero(hora):
    try:
        int(hora)
        return True
    except ValueError:
        return False 

def main():
    
    campos = ["el nombre del trabajador","las horas trabajadas","el precio por hora"]

    while True:
        mapaInfo = {}

        for campo in campos:
            while True:
                informacion = input(f"Ingrese {campo}: ").strip()

                if informacion == "":
                    print("No puedes ingresar un campo vacio!")
                    continue

                if campo == "el nombre del trabajador":
                    if validar_nombre(informacion):
                        mapaInfo[campo] = informacion
                        break
                    else:
                        print("Debes de ingresar un nombre valido!")
                        continue
            

                if campo == "las horas trabajadas" or campo == "el precio por hora":
                    if validar_entero(informacion):
                        mapaInfo[campo] = int(informacion)
                        break
                    else:
                        print("Solo se permiten numeros!")
                        continue


        mostrar_resultados(mapaInfo=mapaInfo) 
        

        condicion = input("Deseas realizar otro calculo (S/s) para continuar: ").strip()
        if condicion.lower() == "s":
            print("\nReiniciando.....")
            continue
        else:
            print("Gracias por usar el programa!")
            break
                    

if __name__ == "__main__":
    main()    