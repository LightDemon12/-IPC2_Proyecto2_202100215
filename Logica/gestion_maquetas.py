class NodoEstructura:
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None
        self.anterior = None

class NodoObjetivo:
    def __init__(self, nombre, coordenada_fila, coordenada_columna):
        self.nombre = nombre
        self.coordenada_fila = coordenada_fila
        self.coordenada_columna = coordenada_columna
        self.siguiente = None
        self.anterior = None

class NodoMaqueta:
    def __init__(self, nombre, num_filas, num_columnas, coordenada_fila, coordenada_columna):
        self.nombre = nombre
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.coordenada_fila = coordenada_fila
        self.coordenada_columna = coordenada_columna
        self.objetivos = None  # Primer nodo de la lista de objetivos
        self.estructura = None  # Primer nodo de la lista de estructura
        self.siguiente = None
        self.anterior = None

    def agregar_objetivo(self, nombre, coordenada_fila, coordenada_columna):
        nuevo_objetivo = NodoObjetivo(nombre, coordenada_fila, coordenada_columna)
        if not self.objetivos:
            self.objetivos = nuevo_objetivo
        else:
            actual = self.objetivos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_objetivo
            nuevo_objetivo.anterior = actual

    def agregar_estructura(self, caracter):
        nueva_estructura = NodoEstructura(caracter)
        if not self.estructura:
            self.estructura = nueva_estructura
        else:
            actual = self.estructura
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_estructura
            nueva_estructura.anterior = actual

class ListaMaquetas:
    def __init__(self):
        self.cabeza = None

    def buscar_por_nombre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def obtener_estructura(self, nombre):
        maqueta = self.buscar_por_nombre(nombre)
        if maqueta:
            return maqueta.obtener_estructura()
        else:
            print(f"No se encontró ninguna maqueta con el nombre {nombre}")
            return None

    def obtener_objetivos(self, nombre):
        maqueta = self.buscar_por_nombre(nombre)
        if maqueta:
            return maqueta.obtener_objetivos()
        else:
            print(f"No se encontró ninguna maqueta con el nombre {nombre}")
            return None