from Interfaz.interfaz import iniciar_interfaz
from Logica.gestion_maquetas import NodoMaqueta, ListaMaquetas

def main():
    # Iniciar una lista vacía de maquetas
    lista_maquetas = ListaMaquetas()

    # Iniciar la interfaz con lista_maquetas
    iniciar_interfaz(lista_maquetas)

if __name__ == "__main__":
    main()


