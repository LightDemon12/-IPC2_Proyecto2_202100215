import xml.etree.ElementTree as ET


def leer_xml(ruta_archivo):
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        # Ahora puedes acceder a los elementos del archivo XML
        for child in root:
            print(child.tag, child.attrib)

    except ET.ParseError:
        print("Error al parsear el archivo XML")
    except FileNotFoundError:
        print("No se encontró el archivo XML")