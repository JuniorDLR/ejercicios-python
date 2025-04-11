"""
1. Escribe un algoritmo que declare tres variables: una para el nombre de una
persona, otra para su edad y otra para su estatura. Asigna valores adecuados a cada
una.

"""
def input_user():
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese su edad: "))
    estatura = float(input("Ingrese su estatura: "))
    
    return (nombre,edad,estatura)


def main():
    
    nombre,edad ,estatura = input_user()
    print("\n")
    print("="*17)
    print("DATOS PERSONALES")
    print("="*17)
   
    print(f"Su nombre es: {nombre}\nSu edad es: {edad} \nSu estatura es: {estatura}")
    
    

if __name__ == '__main__':
   main()