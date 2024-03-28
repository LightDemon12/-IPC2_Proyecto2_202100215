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
class NodoPila:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Pila:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = NodoPila(value, self.top)

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

class NodoMovimiento:
    def __init__(self, nodo, next=None):
        self.nodo = nodo
        self.next = next

class ListaMovimientos:
    def __init__(self):
        self.head = None

    def append(self, nodo):
        if not self.head:
            self.head = NodoMovimiento(nodo)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = NodoMovimiento(nodo)

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


    def dfs(maqueta, inicio, objetivos):
        pila = Pila()
        pila.push((inicio, NodoEstructura(None)))  # NodoEstructura para el camino

        visitados = NodoEstructura(None)  # Lista enlazada para los nodos visitados
        objetivos_visitados = NodoEstructura(None)  # Lista enlazada para los objetivos visitados
        movimientos = ListaMovimientos()  # Lista enlazada para los movimientos

        while not pila.is_empty():
            nodo_actual, camino = pila.pop()

            # Comprobar si el nodo actual ya ha sido visitado
            actual = visitados
            while actual:
                if actual.caracter == nodo_actual:
                    break
                actual = actual.siguiente
            else:  # Si el nodo actual no ha sido visitado
                # Marcar el nodo actual como visitado
                visitado = NodoEstructura(nodo_actual)
                visitado.siguiente = visitados
                visitados = visitado

                # Añadir el nodo actual al camino
                paso = NodoEstructura(nodo_actual)
                paso.siguiente = camino
                camino = paso

                # Añadir el nodo actual a los movimientos
                movimientos.append(nodo_actual)

                # Comprobar si el nodo actual es uno de los objetivos
                objetivo_actual = objetivos
                while objetivo_actual:
                    if objetivo_actual.nombre == nodo_actual:
                        # Añadir el camino al nodo actual a los objetivos visitados
                        objetivo_visitado = NodoEstructura(camino)
                        objetivo_visitado.siguiente = objetivos_visitados
                        objetivos_visitados = objetivo_visitado
                        break
                    objetivo_actual = objetivo_actual.siguiente

                # Para cada vecino del nodo actual, si no está bloqueado, añádelo a la pila
                # Nota: necesitarás implementar un método para obtener los vecinos de un nodo en tu maqueta
                for vecino in maqueta.get_vecinos(nodo_actual):
                    pila.push((vecino, camino))

        return objetivos_visitados.siguiente, movimientos  # Devuelve los objetivos visitados y los movimientos

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
                        color = 'red'  # Los objetivos son cuadros rojos
                        break
                    objetivo_actual = objetivo_actual.siguiente

                tabla += f'<TD BGCOLOR="{color}"></TD>\n'
                nodo_actual = nodo_actual.siguiente
            tabla += '</TR>\n'
        tabla += '</TABLE>'

        dot.node('piso', label='<'+tabla+'>')
        dot.render(nombre_archivo, view=False)

    def generar_dot_dfs(self, movimientos, nombre_archivo='laberinto_dfs'):
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
                        color = 'red'  # Los objetivos son cuadros rojos
                        break
                    objetivo_actual = objetivo_actual.siguiente

                movimiento_actual = movimientos.head
                while movimiento_actual:
                    if i == movimiento_actual.nodo.coordenada_fila and j == movimiento_actual.nodo.coordenada_columna:
                        color = 'blue'  # Los movimientos son cuadros azules
                        break
                    movimiento_actual = movimiento_actual.next

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




