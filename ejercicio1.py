'''
El siguiente código genera un excepción, utilizar un bloque try-catch para que no termine la ejecución del programa y capturar la excepción que se genera. 
Imprimir el mensaje de error que se genera por pantalla.
'''

def main():
    lista = [1, 2, 3, 4, 5]
    try:
        print(lista[10])
    except IndexError:
        print("Indice fuera del rango")
main()