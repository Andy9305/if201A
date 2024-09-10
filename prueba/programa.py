'''
Definicion de funciones que seran sometidas a pruebas unitarias
Fecha:09/09/2024
'''
def suma(x, y):
    return x+y

def es_mayor(x, y):
    return (x>y)
def divide(x, y):
    if y== 0:
        return ValueError("No se puede dividir por 0")
    return(x/y)