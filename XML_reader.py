import xml.etree.ElementTree as ET
from gestion_maquetas import NodoMaqueta, ListaMaquetas

def cargar_maquetas_desde_xml(ruta_archivo, lista_maquetas=None):
    print(f"Cargando maquetas desde el archivo: {ruta_archivo}")
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        if lista_maquetas is None:
            lista_maquetas = ListaMaquetas()

        for maqueta_xml in root.iter('maqueta'):
            maqueta = NodoMaqueta(
                nombre=maqueta_xml.find('nombre').text.strip(),
                num_filas=int(maqueta_xml.find('filas').text.strip()),
                num_columnas=int(maqueta_xml.find('columnas').text.strip()),
                coordenada_fila=int(maqueta_xml.find('entrada/fila').text.strip()),
                coordenada_columna=int(maqueta_xml.find('entrada/columna').text.strip())
            )

            for objetivo_xml in maqueta_xml.iter('objetivo'):
                maqueta.agregar_objetivo(
                    nombre=objetivo_xml.find('nombre').text.strip(),
                    coordenada_fila=int(objetivo_xml.find('fila').text.strip()),
                    coordenada_columna=int(objetivo_xml.find('columna').text.strip())
                )

            for caracter in maqueta_xml.find('estructura').text.strip():
                if not caracter.isspace():
                    maqueta.agregar_estructura(caracter)

            lista_maquetas.agregar_maqueta(maqueta)

        lista_maquetas.imprimir_todos()  # Nueva línea de código

        return lista_maquetas

    except ET.ParseError:
        print("Error al parsear el archivo XML")
    except FileNotFoundError:
        print("No se encontró el archivo XML")