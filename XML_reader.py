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
        nuevo_nodo = NodoMaqueta(nombre_maqueta, estructura)
        if self.primer_nodo_maqueta is None:
            self.primer_nodo_maqueta = nuevo_nodo
        else:
            actual = self.primer_nodo_maqueta
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo






class XMLReader:
    @staticmethod
    def leer_xml(nombre_archivo):
        # Lógica para leer y procesar el archivo XML
        print(f"Leyendo archivo XML: {nombre_archivo}")

