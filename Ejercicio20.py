"""
20.Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra
los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer
la ruta en una semana cualquiera

"""

def promedio_recorrido(tiempo):
    dias = 3
    promedio = sum(tiempo) / dias
    return promedio

def mostrar_resultados(lista_tiempo):

    tiempo_promedio = promedio_recorrido(tiempo=lista_tiempo)
    print("="*30)
    print("          RESULTADOS     ")
    print("="*30)
    print(f"Tiempo promedio: {tiempo_promedio:.2f} minutos")
    print("="*30)


def main():

    
    campos = ["lunes","miercoles","viernes"]

    while True:
        lista_tiempo = []

        for campo in campos:
            dato = input(f"Ingrese el tiempo del dia {campo}: ").strip()

            if dato == "":
                print("No se permiten campos vacios!")
                continue
            else:
                try:
                    tiempo = float(dato)
                    lista_tiempo.append(tiempo)
                except ValueError:
                    print("Solo se permite numeros!")
                    continue

        print("\n")
        mostrar_resultados(lista_tiempo=lista_tiempo)        

        condicion = input("Desea realizar otro calculo (S/s) para continuar: ")
        if condicion.lower() == "s":
            print("\nReiniciando.....")
            continue
        else:
            print("Gracias por usar el programa!")
            break


if __name__ == "__main__":
    main()    