'''

    El siguiente código pide el ingreso de un entero pero se rompe cuando el ingreso no puede castearse a entero, utilizar un bloque try-catch
    para que no termine la ejecución del programa e indicar el usuario su error.

'''

def main():
    try:
        ingreso = int(input("Ingrese un número: "))
    except ValueError:
        print("El valor ingresado no puede convertirse a un entero")
    else:
        print("El número ingresado es: ", ingreso)

main()