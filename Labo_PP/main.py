from datetime import datetime
from validaciones import validar_nombre, validar_descripcion, validar_presupuesto, validar_fecha, obtener_opcion
from manejo_archivos import cargar_proyectos, guardar_proyectos, guardar_proyectos_finalizados
from funciones import (
    ingresar_proyecto,
    modificar_proyecto,
    cancelar_proyecto,
    comprobar_proyectos,
    mostrar_todos,
    calcular_presupuesto_promedio,
    buscar_proyecto_por_nombre,
    ordenar_proyectos,
    retomar_proyecto,
    mostrar_finalizados_o_Iniciados_en_10
)

PROYECTOS_CSV = 'Proyectos.csv'
PROYECTOS_FINALIZADOS_JSON = 'ProyectosFinalizados.json'

def menu():
    print("""
    +-------------------------------------+
    |        MENÚ PRINCIPAL               |
    +-------------------------------------+
    |  1. Ingresar proyecto               |
    |  2. Modificar proyecto              |
    |  3. Cancelar proyecto               |
    |  4. Comprobar proyectos             |
    |  5. Mostrar todos                   |
    |  6. Calcular presupuesto            |
    |     promedio                        |
    |  7. Buscar proyecto por             |
    |     nombre                          |
    |  8. Ordenar proyectos               |
    |  9. Retomar proyecto                |
    | 10. Mostrar Finalizados o Iniciados |
    | 11. Salir                           |
    +-------------------------------------+
    
    
    """ )

def main():
    
    proyectos = cargar_proyectos(PROYECTOS_CSV)

    while True:
        menu()
        opcion = obtener_opcion("Seleccione una opción: ", 1, 11)
        if opcion == 1:
            ingresar_proyecto(proyectos)
        elif opcion == 2:
            modificar_proyecto(proyectos)
        elif opcion == 3:
            cancelar_proyecto(proyectos)
        elif opcion == 4:
            comprobar_proyectos(proyectos)
        elif opcion == 5:
            mostrar_todos(proyectos)
        elif opcion == 6:
            calcular_presupuesto_promedio(proyectos)
        elif opcion == 7:
            buscar_proyecto_por_nombre(proyectos)
        elif opcion == 8:
            ordenar_proyectos(proyectos)
        elif opcion == 9:
            retomar_proyecto(proyectos)
        elif opcion == 10:
            mostrar_finalizados_o_Iniciados_en_10(proyectos)
        elif opcion == 11:
            guardar_proyectos(proyectos, PROYECTOS_CSV)
            guardar_proyectos_finalizados(proyectos, PROYECTOS_FINALIZADOS_JSON)
            break

if __name__ == "__main__":
    main()