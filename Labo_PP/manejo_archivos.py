import json

def cargar_proyectos(archivo_csv):
    """
    Carga una lista de proyectos desde un archivo CSV.

    :param archivo_csv: Ruta al archivo CSV que contiene los datos de los proyectos.
    :return: Lista de diccionarios leida.
    """
    proyectos = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as csvfile:
            reader = csvfile.readlines()
            for row in reader[1:]:
                data= row.strip().split(',')
                proyecto = {
                    "ID" : (data[0]),
                    'Nombre del Proyecto' : str(data[1]),
                    'Descripción' : (data[2]),
                    'Fecha de Inicio' : (data[3]),
                    'Fecha de Fin' : (data[4]),
                    'Presupuesto' : (data[5]),
                    'Estado' : str(data[6])
                }
                
                proyectos.append(proyecto)
    except FileNotFoundError:
        pass
    return proyectos

def guardar_proyectos(proyectos, archivo_csv):
    """
    Guarda una lista de proyectos en un archivo CSV.

    :param proyectos: Lista de diccionarios.
    :param archivo_csv: Ruta al archivo CSV donde se guardarán los datos de los proyectos.
    """
    with open(archivo_csv, mode='w', encoding='utf-8') as csvfile:
        datos_antiguos = csvfile.read()
        nuevos_datos = 'ID,Nombre del Proyecto,Descripción,Fecha de Inicio,Fecha de Fin,Presupuesto,Estado\n'
        csvfile.write(nuevos_datos)
        
        for proyecto in proyectos:
            nuevos_datos += (
                f"{proyecto['ID']},"
                f"{proyecto['Nombre del Proyecto']},"
                f"{proyecto['Descripción']},"
                f"{proyecto['Fecha de Inicio']},"
                f"{proyecto['Fecha de Fin']},"
                f"{proyecto['Presupuesto']},"
                f"{proyecto['Estado']}\n"
            )
            csvfile.write(nuevos_datos)
            
            if datos_antiguos != nuevos_datos :
                with open(archivo_csv, mode='w') as file:
                    file.write(nuevos_datos)

def guardar_proyectos_finalizados(proyectos, archivo_json):
    """
    Guarda una lista de proyectos finalizados en un archivo JSON.

    :param proyectos: Lista de diccionarios.
    :param archivo_json: Ruta al archivo JSON donde se guardarán los datos de los proyectos finalizados.
    """
    finalizados = [p for p in proyectos if p['Estado'] == 'Finalizado']
    with open(archivo_json, mode='w') as jsonfile:
        json.dump(finalizados, jsonfile, indent=4)