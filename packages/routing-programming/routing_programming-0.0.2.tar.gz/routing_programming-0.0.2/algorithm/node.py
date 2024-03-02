class Node:
    def __init__(self, id, x, y, demand, ready_time, due_time, service_time):
        """
        Inicializa una nueva instancia de la clase Node.

        Parámetros:
            id (int): Identificador único del nodo.
            x (float): Coordenada x del nodo.
            y (float): Coordenada y del nodo.
            demand (int): Demanda asociada al nodo.
            ready_time (int): Tiempo más temprano en el que se puede comenzar el servicio en el nodo.
            due_time (int): Tiempo límite para comenzar el servicio en el nodo.
            service_time (int): Tiempo requerido para completar el servicio en el nodo.
        """
        self.id = id
        self.is_depot = id == 0
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_time = due_time
        self.service_time = service_time

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena de la instancia de Node, mostrando su identificador.

        Retorna:
            str: Representación en cadena del nodo.
        """
        return f"Node {self.id}"
