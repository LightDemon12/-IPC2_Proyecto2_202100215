import xml.etree.ElementTree as ET

class NodoEstructura:
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None

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
        self.estructura = estructura  # Cambiar para almacenar nodos de estructura
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
                print("Estructura:")
                estructura_actual = actual.estructura
                while estructura_actual:
                    print("  Caracter:", estructura_actual.caracter)
                    estructura_actual = estructura_actual.siguiente
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
    print("Recibiendo ruta del archivo:", ruta_archivo)
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        maquetas_list = LinkedListMaquetas()

        for maqueta_xml in sorted(root.findall('maquetas/maqueta'), key=lambda maq: maq.find('nombre').text.strip()):
            nombre = maqueta_xml.find('nombre').text.strip()
            filas = int(maqueta_xml.find('filas').text.strip())
            columnas = int(maqueta_xml.find('columnas').text.strip())
            entrada = (int(maqueta_xml.find('entrada/fila').text.strip()), int(maqueta_xml.find('entrada/columna').text.strip()))

            nueva_maqueta = NodoMaqueta(nombre, filas, columnas, entrada, None)

            # Procesar estructura
            # Procesar estructura
            estructura_texto = maqueta_xml.find('estructura').text.strip()
            estructura_texto_filtrada = ''.join(filter(lambda x: x in ['*', '-'], estructura_texto))
            for caracter in estructura_texto_filtrada:
                nodo = NodoEstructura(caracter)
                if nueva_maqueta.estructura is None:
                    nueva_maqueta.estructura = nodo
                else:
                    actual = nueva_maqueta.estructura
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = nodo


            # Procesar objetivos
            objetivos = maqueta_xml.findall('objetivos/objetivo')
            for objetivo_xml in objetivos:
                nombre_objetivo = objetivo_xml.find('nombre').text.strip()
                fila_objetivo = int(objetivo_xml.find('fila').text.strip())
                columna_objetivo = int(objetivo_xml.find('columna').text.strip())
                nueva_maqueta.agregar_objetivo(nombre_objetivo, fila_objetivo, columna_objetivo)

            maquetas_list.agregar_maqueta(nueva_maqueta)

        # Mostrar maquetas después de procesar el archivo XML
        maquetas_list.mostrar_maquetas()

        return maquetas_list

    except Exception as e:
        print(f"Error al procesar el archivo XML: {e}")
        return None

