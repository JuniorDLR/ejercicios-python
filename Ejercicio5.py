"""
5. Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15%
de 200?

"""

def calcular_porcentaje(numero):
    porcentaje = 25
    return (porcentaje/100) * numero



def main():
    

    while(True):
      
      numero = int(input("Ingrese un numero para calcular el porcentaje: "))
      resultado = calcular_porcentaje(numero=numero)
      print(f"El porcentaje de {numero} es: {resultado:.0f}")

      condicion =  input("¿Deseas realizar otra operación? (S/s): ")

      if(condicion.lower() == "s"):
          continue
      else:
          print("Gracias por usar el programa!")
          break
      



if __name__ == "__main__":
    main()    