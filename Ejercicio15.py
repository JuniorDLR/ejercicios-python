"""
15. Pide nombre y apellido y muestra un posible correo:
nombre.apellido@miuniversidad.edu.n
"""

def main():
    campos = ["nombre", "apellido"]
    dominio = "@uamv.edu.ni"
    nombre_completo = []

    for campo in campos:
        while True:
            dato = input(f"Ingrese su {campo}: ")

            if dato.strip() == "":
                print(f"El {campo} no puede quedar vacío!")
                continue
            else:
                nombre_completo.append(dato.lower())
                break

    correo =  "".join("".join(nombre_completo).split()).lower()
    print("=" * 20)
    print("     RESULTADO    ")
    print("=" * 20)
    print(f"{correo}{dominio}")
    print("=" * 20)

if __name__ == "__main__":
    main()
