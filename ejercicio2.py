'''

    El siguiente código intenta agarrar una excepción pero no lo está haciendo correctamente, corregirlo para que funcione correctamente.

'''

def main():
    try:
        5 / 0
    except ZeroDivisionError:
        print("No se puede dividir por cero")

main()