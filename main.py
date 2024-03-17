# importar cosas necesarias
import tkinter as tk
from tkinter import filedialog
from XML_reader import XMLReader

# Variable global para almacenar la información del archivo XML cargado
informacion_xml = None

def inicializacion():
    # Lógica de inicialización
    input("Soluciones mecatrónicas innovadoras. Presione Enter para iniciar el programa.")

def cargar_archivo_xml():
    global informacion_xml
    # Abrir el cuadro de diálogo para seleccionar un archivo XML
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])

    if ruta_archivo:
        informacion_xml = XMLReader.leer_xml(ruta_archivo)
        print("Archivo XML cargado correctamente.")

def listar_maquetas():
    # Lógica para listar las maquetas ordenadas alfabéticamente
    print("Listado de maquetas:")

def ver_configuracion_maqueta():
    # Lógica para ver la configuración de una maqueta
    print("Configuración de maqueta:")

def resolver_maquetas():
    # Lógica para resolver las maquetas
    print("Resolución de maquetas:")

def ayuda():
    # Lógica para mostrar la ayuda
    print("Ayuda:")
    print("Información del estudiante:")
    print("Nombre: Angel Guilllermo de jesús Pérez jiménez")
    print("Carnet: 202100215")
    print("Correo electrónico: 3870961320101@ingenieria.usac.edu.gt")
    print("\nEnlace a la documentación del proyecto:")
    print("[https://github.com/LightDemon12/-IPC2_Proyecto2_202100215]")


def main():
    print("Inicialización ----> Soluciones mecatrónicas innovadoras")
    input("Presione Enter para iniciar el programa.")

    while True:
        print("\nMenú Principal:")
        print("1. Cargar un archivo XML de entrada")
        print("2. Ver listado de maquetas ordenado alfabéticamente")
        print("3. Ayuda")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_archivo_xml()
        elif opcion == "2":
            while True:
                print("\nSubmenú de Ver listado de maquetas:")
                print("1. Ver configuración de maqueta")
                print("2. Resolución de maquetas")
                print("3. Volver al menú principal")

                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    ver_configuracion_maqueta()
                elif sub_opcion == "2":
                    resolver_maquetas()
                elif sub_opcion == "3":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
        elif opcion == "3":
            ayuda()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
