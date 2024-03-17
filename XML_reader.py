import xml.etree.ElementTree as ET

class NodoEstructura:
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None

class NodoMaqueta:
    def __init__(self, nombre_maqueta, estructura):
        self.nombre_maqueta = nombre_maqueta
        self.primer_nodo_estructura = None
        
        # Crear los nodos de la estructura y enlazarlos
        if estructura:
            for caracter in estructura:
                self.agregar_caracter_estructura(caracter)

    def agregar_caracter_estructura(self, caracter):
        nuevo_nodo = NodoEstructura(caracter)
        if self.primer_nodo_estructura is None:
            self.primer_nodo_estructura = nuevo_nodo
        else:
            actual = self.primer_nodo_estructura
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

class LinkedList:
    def __init__(self):
        self.primer_nodo_maqueta = None

    def agregar_maqueta(self, nombre_maqueta, estructura):
        nueva_maqueta = NodoMaqueta(nombre_maqueta, estructura)  
        if self.primer_nodo_maqueta is None:
            self.primer_nodo_maqueta = nueva_maqueta
        else:
            actual = self.primer_nodo_maqueta
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_maqueta  

    def mostrar_maquetas(self):
        if self.primer_nodo_maqueta is None:
            print("No hay maquetas en la lista.")
        else:
            actual = self.primer_nodo_maqueta
            while actual:
                print("Nombre de la maqueta:", actual.nombre_maqueta)
                # Aquí puedes imprimir más información de la maqueta si lo deseas
                actual = actual.siguiente



class XMLReader:
    @staticmethod
    def leer_xml(ruta_archivo):
        global informacion_xml
        informacion_xml = open(ruta_archivo).read()
        if informacion_xml:
            print("Leyendo archivo XML cargado...")
            # Procesar la información XML y almacenarla en listas enlazadas
            tree = ET.ElementTree(ET.fromstring(informacion_xml))
            root = tree.getroot()
            maquetas = LinkedList()
            for maqueta_xml in root.findall('maqueta'):
                nombre_maqueta = maqueta_xml.find('nombre').text.strip()
                filas = int(maqueta_xml.find('filas').text.strip())
                columnas = int(maqueta_xml.find('columnas').text.strip())
                entrada_xml = maqueta_xml.find('entrada')
                fila_entrada = int(entrada_xml.find('fila').text.strip())
                columna_entrada = int(entrada_xml.find('columna').text.strip())
                maqueta = NodoMaqueta(nombre_maqueta, filas, columnas, (fila_entrada, columna_entrada))
                estructura = maqueta_xml.find('estructura').text.strip()
                for caracter in estructura:
                    maqueta.agregar_caracter_estructura(caracter)
                objetivos_xml = maqueta_xml.find('objetivos')
                for objetivo_xml in objetivos_xml.findall('objetivo'):
                    nombre_objetivo = objetivo_xml.find('nombre').text.strip()
                    fila_objetivo = int(objetivo_xml.find('fila').text.strip())
                    columna_objetivo = int(objetivo_xml.find('columna').text.strip())
                    maqueta.agregar_objetivo(nombre_objetivo, fila_objetivo, columna_objetivo)
                maquetas.agregar_maqueta(maqueta)
            print("Procesamiento del XML completado.")
            return maquetas
        else:
            print("No se ha cargado ningún archivo XML.")
            return None

