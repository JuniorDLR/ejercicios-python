"""
10. Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su
salario actual y un descuento de 2,5% por servicios

"""

def porcentaje_incremento(porcentaje):
    return porcentaje / 100


def cierre_programa():
    print("Gracias por usar el programa!")


def salario_nuevo(salario_actual, porcentaje):
    porcentaje_servicio = porcentaje_incremento(porcentaje=2.5)

    incremento_salario = salario_actual * porcentaje
    salario_con_incremento = salario_actual + incremento_salario

    descuento_servicio = salario_con_incremento * porcentaje_servicio
    salario_final = salario_con_incremento - descuento_servicio

    return salario_final, incremento_salario, descuento_servicio

def calcular_incremento(salario_actual):

    while True:
        incremento = input("¿De cuánto es el incremento en porcentaje? (ej: 8 o 8.5): ").strip()
        
        if incremento == "":
            print("No se puede dejar vacio")
            continue
        else:
            try:
                valor = float(incremento)
                
                porcentaje = porcentaje_incremento(porcentaje=valor)
                nuevo_salario, aumento, descuento = salario_nuevo(salario_actual=salario_actual,porcentaje=porcentaje)
                mostrar_resultados(nuevo_salario, aumento, descuento)

                break
            except ValueError:
                print("Solo se permiten números (usa punto para decimales)")
                continue
            

def mostrar_resultados(nuevo_salario, aumento, descuento):
    print("=" * 30)
    print("        RESULTADOS        ")
    print("=" * 30)
    print(f"Salario base:           ${nuevo_salario + descuento - aumento:.2f}")
    print(f"Aumento aplicado:       +${aumento:.2f}")
    print(f"Descuento por servicios:-${descuento:.2f}")
    print("-" * 30)
    print(f"Salario final:          ${nuevo_salario:.2f}")
    print("=" * 30)


def main():
    

    while True:
        salario_input = input("Ingrese su salario actual: ")

        if salario_input.strip() == "":
            print("No se puede dejar vacio")
            continue

        try:
            salario_actual = float(salario_input)
            if salario_actual <=0:
                print("El salario debe de ser mayoir a 0")
                continue
            else:
                calcular_incremento(salario_actual)

        except ValueError:
            print("Solo se permiten números (usa punto para decimales).")
            continue


        condicion = input("Desea realizar otro nuevo salario (S/s) para continuar: ")
        if condicion.lower() == "s":
            continue
        else:
            cierre_programa()
            break     



if __name__ == "__main__":
    main()    