from tkinter import filedialog

class SelectorArchivo:
    def __init__(self):
        self.ruta_archivo = None

    def seleccionar_archivo(self, funcion_leer_xml):
        self.ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
        if self.ruta_archivo != "":
            print("Archivo XML seleccionado:", self.ruta_archivo)
            funcion_leer_xml(self.ruta_archivo)
        else:
            print("No se seleccionó ningún archivo.")

    def obtener_ruta_archivo(self):
        return self.ruta_archivo