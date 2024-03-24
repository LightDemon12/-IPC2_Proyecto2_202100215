from tkinter import filedialog
from XML_reader import leer_xml

ruta_archivo = None  # Variable global para almacenar la ruta del archivo XML

def seleccionar_archivo(funcion_leer_xml):
    global ruta_archivo  # Declarar ruta_archivo como global
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
    if ruta_archivo != "":
        print("Archivo XML seleccionado:", ruta_archivo)
        funcion_leer_xml(ruta_archivo)
    else:
        print("No se seleccionó ningún archivo.")
