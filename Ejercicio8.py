"""

8. Una persona recibe un préstamo de 10,000.00 de un banco y desea saber cuánto
pagará de interés, si el banco le cobra una tasa del 27% anual.

"""

def main():
    
    capital = 10000.00
    ano = 1
    tasa_interes = 27 / 100
    interes = float(capital * tasa_interes * ano)

    print(f"El interés con una tasa anual del 27% es: {interes:.0f}")
    
if __name__ == "__main__":
    main()    
