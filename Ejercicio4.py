"""
4. Declara una variable de tipo texto que contenga un número (por ejemplo, "25").
Luego convierte ese valor a número e imprímelo incrementado en 1

"""

def convertir_texto_a_numero(texto):
    return int(texto)

def verificar_cadena(texto):
    return texto.isdigit()

def main():

    while(True):
        texto = input("Ingrese un numero: ")

        if texto.strip() == "":

            print("\n")
            print("Debes de ingresar un numero")
            continue

        elif not verificar_cadena(texto=texto):

            print("\n")
            print("No se permite letras, solo numeros")
            continue

        else:    
            resultado = convertir_texto_a_numero(texto=texto)
            print(f"El numero es: {resultado+1}" )
            break
    


if __name__ == "__main__":
    main()