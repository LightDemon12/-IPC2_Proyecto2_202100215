import tkinter as tk
from tkinter import ttk
from Logica.seleccion_archivo import seleccionar_archivo
from Logica.XML_reader import cargar_maquetas_desde_xml
from Logica.gestion_maquetas import ListaMaquetas, NodoMaqueta, ListaDFS, NodoDFS, dfs, generar_dot_DFS, generar_dot_objetivos_alcanzados, mostrar_imagen
import webbrowser

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

    def boton_resolucion_maquetas(lista_maquetas, combo_maquetas):
        print("boton_resolucion_maquetas presionado")

        # Obtener el nombre de la maqueta seleccionada en el combobox
        nombre_maqueta = combo_maquetas.get()

        # Obtener la maqueta de la lista
        maqueta = lista_maquetas.buscar_por_nombre(nombre_maqueta)

        # Crear el laberinto DFS a partir de la maqueta seleccionada
        laberinto = maqueta.crear_laberintoDFS(maqueta.num_filas, maqueta.num_columnas)

        # Obtener las coordenadas de inicio del laberinto
        inicio = laberinto.obtener_inicio()

        # Llamar a la función dfs con el laberinto y las coordenadas de inicio
        objetivos_visitados, recorrido_completo = dfs(laberinto, inicio)

        # Mostrar los nodos visitados
        print("Nodos visitados:")
        objetivos_visitados.mostrarListaDFS()

        # Mostrar el recorrido completo
        print("Recorrido completo:")
        recorrido_completo.mostrarListaRecorrido()

        # Generar el archivo .dot
        generar_dot_DFS(lista_maquetas, nombre_maqueta, recorrido_completo, objetivos_visitados, 'recorrido_dfs')
        # Mostrar la imagen generada
        mostrar_imagen('recorrido_dfs.png')
        generar_dot_objetivos_alcanzados(lista_maquetas, nombre_maqueta, objetivos_visitados, 'objetivos_alcanzados')
        # Mostrar la imagen generada
        mostrar_imagen('objetivos_alcanzados.png')








    def abrir_link():
        webbrowser.open('https://github.com/LightDemon12/-IPC2_Proyecto2_202100215')

    def boton_ayuda():
        print("boton_ayuda presionado")

        # Crear una nueva ventana
        ventana_ayuda = tk.Toplevel()
        ventana_ayuda.geometry("350x100")  # Establecer el tamaño de la ventana

        # Mostrar la información
        info = tk.Label(ventana_ayuda, text="Estudiante: Angel Guillermo de Jesús Pérez Jiménez\n"
                                            "Carnet: 202100215\n"
                                            "Correo: 3870961320101@ingenieria.usac.edu.gt")
        info.grid(row=0, column=0, columnspan=3, sticky='nsew')

        # Crear los botones
        boton1 = tk.Button(ventana_ayuda, text="Botón 1", command=abrir_link)
        boton1.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        boton2 = tk.Button(ventana_ayuda, text="Botón 2")
        boton2.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
        boton3 = tk.Button(ventana_ayuda, text="Botón 3")
        boton3.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

        # Configurar las columnas para que se expandan y llenen el espacio disponible
        ventana_ayuda.grid_columnconfigure(0, weight=1)
        ventana_ayuda.grid_columnconfigure(1, weight=1)
        ventana_ayuda.grid_columnconfigure(2, weight=1)


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

            # Crear el laberinto
            laberinto = maqueta.crear_laberinto()

            # Generar el archivo .dot
            maqueta.generar_dot(nombre_archivo='laberinto')
            maqueta.mostrar_imagen('laberinto.png')

    # Botón para cargar XML
    button_xml = tk.Button(master=app, text="Cargar XML", command=boton_XML)
    button_xml.grid(row=0, column=1, padx=20, pady=20)
    # Botón para gestión de maquetas
    button_gestion_maquetas = tk.Button(master=app, text="Limpiar Lista", command=boton_gestion_maquetas)
    button_gestion_maquetas.grid(row=0, column=2, padx=20, pady=20)
    # Botón para resolución de maquetas
    button_resolucion_maquetas = tk.Button(master=app, text="Resolución de maquetas", command=lambda: boton_resolucion_maquetas(lista_maquetas, combo_maquetas))
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


