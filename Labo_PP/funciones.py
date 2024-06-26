from datetime import datetime
from validaciones import obtener_opcion, validar_nombre, validar_descripcion, validar_presupuesto, validar_fecha

def ingresar_proyecto(proyectos):
    """
    Permite al usuario ingresar un nuevo proyecto en la lista de proyectos.

    :param proyectos: Lista de proyectos.
    """
    if len(proyectos) >= 50:
        print("No se pueden agregar más proyectos. Límite alcanzado.")
        return

    nombre = input("Nombre del Proyecto: ")
    while not validar_nombre(nombre):
        print("Nombre inválido. Debe tener solo caracteres alfabéticos y no más de 30 caracteres.")
        nombre = input("Nombre del Proyecto: ")

    descripcion = input("Descripción: ")
    while not validar_descripcion(descripcion):
        print("Descripción inválida. No debe exceder los 200 caracteres.")
        descripcion = input("Descripción: ")

    presupuesto = input("Presupuesto: ")
    while not validar_presupuesto(presupuesto):
        print("Presupuesto inválido. Debe ser un valor numérico entero no menor a $500000.")
        presupuesto = input("Presupuesto: ")

    fecha_inicio = input("Fecha de Inicio (DD-MM-AAAA): ")
    while not validar_fecha(fecha_inicio):
        print("Fecha de inicio inválida. Debe estar en formato DD-MM-AAAA.")
        fecha_inicio = input("Fecha de Inicio (DD-MM-AAAA): ")

    fecha_fin = input("Fecha de Fin (DD-MM-AAAA): ")
    while not validar_fecha(fecha_fin) or datetime.strptime(fecha_fin, '%d-%m-%Y') < datetime.strptime(fecha_inicio, '%d-%m-%Y'):
        print("Fecha de fin inválida. Debe estar en formato DD-MM-AAAA y no puede ser anterior a la fecha de inicio.")
        fecha_fin = input("Fecha de Fin (DD-MM-AAAA): ")

    id_proyecto = len(proyectos) + 1
    proyecto = {
        'id': id_proyecto,
        'Nombre del Proyecto': nombre,
        'Descripción': descripcion,
        'Fecha de Inicio': fecha_inicio,
        'Fecha de Fin': fecha_fin,
        'Presupuesto': int(presupuesto),
        'Estado': 'Activo'
    }
    proyectos.append(proyecto)
    print(f"Proyecto '{nombre}' ingresado con éxito.")

def modificar_proyecto(proyectos):
    """
    Permite modificar los datos de un proyecto existente en la lista de proyectos.

    :param proyectos: Lista de proyectos.
    """
    mostrar_todos(proyectos)
    id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
    while not id_proyecto.isdigit():
        print("ID inválido. Debe ser un número entero.")
        id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
        
    proyecto = next((p for p in proyectos if p['id'] == int(id_proyecto)), None)
    if not proyecto:
        print(f"No se encontró ningún proyecto con ID {id_proyecto}.")
        return

    while True:
        print("""
    +------------------------------+
    |        MENÚ PRINCIPAL        |
    +------------------------------+
    |  1. Nombre del Proyecto      |
    |  2. Descripcion              |
    |  3. Presupuesto              |
    |  4. Fecha de Inicio          |
    |  5. Fecha de Fin             |
    |  6. Estado                   |
    |  7. Salir                    |
    +------------------------------+
    """)
        opcion = obtener_opcion("Seleccione el campo a modificar: ", 1, 7)
        if opcion == 1:
            nombre = input("Nuevo Nombre del Proyecto: ")
            while not validar_nombre(nombre):
                print("Nombre inválido. Debe tener solo caracteres alfabéticos y no más de 30 caracteres.")
                nombre = input("Nuevo Nombre del Proyecto: ")
            proyecto['Nombre del Proyecto'] = nombre
        elif opcion == 2:
            descripcion = input("Nueva Descripción: ")
            while not validar_descripcion(descripcion):
                print("Descripción inválida. No debe exceder los 200 caracteres.")
                descripcion = input("Nueva Descripción: ")
            proyecto['Descripción'] = descripcion
        elif opcion == 3:
            presupuesto = input("Nuevo Presupuesto: ")
            while not validar_presupuesto(presupuesto):
                print("Presupuesto inválido. Debe ser un valor numérico entero no menor a $500000.")
                presupuesto = input("Nuevo Presupuesto: ")
            proyecto['Presupuesto'] = int(presupuesto)
        elif opcion == 4:
            fecha_inicio = input("Nueva Fecha de Inicio (DD-MM-AAAA): ")
            while not validar_fecha(fecha_inicio):
                print("Fecha de inicio inválida. Debe estar en formato DD-MM-AAAA.")
                fecha_inicio = input("Nueva Fecha de Inicio (DD-MM-AAAA): ")
            proyecto['Fecha de Inicio'] = fecha_inicio
        elif opcion == 5:
            fecha_fin = input("Nueva Fecha de Fin (DD-MM-AAAA): ")
            while not validar_fecha(fecha_fin) or datetime.strptime(fecha_fin, '%d-%m-%Y') < datetime.strptime(proyecto['Fecha de Inicio'], '%d-%m-%Y'):
                print("Fecha de fin inválida. Debe estar en formato DD-MM-AAAA y no puede ser anterior a la fecha de inicio.")
                fecha_fin = input("Nueva Fecha de Fin (DD-MM-AAAA): ")
            proyecto['Fecha de Fin'] = fecha_fin
        elif opcion == 6:
            estado = input("Nuevo Estado (Activo, Cancelado, Finalizado): ")
            while estado not in ['Activo', 'Cancelado', 'Finalizado']:
                print("Estado inválido. Debe ser 'Activo', 'Cancelado' o 'Finalizado'.")
                estado = input("Nuevo Estado (Activo, Cancelado, Finalizado): ")
            proyecto['Estado'] = estado
        elif opcion == 7:
            break
        print("Proyecto modificado con éxito.")

def cancelar_proyecto(proyectos):
    """
    Cambia el estado de un proyecto a 'Cancelado' basándose en su ID.

    :param proyectos: Lista de proyectos.
    """
    mostrar_discriminado(proyectos, 'Activo')
    id_proyecto = input("Ingrese el ID del proyecto a cancelar: ")
    while not id_proyecto.isdigit():
        print("ID inválido. Debe ser un número entero.")
        id_proyecto = input("Ingrese el ID del proyecto a cancelar: ")
    proyecto = next((p for p in proyectos if p['id'] == int(id_proyecto)), None)
    if proyecto:
        proyecto['Estado'] = 'Cancelado'
        print(f"Proyecto con ID {id_proyecto} ha sido cancelado.")
    else:
        print(f"No se encontró ningún proyecto con ID {id_proyecto}.")

def comprobar_proyectos(proyectos):
    """
    Verifica y actualiza el estado de los proyectos basándose en su fecha de fin y el estado actual.

    :param proyectos: Lista de proyectos.
    """
     # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Formato de fecha esperado
    formato_fecha ="%d-%m-%Y"
    
    # Iterar sobre cada proyecto
    for proyecto in proyectos:
        # Convertir la fecha de finalización del proyecto a un objeto datetime
        try:
            fecha_fin = datetime.strptime(proyecto['Fecha de Fin'].strip(), formato_fecha)
        except ValueError:
            print(f"Error: Formato de fecha inválido en el proyecto con ID {proyecto['id']}")
            continue
        
        # Comparar la fecha de finalización con la fecha actual
        if fecha_fin < fecha_actual and proyecto['Estado'] != 'Finalizado':
            proyecto['Estado'] = 'Finalizado'
            print(f"El proyecto con ID {proyecto['id']} ha sido finalizado.")
        elif fecha_fin >= fecha_actual and proyecto['Estado'] == 'Finalizado':
            proyecto['Estado'] = 'Activo'
            print(f"El proyecto con ID {proyecto['id']} ha sido reactivado a Activo.")
    print("Comprobación de proyectos completada.")

def mostrar_todos(proyectos):
    """
    Muestra todos los proyectos en formato de tabla.

    :param proyectos: Lista de proyectos.
    """
    print(f"| {'(ID) Nombre del Proyecto':38} | {'Descripción':80} | {'Fecha de Inicio':12} | {'Fecha de Fin':12} | {'Presupuesto':12} | {'Estado':10} |")
    print('-' * 150)
    for proyecto in proyectos:
            print(f"| {proyecto['id']} {proyecto['Nombre del Proyecto']:38} | {proyecto['Descripción']:80} | {proyecto['Fecha de Inicio']:12} | {proyecto['Fecha de Fin']:12} | {proyecto['Presupuesto']:12} | {proyecto['Estado']:10} |")

def calcular_presupuesto_promedio(proyectos):
    """
    Calcula y muestra el presupuesto promedio de los proyectos.

    :param proyectos: Lista de proyectos.
    """
    presupuesto_total= 0
    if not proyectos:
        print("No hay proyectos disponibles.")
        return
    for proyecto in proyectos:
        presupuesto_total= presupuesto_total + int(proyecto['Presupuesto'])
    promedio = presupuesto_total / len(proyectos)
    print(f"Presupuesto promedio de los proyectos: ${promedio:.2f}")

def buscar_proyecto_por_nombre(proyectos):
    """
    Busca y muestra un proyecto basándose en su nombre.

    :param proyectos: Lista de proyectos.
    """
    nombre = input("Ingrese el nombre del proyecto a buscar: ")
    for proyecto in proyectos:
        if proyecto['Nombre del Proyecto'].lower() == nombre.lower():
            print(f"| {proyecto['Nombre del Proyecto']:30} | {proyecto['Descripción']:50} | {proyecto['Presupuesto']:12} | {proyecto['Fecha de Inicio']:12} | {proyecto['Fecha de Fin']:12} | {proyecto['Estado']:10} |")
            return
    print(f"No se encontró ningún proyecto con el nombre '{nombre}'.")

def ordenar_proyectos(proyectos):
    """
    Ordena los proyectos basándose en el criterio seleccionado y en el orden (ascendente o descendente).

    :param proyectos: Lista de proyectos.
    """
    print("""
    +------------------------------+
    |    CRITERIOS DE ORDENACIÓN   |
    +------------------------------+
    |  1. Nombre                   |
    |  2. Presupuesto              |
    |  3. Fecha de Inicio          |
    +------------------------------+
    """)
    criterio_ordenamiento = obtener_opcion("Seleccione el criterio de ordenamiento: ", 1, 3)
    orden = obtener_opcion("Seleccione el orden (1. Ascendente, 2. Descendente): ", 1, 2)
    reverso = True if orden == 1 else False

    if criterio_ordenamiento == 1:
        ordenar_por(proyectos, reverso, 'Nombre del Proyecto')
        mostrar_todos(proyectos) and print("Proyectos ordenados con éxito.")
         
    elif criterio_ordenamiento == 2:
        ordenar_por(proyectos, reverso, 'Presupuesto')
        mostrar_todos(proyectos) and print("Proyectos ordenados con éxito.")
         
    elif criterio_ordenamiento == 3:
        ordenar_por_FechaInicio(proyectos,reverso)
        mostrar_todos(proyectos) and print("Proyectos ordenados con éxito.")     

def retomar_proyecto(proyectos):
    """
    Cambia el estado de un proyecto de 'Cancelado' a 'Activo' basándose en su ID.

    :param proyectos: Lista de proyectos.
    """
    mostrar_discriminado(proyectos, 'Cancelado')
    id_proyecto = input("Ingrese el ID del proyecto a retomar: ")
    while not id_proyecto.isdigit():
        print("ID inválido. Debe ser un número entero.")
        id_proyecto = input("Ingrese el ID del proyecto a retomar: ")
    proyecto = next((p for p in proyectos if p['id'] == int(id_proyecto)), None)
    if proyecto and proyecto['Estado'] == 'Cancelado':
        proyecto['Estado'] = 'Activo'
        print(f"Proyecto con ID {id_proyecto} ha sido retomado.")
    else:
        print(f"No se encontró ningún proyecto cancelado con ID {id_proyecto}.")
        
def mostrar_discriminado(proyectos, opcion):
    """
    Muestra los proyectos que tienen el estado especificado en 'opcion'.

    :param proyectos: Lista de proyectos.
    :param opcion: Estado de los proyectos a mostrar (e.g., 'Activo', 'Cancelado', 'Finalizado').
    """
    print(f"| {'(ID) Nombre del Proyecto':38} | {'Descripción':80} | {'Fecha de Inicio':12} | {'Fecha de Fin':12} | {'Presupuesto':12} | {'Estado':10} |")
    print('-' * 150)
    for proyecto in proyectos:
        if proyecto['Estado'] == opcion:
            print(f"|{proyecto['id']} {proyecto['Nombre del Proyecto']:38} | {proyecto['Descripción']:80} | {proyecto['Fecha de Inicio']:12} | {proyecto['Fecha de Fin']:12} | {proyecto['Presupuesto']:12} | {proyecto['Estado']:10} |")

def ordenar_por(proyectos, ascendente, seccion):
    """
    Ordena los proyectos basándose en la sección especificada y el orden (ascendente o descendente).

    :param proyectos: Lista de proyectos.
    :param ascendente: Booleano que indica si el orden es ascendente (True) o descendente (False).
    :param seccion: La clave del diccionario por la que se desea ordenar ('Nombre del Proyecto', 'Presupuesto').
    """
    n = len(proyectos)
    for i in range(n):
        for j in range(0, n-i-1):
            if seccion == 'Nombre del Proyecto':
                if (ascendente and proyectos[j][seccion].lower() > proyectos[j+1][seccion].lower()) or \
                (not ascendente and proyectos[j][seccion].lower() < proyectos[j+1][seccion].lower()):
                # Intercambiar si el elemento encontrado es mayor (ascendente) o menor (descendente) que el siguiente elemento
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
            elif (ascendente and proyectos[j][seccion] > proyectos[j+1][seccion]) or \
                (not ascendente and proyectos[j][seccion] < proyectos[j+1][seccion]):
                # Intercambiar si el elemento encontrado es mayor (ascendente) o menor (descendente) que el siguiente elemento
                    proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]

def ordenar_por_FechaInicio(proyectos,ascendente):
    """
    Ordena los proyectos basándose en la fecha de inicio y el orden (ascendente o descendente).

    :param proyectos: Lista de proyectos.
    :param ascendente: Booleano que indica si el orden es ascendente (True) o descendente (False).
    """
    n = len(proyectos)
    for i in range(n):
        for j in range(0, n-i-1):
            fecha_j = datetime.strptime(proyectos[j]['Fecha de Inicio'].strip(), '%d-%m-%Y')
            fecha_j1 = datetime.strptime(proyectos[j+1]['Fecha de Inicio'].strip(), '%d-%m-%Y')
            if (ascendente and fecha_j > fecha_j1) or (not ascendente and fecha_j < fecha_j1):
                # Intercambiar si la fecha actual es mayor (ascendente) o menor (descendente) que la siguiente fecha
                proyectos[j], proyectos[j+1] = proyectos[j+1], proyectos[j]
    return proyectos

def proyecto_seccion_en_10s(proyecto, opcion):
    fecha_ini_decada = datetime.strptime('01-01-2010', '%d-%m-%Y')
    fecha_fin_decada = datetime.strptime('31-12-2019', '%d-%m-%Y')
    #Me tiraba error unconverted remain, lo que significaba que habian espacios de mas por lo que agrego la funcion.strip() 
    # que quita todos los espacios en blancos que hay en el csv al traerlos
    fecha_inicio = datetime.strptime(proyecto['Fecha de Inicio'].strip(), '%d-%m-%Y')
    return fecha_ini_decada <= fecha_inicio <= fecha_fin_decada and proyecto['Estado'] == opcion

def mostrar_finalizados_o_Iniciados_en_10(proyectos):
    """
    Muestra todos los proyectos en formato de tabla.

    :param proyectos: Lista de proyectos.
    """
    opcion = obtener_opcion("Seleccione los proyectos a mostrar: \n 1.Finalizados en los 10's \n 2.Iniciados en los 10's\n\n" ,1 ,2)
    if opcion == 1:
        nombre = 'Finalizado'
    elif opcion == 2:
        nombre = 'Activo'
            
    print("Proyectos finalizados en la década de los 10s:")
    print(f"| {'Nombre del Proyecto':38} | {'Descripción':80} | {'Fecha de Inicio':12} | {'Fecha de Fin':12} | {'Presupuesto':12} | {'Estado':10} |")
    print('-' * 150)
    for proyecto in proyectos:
        if proyecto_seccion_en_10s(proyecto,nombre):
            print(f"| {proyecto['Nombre del Proyecto']:38} | {proyecto['Descripción']:80} | {proyecto['Fecha de Inicio']:12} | {proyecto['Fecha de Fin']:12} | {proyecto['Presupuesto']:12} | {proyecto['Estado']:10} |")
        