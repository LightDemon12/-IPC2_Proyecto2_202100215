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

    def agregar_maqueta(self, maqueta):
        if not self.cabeza:
            self.cabeza = maqueta
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = maqueta
            maqueta.anterior = actual

        self.ordenar_maquetas()

    def ordenar_maquetas(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        cabeza_ordenada = None

        while self.cabeza is not None:
            nodo_actual = self.cabeza
            self.cabeza = self.cabeza.siguiente

            if cabeza_ordenada is None or cabeza_ordenada.nombre > nodo_actual.nombre:
                nodo_actual.siguiente = cabeza_ordenada
                cabeza_ordenada = nodo_actual
            else:
                nodo_actual_aux = cabeza_ordenada
                while nodo_actual_aux.siguiente is not None and nodo_actual_aux.siguiente.nombre < nodo_actual.nombre:
                    nodo_actual_aux = nodo_actual_aux.siguiente

                nodo_actual.siguiente = nodo_actual_aux.siguiente
                nodo_actual_aux.siguiente = nodo_actual

        self.cabeza = cabeza_ordenada

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

    def imprimir_todos(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Filas: {actual.num_filas}, Columnas: {actual.num_columnas}")
            print("Objetivos:")
            objetivo_actual = actual.objetivos
            while objetivo_actual:
                print(f"Nombre: {objetivo_actual.nombre}, Fila: {objetivo_actual.coordenada_fila}, Columna: {objetivo_actual.coordenada_columna}")
                objetivo_actual = objetivo_actual.siguiente
            print("Estructura:")
            estructura_actual = actual.estructura
            while estructura_actual:
                print(estructura_actual.caracter)
                estructura_actual = estructura_actual.siguiente
            actual = actual.siguiente
    def __iter__(self):
        nodo = self.cabeza
        while nodo is not None:
            yield nodo
            nodo = nodo.siguiente