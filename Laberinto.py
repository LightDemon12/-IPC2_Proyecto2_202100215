from graphviz import Digraph
import tkinter as tk
from PIL import Image, ImageTk

class Nodo:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def crear_laberinto(estructura, filas, columnas):
    cabeza = None
    fila_actual = None

    for i in range(filas):
        fila = None
        nodo_actual = None
        for j in range(columnas):
            if nodo_actual is None:
                nodo_actual = Nodo(estructura[i*columnas + j])
                fila = nodo_actual
            else:
                nodo_actual.next = Nodo(estructura[i*columnas + j])
                nodo_actual = nodo_actual.next
        if fila_actual is None:
            fila_actual = Nodo(fila)
            cabeza = fila_actual
        else:
            fila_actual.next = Nodo(fila)
            fila_actual = fila_actual.next

    return cabeza

def obtener_celda(laberinto, fila, columna):
    fila_actual = laberinto
    for _ in range(fila):
        fila_actual = fila_actual.next

    celda = fila_actual.value
    for _ in range(columna):
        celda = celda.next

    return celda.value

class NodoLista:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def aplanar_lista(lista_de_listas):
    return [item for sublist in lista_de_listas for item in sublist]

def dfs(laberinto, filas, columnas, inicio, objetivos):
    cabeza = NodoLista((inicio, []))
    visitados = set()
    objetivos_visitados = []

    while cabeza is not None:
        (fila, columna), camino = cabeza.value
        cabeza = cabeza.next

        if (fila, columna) in visitados:
            continue

        visitados.add((fila, columna))
        camino = camino + [(fila, columna)]

        if (fila, columna) in objetivos:
            objetivos_visitados.append(camino)

        if fila > 0 and obtener_celda(laberinto, fila-1, columna) != '*':
            cabeza = NodoLista(((fila-1, columna), camino), cabeza)
        if fila < filas-1 and obtener_celda(laberinto, fila+1, columna) != '*':
            cabeza = NodoLista(((fila+1, columna), camino), cabeza)
        if columna > 0 and obtener_celda(laberinto, fila, columna-1) != '*':
            cabeza = NodoLista(((fila, columna-1), camino), cabeza)
        if columna < columnas-1 and obtener_celda(laberinto, fila, columna+1) != '*':
            cabeza = NodoLista(((fila, columna+1), camino), cabeza)

    return objetivos_visitados

def generar_dot(laberinto, filas, columnas, objetivos, entrada, recorrido=None, nombre_archivo='laberinto'):
    dot = Digraph('G', node_attr={'shape': 'plaintext'}, format='png')

    tabla = '<TABLE border="1" cellspacing="0" cellpadding="10">\n'
    fila_actual = laberinto
    for i in range(filas):
        tabla += '<TR>\n'
        nodo_actual = fila_actual.value
        for j in range(columnas):
            color = 'black' if nodo_actual.value == '*' else 'white'
            if (i, j) in objetivos:
                color = 'red'
            if (i, j) == entrada:
                color = 'green'
            if recorrido and (i, j) in recorrido:
                color = 'blue'
            tabla += f'<TD BGCOLOR="{color}"></TD>\n'
            nodo_actual = nodo_actual.next
        tabla += '</TR>\n'
        fila_actual = fila_actual.next
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

estructura = "*-*-*****-*-----------*****--**-*----****--*-*--*----**-******--*--*-------********-*------*-------"
filas = 9
columnas = 11
objetivos = [(0, 3), (2, 6), (3, 8), (3, 3), (8, 1)]
entrada = (0, 2)
laberinto = crear_laberinto(estructura, filas, columnas)
generar_dot(laberinto, filas, columnas, objetivos, entrada, nombre_archivo='laberinto_inicial')


camino = dfs(laberinto, filas, columnas, entrada, objetivos)
if camino is None:
    print("No se encontró un camino a los objetivos.")
else:
    print("Se encontró un camino a los objetivos:", camino)
    camino_aplanado = aplanar_lista(camino)
    generar_dot(laberinto, filas, columnas, objetivos, entrada, camino_aplanado, nombre_archivo='laberinto_con_recorrido')
# Crear la ventana principal y ocultarla
ventana_principal = tk.Tk()
ventana_principal.withdraw()

# Crear las ventanas con las imágenes
ventana1 = mostrar_imagen('laberinto_inicial.png')
ventana2 = mostrar_imagen('laberinto_con_recorrido.png')

# Llamar a mainloop una vez que todas las ventanas estén creadas
ventana_principal.mainloop()
