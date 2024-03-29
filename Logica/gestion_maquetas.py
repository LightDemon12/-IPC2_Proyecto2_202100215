from graphviz import Digraph
from graphviz import Digraph
import tkinter as tk
from PIL import Image, ImageTk

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

    def obtener_estructura(self):
        estructura = ""
        actual = self.estructura
        while actual:
            estructura += actual.caracter 
            actual = actual.siguiente
        return estructura[:-1]  # Eliminar la última nueva línea

    def obtener_objetivos(self):
        objetivos = ""
        actual = self.objetivos
        while actual:
            objetivos += f"Nombre: {actual.nombre}, Fila: {actual.coordenada_fila}, Columna: {actual.coordenada_columna}\n"
            actual = actual.siguiente
        return objetivos[:-1]  # Eliminar la última nueva línea
    


    def crear_laberinto(self):
        # Crear una nueva lista enlazada para el laberinto
        laberinto = NodoEstructura(None)

        # Copiar la estructura de la maqueta a la lista enlazada del laberinto
        nodo_actual = self.estructura
        nodo_laberinto = laberinto
        while nodo_actual:
            nodo_laberinto.siguiente = NodoEstructura(nodo_actual.caracter)
            nodo_laberinto = nodo_laberinto.siguiente
            nodo_actual = nodo_actual.siguiente
        return laberinto.siguiente  # Devuelve el laberinto creado (omitimos el primer nodo que era un placeholder)


    def crear_laberintoDFS(self, num_filas, num_columnas):
        # Crear una nueva lista enlazada para el laberinto
        laberinto = ListaDFS()

        # Copiar la estructura de la maqueta a la lista enlazada del laberinto
        nodo_actual = self.estructura
        for i in range(num_filas):
            for j in range(num_columnas):
                caracter = nodo_actual.caracter
                if (i, j) == (self.coordenada_fila, self.coordenada_columna):  # Si es la entrada
                    caracter = '#'
                else:
                    objetivo_actual = self.objetivos
                    while objetivo_actual:
                        if i == objetivo_actual.coordenada_fila and j == objetivo_actual.coordenada_columna:  # Si es un objetivo
                            caracter = '|'
                            break
                        objetivo_actual = objetivo_actual.siguiente
                laberinto.agregar_nodo(caracter, i, j)
                nodo_actual = nodo_actual.siguiente
        return laberinto  # Devuelve el laberinto creado

    def generar_dot(self, nombre_archivo='laberinto'):
        dot = Digraph('G', node_attr={'shape': 'plaintext'}, format='png')

        tabla = '<TABLE border="1" cellspacing="0" cellpadding="10">\n'
        nodo_actual = self.estructura
        for i in range(self.num_filas):
            tabla += '<TR>\n'
            for j in range(self.num_columnas):
                color = 'black' if nodo_actual.caracter == '*' else 'white'  

                if i == self.coordenada_fila  and j == self.coordenada_columna:  
                    color = 'green'  # La entrada es un cuadro verde

    
                objetivo_actual = self.objetivos
                while objetivo_actual:
                    if i == objetivo_actual.coordenada_fila and j == objetivo_actual.coordenada_columna:  
                        color = 'yellow'  # Los objetivos son cuadros rojos
                        break
                    objetivo_actual = objetivo_actual.siguiente

                tabla += f'<TD BGCOLOR="{color}"></TD>\n'
                nodo_actual = nodo_actual.siguiente
            tabla += '</TR>\n'
        tabla += '</TABLE>'

        dot.node('piso', label='<'+tabla+'>')
        dot.render(nombre_archivo, view=False)


    def mostrar_imagen(self, ruta_imagen):
        ventana = tk.Toplevel()  # Cambiar tk.Tk() a tk.Toplevel()
        imagen = Image.open(ruta_imagen)
        imagen_tk = ImageTk.PhotoImage(imagen)
        etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
        etiqueta_imagen.pack()
        etiqueta_imagen.imagen = imagen_tk
        return ventana


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
            
    def obtener_nombres(self):
        nombres = ""
        for maqueta in self:
            nombres += maqueta.nombre + "\n"
        return nombres[:-1]  # Eliminar la última nueva línea
    
    def eliminar_todas(self):
        self.cabeza = None

    def obtener_num_filas(self, nombre):
        nodo_maqueta = self.buscar_por_nombre(nombre)
        if nodo_maqueta is not None:
            return nodo_maqueta.num_filas
        else:
            return None

    def obtener_num_columnas(self, nombre):
        nodo_maqueta = self.buscar_por_nombre(nombre)
        if nodo_maqueta is not None:
            return nodo_maqueta.num_columnas
        else:
            return None

class NodoDFS:
    def __init__(self, caracter, fila=None, columna=None, siguiente=None):
        self.caracter = caracter
        self.fila = fila
        self.columna = columna
        self.siguiente = siguiente


class ListaDFS:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, caracter, fila, columna):
        nuevo_nodo = NodoDFS(caracter, fila, columna)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
    def pop(self):
        if self.cabeza is None:
            return None
        nodo = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return nodo
    
    def mostrarListaDFS(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f'Caracter: {nodo_actual.caracter}, Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}')
            nodo_actual = nodo_actual.siguiente

    def obtener_celda(self, fila, columna):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

    def obtener_inicio(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.caracter == '#':
                return (nodo_actual.fila, nodo_actual.columna)
            nodo_actual = nodo_actual.siguiente
        return None

class ListaRecorrido:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, caracter, fila, columna):
        nuevo_nodo = NodoDFS(caracter, fila, columna)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def mostrarListaRecorrido(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f'Caracter: {nodo_actual.caracter}, Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}')
            nodo_actual = nodo_actual.siguiente

    def obtener_celda(self, fila, columna):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.fila == fila and nodo_actual.columna == columna:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None
    
def dfs(laberinto, inicio):
    cabeza = ListaDFS()
    inicio_fila, inicio_columna = inicio
    cabeza.agregar_nodo('#', inicio_fila, inicio_columna)  # Añade el nodo de inicio a la cabeza
    visitados = ListaDFS()
    objetivos_visitados = ListaDFS()
    recorrido_completo = ListaRecorrido()  # Almacena todos los nodos a los que se mueve el algoritmo

    while cabeza.cabeza is not None:
        nodo_actual = cabeza.pop()
        recorrido_completo.agregar_nodo(nodo_actual.caracter, nodo_actual.fila, nodo_actual.columna)  # Agrega el nodo a recorrido_completo
        fila, columna = nodo_actual.fila, nodo_actual.columna

        if visitados.obtener_celda(fila, columna) is not None:  # Si el nodo ya ha sido visitado
            continue

        print(f'Visitando nodo: ({fila}, {columna})')  # Imprime las coordenadas del nodo visitado

        if nodo_actual.caracter == '|':  # Si el nodo es un objetivo
            objetivos_visitados.agregar_nodo(nodo_actual.caracter, fila, columna)

        # Mover hacia arriba
        dx, dy = -1, 0
        vecino = laberinto.obtener_celda(fila + dx, columna + dy)
        if vecino is not None and vecino.caracter != '*':
            cabeza.agregar_nodo(vecino.caracter, fila + dx, columna + dy)

        # Mover hacia abajo
        dx, dy = 1, 0
        vecino = laberinto.obtener_celda(fila + dx, columna + dy)
        if vecino is not None and vecino.caracter != '*':
            cabeza.agregar_nodo(vecino.caracter, fila + dx, columna + dy)

        # Mover hacia la izquierda
        dx, dy = 0, -1
        vecino = laberinto.obtener_celda(fila + dx, columna + dy)
        if vecino is not None and vecino.caracter != '*':
            cabeza.agregar_nodo(vecino.caracter, fila + dx, columna + dy)

        # Mover hacia la derecha
        dx, dy = 0, 1
        vecino = laberinto.obtener_celda(fila + dx, columna + dy)
        if vecino is not None and vecino.caracter != '*':
            cabeza.agregar_nodo(vecino.caracter, fila + dx, columna + dy)

        visitados.agregar_nodo(nodo_actual.caracter, fila, columna)  # Marca el nodo como visitado después de explorar todos sus vecinos

    print("Recorrido completo:")
    recorrido_completo.mostrarListaRecorrido()  # Muestra el recorrido completo

    return objetivos_visitados, recorrido_completo




def generar_dot_DFS(lista_maquetas, nombre_maqueta, recorrido_completo, visitados, nombre_archivo='recorrido_dfs'):
    dot = Digraph('G', node_attr={'shape': 'plaintext'}, format='png')

    # Obtener la maqueta de la lista
    maqueta = lista_maquetas.buscar_por_nombre(nombre_maqueta)

    # Generar la tabla a partir de la estructura de la maqueta
    tabla = '<TABLE border="1" cellspacing="0" cellpadding="10">\n'
    nodo_actual = maqueta.estructura
    for i in range(maqueta.num_filas):
        tabla += '<TR>\n'
        for j in range(maqueta.num_columnas):
            color = 'black' if nodo_actual.caracter == '*' else 'white'

            if i == maqueta.coordenada_fila and j == maqueta.coordenada_columna:
                color = 'green'  # La entrada es un cuadro verde

            objetivo_actual = maqueta.objetivos
            while objetivo_actual:
                if i == objetivo_actual.coordenada_fila and j == objetivo_actual.coordenada_columna:
                    color = 'red'  # Los objetivos son cuadros rojos
                    break
                objetivo_actual = objetivo_actual.siguiente

            # Comprobar si el nodo actual está en el recorrido
            nodo_recorrido = recorrido_completo.cabeza
            while nodo_recorrido is not None:
                if nodo_recorrido.fila == i and nodo_recorrido.columna == j:
                    color = 'purple'  # Los nodos en el recorrido son cuadros morados
                    break
                nodo_recorrido = nodo_recorrido.siguiente

            # Comprobar si el nodo actual ha sido visitado
            nodo_visitado = visitados.obtener_celda(i, j)
            if nodo_visitado is not None:
                color = 'blue'  # Los nodos visitados son cuadros azules

            tabla += f'<TD BGCOLOR="{color}"></TD>\n'
            nodo_actual = nodo_actual.siguiente
        tabla += '</TR>\n'
    tabla += '</TABLE>'

    dot.node('piso', label='<'+tabla+'>')
    dot.render(nombre_archivo, view=False)

def generar_dot_objetivos_alcanzados(lista_maquetas, nombre_maqueta, visitados, nombre_archivo='ALCANZADOS_dfs'):
    dot = Digraph('G', node_attr={'shape': 'plaintext'}, format='png')

    # Obtener la maqueta de la lista
    maqueta = lista_maquetas.buscar_por_nombre(nombre_maqueta)

    # Generar la tabla a partir de la estructura de la maqueta
    tabla = '<TABLE border="1" cellspacing="0" cellpadding="10">\n'
    nodo_actual = maqueta.estructura
    for i in range(maqueta.num_filas):
        tabla += '<TR>\n'
        for j in range(maqueta.num_columnas):
            color = 'black' if nodo_actual.caracter == '*' else 'white'

            if i == maqueta.coordenada_fila and j == maqueta.coordenada_columna:
                color = 'green'  # La entrada es un cuadro verde

            objetivo_actual = maqueta.objetivos
            while objetivo_actual:
                if i == objetivo_actual.coordenada_fila and j == objetivo_actual.coordenada_columna:
                    color = 'red'  # Los objetivos son cuadros rojos
                    break
                objetivo_actual = objetivo_actual.siguiente

            # Comprobar si el nodo actual está en la lista de nodos visitados
            nodo_visitado = visitados.cabeza
            while nodo_visitado is not None:
                if nodo_visitado.fila == i and nodo_visitado.columna == j:
                    color = 'blue'  # Los nodos visitados son cuadros azules
                    break
                nodo_visitado = nodo_visitado.siguiente

            tabla += f'<TD BGCOLOR="{color}"></TD>\n'
            nodo_actual = nodo_actual.siguiente
        tabla += '</TR>\n'
    tabla += '</TABLE>'

    dot.node('piso', label='<'+tabla+'>')
    dot.render(nombre_archivo, view=False)

def mostrar_imagen(ruta_imagen):
    ventana = tk.Toplevel()  # Cambiar tk.Tk() a tk.Toplevel()
    imagen = Image.open(ruta_imagen)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    etiqueta_imagen.pack()
    etiqueta_imagen.imagen = imagen_tk
    return ventana

def contar_objetivos_visitados(objetivos, visitados):
    total_objetivos = 0
    objetivos_visitados = 0
    objetivo_actual = objetivos

    while objetivo_actual is not None:
        if hasattr(objetivo_actual, 'fila') and hasattr(objetivo_actual, 'columna'):
            total_objetivos += 1
            if visitados.obtener_celda(objetivo_actual.fila, objetivo_actual.columna) is not None:
                objetivos_visitados += 1
        objetivo_actual = objetivo_actual.siguiente

    return objetivos_visitados, total_objetivos