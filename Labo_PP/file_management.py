import csv
import json

def cargar_proyectos(archivo_csv):
    proyectos = []
    try:
        with open(archivo_csv, newline='', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Presupuesto'] = int(row['Presupuesto'])
                proyectos.append(row)
    except FileNotFoundError:
        pass
    return proyectos

def guardar_proyectos(proyectos, archivo_csv):
    with open(archivo_csv, mode='w', newline='') as csvfile:
        fieldnames = ['ID', 'Nombre del Proyecto', 'Descripción', 'Fecha de Inicio', 'Fecha de Fin', 'Presupuesto', 'Estado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for proyecto in proyectos:
            writer.writerow(proyecto)

def guardar_proyectos_finalizados(proyectos, archivo_json):
    finalizados = [p for p in proyectos if p['Estado'] == 'Finalizado']
    with open(archivo_json, mode='w') as jsonfile:
        json.dump(finalizados, jsonfile, indent=4)