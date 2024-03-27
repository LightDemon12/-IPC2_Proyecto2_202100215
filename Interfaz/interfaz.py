import tkinter as tk
from tkinter import ttk
from Logica.seleccion_archivo import SelectorArchivo
from Logica.XML_reader import leer_xml
def iniciar_interfaz():
    # Configurar la apariencia de la ventana principal
    app = tk.Tk()
    app.geometry("750x480")
    app.title("Gestión de Maquetas")

    def boton_XML():
        selector = SelectorArchivo()
        selector.seleccionar_archivo(leer_xml)  # Asegúrate de que funcion_leer_xml esté definida
        print("boton_XML presionado")

    def boton_gestion_maquetas():
        print("boton_gestion_maquetas presionado")

    def boton_resolucion_maquetas():
        print("boton_resolucion_maquetas presionado")

    def boton_ayuda():
        print("boton_ayuda presionado")

    def boton_ver_configuracion():
        print("boton_ver_configuracion presionado")

    # Botón para cargar XML
    button_xml = tk.Button(master=app, text="Cargar XML", command=boton_XML)
    button_xml.grid(row=0, column=1, padx=20, pady=20)

    # Botón para gestión de maquetas
    button_gestion_maquetas = tk.Button(master=app, text="Gestión de maquetas", command=boton_gestion_maquetas)
    button_gestion_maquetas.grid(row=0, column=2, padx=20, pady=20)

    # Botón para resolución de maquetas
    button_resolucion_maquetas = tk.Button(master=app, text="Resolución de maquetas", command=boton_resolucion_maquetas)
    button_resolucion_maquetas.grid(row=0, column=3, padx=20, pady=20)

    # Botón para ayuda
    button_ayuda = tk.Button(master=app, text="Ayuda", command=boton_ayuda)
    button_ayuda.grid(row=0, column=4, padx=20, pady=20)

    # Botón para ver configuración de maqueta
    button_ver_configuracion = tk.Button(master=app, text="Ver configuración de maqueta", command=boton_ver_configuracion)
    button_ver_configuracion.grid(row=0, column=5, padx=20, pady=20)

    # Crear Combobox para seleccionar maquetas
    combo_maquetas = ttk.Combobox(master=app)
    combo_maquetas['values'] = ('Maqueta 1', 'Maqueta 2', 'Maqueta 3')  # Ejemplo de valores
    combo_maquetas.grid(row=3, column=1, columnspan=4, padx=20, pady=20)

    # Iniciar el bucle principal de la aplicación
    app.mainloop()


