import numpy as np

def saludar():
    print("hola te saludo desde la función mensajes.hola.saludos.saludar()")
def prueba():
    print('esto es una prueba')

def generar_array(numeros):
    return np.arange(numeros)


class Saludo():
    def __init__(self):
        print("hola te saludo desde la clase mensajes.hola.saludos.Saludo()")

if __name__== '__main__':
    print(generar_array(5))