import xml.etree.ElementTree as ET

class NodoObjetivo:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class NodoMaqueta:
    def __init__(self, nombre, filas, columnas, entrada, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada
        self.estructura = estructura
        self.objetivos = None
        self.siguiente = None

    def agregar_objetivo(self, nombre, fila, columna):
        nuevo_objetivo = NodoObjetivo(nombre, fila, columna)
        if self.objetivos is None:
            self.objetivos = nuevo_objetivo
        else:
            actual = self.objetivos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_objetivo

class LinkedListMaquetas:
    def __init__(self):
        self.primer_nodo = None

    def agregar_maqueta(self, maqueta):
        if self.primer_nodo is None:
            self.primer_nodo = maqueta
        else:
            actual = self.primer_nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = maqueta

    def mostrar_maquetas(self):
        if self.primer_nodo is None:
            print("No hay maquetas disponibles.")
        else:
            actual = self.primer_nodo
            while actual:
                print("Nombre de la maqueta:", actual.nombre)
                print("Filas:", actual.filas)
                print("Columnas:", actual.columnas)
                print("Entrada:", actual.entrada)
                print("Estructura:", actual.estructura)
                print("Objetivos:")
                objetivo_actual = actual.objetivos
                while objetivo_actual:
                    print("  Nombre:", objetivo_actual.nombre)
                    print("  Fila:", objetivo_actual.fila)
                    print("  Columna:", objetivo_actual.columna)
                    objetivo_actual = objetivo_actual.siguiente
                print()
                actual = actual.siguiente


def leer_xml(ruta_archivo):
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        maquetas_list = LinkedListMaquetas()

        for maqueta_xml in sorted(root.findall('maquetas/maqueta'), key=lambda maq: maq.find('nombre').text.strip()):
            nombre = maqueta_xml.find('nombre').text.strip()
            filas = int(maqueta_xml.find('filas').text.strip())
            columnas = int(maqueta_xml.find('columnas').text.strip())
            entrada = (int(maqueta_xml.find('entrada/fila').text.strip()), int(maqueta_xml.find('entrada/columna').text.strip()))
            estructura = maqueta_xml.find('estructura').text.strip()
            
            nueva_maqueta = NodoMaqueta(nombre, filas, columnas, entrada, estructura)
            
            for objetivo_xml in maqueta_xml.findall('objetivos/objetivo'):
                nombre_objetivo = objetivo_xml.find('nombre').text.strip()
                fila_objetivo = int(objetivo_xml.find('fila').text.strip())
                columna_objetivo = int(objetivo_xml.find('columna').text.strip())
                nueva_maqueta.agregar_objetivo(nombre_objetivo, fila_objetivo, columna_objetivo)
            
            maquetas_list.agregar_maqueta(nueva_maqueta)
        
        return maquetas_list

    except Exception as e:
        print(f"Error al procesar el archivo XML: {e}")
        return None


ruta_archivo = "archivo.xml"  # Ruta de tu archivo XML
maquetas_list = leer_xml(ruta_archivo)
if maquetas_list:
    print("Maquetas ordenadas alfabéticamente:")
    maquetas_list.mostrar_maquetas()
