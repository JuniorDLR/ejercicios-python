"""
3. Escribe un algoritmo que reciba el nombre y apellido de una persona, y luego
muestre el nombre completo concatenado.
"""


def obtener_texto_concatenado(informacion):
    nombre = informacion["nombre"]
    apellido = informacion["apellido"]

    return f"Nombre completo: {nombre.capitalize()} {apellido.capitalize()}"

def mostrar_resultado(informacion):
    resultado = obtener_texto_concatenado(informacion)
    print("="*20)
    print("Resultado")
    print("="*20)
    print(resultado)

def main():
    
    campos = ["nombre","apellido"]
    informacion = {}
    for campo in campos:
        while(True):
            dato = input(f'Ingrese su {campo}: ')

            if dato == '':
                print("Debes de agregar un texto valido!")
                continue
            else:
                informacion[campo] = dato
                break
    mostrar_resultado(informacion=informacion)

if __name__ == "__main__":
    main()