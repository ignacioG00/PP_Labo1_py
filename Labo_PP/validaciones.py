import re
from datetime import datetime

def validar_nombre(nombre):
    if re.fullmatch(r'[A-Za-z\s]{1,30}', nombre):
        return True
    return False

def validar_descripcion(descripcion):
    if len(descripcion) <= 200:
        return True
    return False

def validar_presupuesto(presupuesto):
    try:
        presupuesto = int(presupuesto)
        if presupuesto >= 500000:
            return True
    except ValueError:
        pass
    return False

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def obtener_opcion(mensaje, inicio, fin):
    while True:
        try:
            opcion = int(input(mensaje))
            if inicio <= opcion <= fin:
                return opcion
        except ValueError:
            pass
        print(f"Por favor ingrese un número entre {inicio} y {fin}.")