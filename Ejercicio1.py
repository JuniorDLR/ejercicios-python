"""
1. Escribe un algoritmo que declare tres variables: una para el nombre de una
persona, otra para su edad y otra para su estatura. Asigna valores adecuados a cada
una.

"""

def validar_cero(numero):
    try:
        if numero > 0:
            return True
    except ValueError:
        print("Debes de ingresar un numero mayor a cero!")
        return False

    
def mostrar_resultados(resultados):

    nombre = resultados["nombre"]
    edad = resultados["edad"]
    estatura = resultados["estatura"]

    print("\n")
    print("="*17)
    print("DATOS PERSONALES")
    print("="*17)

    print(f"Su nombre es: {nombre}\nSu edad es: {edad} \nSu estatura es: {estatura}")

def main():
    
    campos = ["nombre","edad","estatura"]
    resultados = {}
    for campo in campos:
        while True:
            dato = input(f"Ingrese su {campo}: ")

            if dato.strip() == "":
                print(f"Campo vacio, debes de ingresar un {campo} valido!")
                continue
            if campo == "nombre":
                resultados[campo] = dato
                break
            elif campo == "edad":
                try:
                    edad_entero = int(dato)
                    if validar_cero(numero=edad_entero):
                        resultados[campo] = edad_entero
                        break
                    else:
                        print("El numero debe de ser mayor a cero")
                        continue
                except ValueError:
                    print("Solo se permiten numeros")
                    continue
            elif campo == "estatura":
                try:
                    estatura = float(dato)
                    resultados[campo] = estatura
                    break
                except ValueError:
                    print('Solo se permiten numeros!')
                    continue

    mostrar_resultados(resultados=resultados)
    
    

if __name__ == '__main__':
    main()