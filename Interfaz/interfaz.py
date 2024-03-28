import tkinter as tk
from tkinter import ttk
from Logica.seleccion_archivo import seleccionar_archivo
from Logica.XML_reader import cargar_maquetas_desde_xml
from Logica.gestion_maquetas import ListaMaquetas, NodoMaqueta

def iniciar_interfaz(lista_maquetas):
    # Configurar la apariencia de la ventana principal
    app = tk.Tk()
    app.geometry("750x480")
    app.title("Gestión de Maquetas")

    def actualizar_combobox():
        # Obtener los nombres de las maquetas
        nombres_maquetas = lista_maquetas.obtener_nombres()
        # Dividir la cadena en una lista de nombres
        nombres_maquetas = nombres_maquetas.split("\n")
        # Actualizar los valores del combobox
        combo_maquetas['values'] = nombres_maquetas
        
    def boton_XML():
        ruta_archivo = seleccionar_archivo()
        cargar_maquetas_desde_xml(ruta_archivo, lista_maquetas)
        print("boton_XML presionado")
        # Actualizar el combobox después de cargar las maquetas
        actualizar_combobox()
        
    def boton_gestion_maquetas():
        print("boton_gestion_maquetas presionado")
        lista_maquetas.eliminar_todas()
        actualizar_combobox()

    def boton_resolucion_maquetas():
        print("boton_resolucion_maquetas presionado")

    def boton_ayuda():
        print("boton_ayuda presionado")

    def boton_ver_configuracion():
        print("boton_ver_configuracion presionado")

        # Obtener el nombre de la maqueta seleccionada en el combobox
        nombre_maqueta = combo_maquetas.get()

        # Obtener la maqueta de la lista
        maqueta = lista_maquetas.buscar_por_nombre(nombre_maqueta)

        if maqueta:
            # Obtener la estructura, entrada, objetivos, número de filas y columnas de la maqueta
            estructura = maqueta.obtener_estructura()
            entrada = (maqueta.coordenada_fila, maqueta.coordenada_columna)
            objetivos = maqueta.obtener_objetivos()
            num_filas = maqueta.num_filas
            num_columnas = maqueta.num_columnas

            print(f"Estructura: {estructura}")
            print(f"Entrada: {entrada}")
            print(f"Objetivos: {objetivos}")
            print(f"Número de filas: {num_filas}")
            print(f"Número de columnas: {num_columnas}")

    # Botón para cargar XML
    button_xml = tk.Button(master=app, text="Cargar XML", command=boton_XML)
    button_xml.grid(row=0, column=1, padx=20, pady=20)
    # Botón para gestión de maquetas
    button_gestion_maquetas = tk.Button(master=app, text="Limpiar Lista", command=boton_gestion_maquetas)
    button_gestion_maquetas.grid(row=0, column=2, padx=20, pady=20)
    # Botón para resolución de maquetas
    button_resolucion_maquetas = tk.Button(master=app, text="Resolución de maquetas", command=boton_resolucion_maquetas)
    button_resolucion_maquetas.grid(row=0, column=3, padx=20, pady=20)
    # Botón para ayuda
    button_ayuda = tk.Button(master=app, text="Ayuda", command=boton_ayuda)
    button_ayuda.grid(row=0, column=5, padx=20, pady=20)
    # Botón para ver configuración de maqueta
    button_ver_configuracion = tk.Button(master=app, text="Ver configuración de maqueta", command=boton_ver_configuracion)
    button_ver_configuracion.grid(row=0, column=4, padx=20, pady=20)
    # Crear Combobox para seleccionar maquetas
    combo_maquetas = ttk.Combobox(master=app)
    # Actualizar los valores del combobox con los nombres de las maquetas
    actualizar_combobox()
    combo_maquetas.grid(row=3, column=1, columnspan=5, padx=20, pady=20)
    # Iniciar el bucle principal de la aplicación
    app.mainloop()


