"""
13.Solicita el precio de 3 productos y muestra:
Subtotal
IVA (15%)
Total a pagar
"""
def calculo_subtotal(productos):

    subtotal = 0.0
    for producto in productos:
        subtotal += producto["precio"]
    
    return subtotal  

def calculo_iva(total):
    conversion = 15 / 100
    return conversion * total


def mostrar_resultados(subtotal,iva,total):
    print("\n=== PRODUCTOS INGRESADOS ===")
    print(f"Subtotal:    ${subtotal:.2f}")
    print(f"IVA:         {iva:.0f}%")
    print(f"Total:       ${total:.2f}")
    print("===============================")

def cierre_programa(message):
    print(message)

def main():

    cantidad = int(input("Ingrese la cantidad de productos a agregar: "))
    campos = ["nombre","precio"]
    productos = []


    for i in range(1,cantidad+1):
        
        print(f"Producto {i}",end="\n")
        producto = {}
        for campo in campos:
            while True:

                dato = input(f"Ingrese el {campo} del producto: ").strip()
                if dato == "":
                    print("Campo vacio, intenta de nuevo!")
                    continue

                if campo == "precio":
                        try:
                            dato =  float(dato)
                        except ValueError:
                            print("Debes de ingresar un precio valido!")
                            continue
                    
                producto[campo] = dato
                break

        productos.append(producto)
        
    subtotal = calculo_subtotal(productos=productos)
    iva = calculo_iva(subtotal)  
    total = subtotal + iva
    mostrar_resultados(subtotal=subtotal,iva=iva,total=total)



if __name__ == "__main__":
    main()