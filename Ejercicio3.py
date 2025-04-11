"""
3. Escribe un algoritmo que reciba el nombre y apellido de una persona, y luego
muestre el nombre completo concatenado.
"""


def obtener_texto_concatenado(nombre,apellido):
    return f"{nombre.capitalize()} {apellido.capitalize()}"


def main():

    while(True):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        if(nombre.strip() == "" or apellido.strip() == ""):
            print("Debes de agregar un texto valido!")
            continue
        else:
            resultado = obtener_texto_concatenado(nombre=nombre,apellido=apellido)
            print("="*20)
            print("Resultado")
            print("="*20)
            print(resultado)
            break


if __name__ == "__main__":
    main()