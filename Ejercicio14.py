"""
14. Calcula la calificación final de un estudiante con ponderaciones:
Tareas: 30%
Examen parcial: 30%
Examen final: 40%

"""

def porcentaje_nota():
    porcentaje_tarea = 30 / 100
    porcentaje_parcial = 30 / 100
    porcentaje_final = 40 / 100
    lista = [porcentaje_tarea,porcentaje_parcial,porcentaje_final]
    return lista

def motrar_resultados(notas):

    porcentaje_lista = porcentaje_nota()
    nota_final = 0.0
    
    for (_,nota), porcentaje in zip(notas.items(),porcentaje_lista):
        nota_final += nota * porcentaje

    print("="*20)
    print("     RESULTADOS     ")
    print("="*20)
    print(f"Nota final: {nota_final:.2f}")
    print("="*20)

    

def main():
    
    campos = ["tarea","examen parcial","examen final"]
    nota = {}
    for campo in campos:
        while True:
            dato = input(f"Ingrese la nota de {campo}: ").strip()

            if  dato == "":
                print("Campo vacio, intenta de nuevo!")
                continue

            if campo == "tarea" or campo == "examen parcial" or campo == "examen final":
                try:
                    if float(dato) >= 0 and float(dato) <=100:
                        dato = float(dato)
                        nota[campo] = dato
                        break
                    else:
                        print("La nota debe de ser del 0 al 100")
                        continue
                except ValueError:
                    print("Solo se permite numeros!")
                    continue

    motrar_resultados(nota)





            




if __name__ == "__main__":
    main()