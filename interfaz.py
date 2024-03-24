import tkinter as tk
import customtkinter
from seleccion_archivo import seleccionar_archivo
from XML_reader import leer_xml

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1200x720")

def boton_XML():
    seleccionar_archivo(leer_xml)  # Pasar la función leer_xml como argumento

def boton_gestion_maquetas():
    print("boton_gestion_maquetas presionado")

def boton_resolucion_maquetas():
    print("boton_resolucion_maquetas presionado")

def boton_ayuda():
    print("boton_ayuda presionado")

# Botón para cargar XML
button_xml = customtkinter.CTkButton(master=app, text="Cargar XML", command=boton_XML)
button_xml.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Botón para gestión de maquetas
button_gestion_maquetas = customtkinter.CTkButton(master=app, text="Gestión de maquetas", command=boton_gestion_maquetas)
button_gestion_maquetas.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

# Botón para resolución de maquetas
button_resolucion_maquetas = customtkinter.CTkButton(master=app, text="Resolución de maquetas", command=boton_resolucion_maquetas)
button_resolucion_maquetas.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

# Botón para ayuda
button_ayuda = customtkinter.CTkButton(master=app, text="Ayuda", command=boton_ayuda)
button_ayuda.grid(row=0, column=4, padx=20, pady=20, sticky="nsew")

# Configurar el espaciado uniforme de las columnas
app.grid_columnconfigure((0, 5), weight=1)

app.mainloop()
