from collections import deque
from copy import deepcopy
import random
import time
from algorithm.node import Node


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return output

    return wrapper


from collections import deque
from copy import deepcopy
import random
import time
from algorithm.node import Node


def timer(func):
    """Decorator to measure the execution time of a function."""

    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return output

    return wrapper


class RoutingAlgorithm:
    """
    Inicializa una nueva instancia de RoutingAlgorithm.

    Parámetros:
        initial_solution (list[list[int]]): Solución inicial representada como una lista de rutas.
        distance_matrix (list[list[float]]): Matriz de distancias entre nodos.
        nodes (list[Node]): Lista de nodos en el problema.
        vehicle_capacity (float): Capacidad máxima de carga de los vehículos.
        iterations (int): Número de iteraciones para ejecutar el algoritmo de búsqueda.
    """

    def __init__(
        self,
        initial_solution: list[list],
        distance_matrix: list[list],
        nodes: Node,
        vehicle_capacity: float,
        iterations: int,
    ):
        self.nodes = nodes
        self.nodes_num = len(nodes)
        self.initial_solution = initial_solution
        self.distance_matrix = distance_matrix
        self.vehicle_capacity = vehicle_capacity
        self.iterations = iterations
        self.best_time = float("inf")
        self.best_solution = None
        self.used_starting_clients = set()

    def can_insert(self, new_path):
        """
        Verifica si es posible insertar un nuevo camino respetando las restricciones de carga y tiempo.

        Parámetros:
            new_path (list[int]): Camino propuesto para insertar.

        Retorna:
            bool: True si el camino puede ser insertado, False en caso contrario.
        """
        """Optimized version of can_insert to check if a new path is viable within load and time constraints."""
        carga_actual = 0
        tiempo_actual = 0
        tiempo_limite_depot = self.nodes[0].due_time

        for indice in range(len(new_path) - 1):
            nodo_actual = self.nodes[new_path[indice]]
            siguiente_nodo = self.nodes[new_path[indice + 1]]
            # Verificar restricción de carga
            if carga_actual + siguiente_nodo.demand > self.vehicle_capacity:
                return False
            # Calcular tiempo de viaje al siguiente nodo
            tiempo_viaje = self.distance_matrix[nodo_actual.id][siguiente_nodo.id]
            # Calcular tiempo de llegada al siguiente nodo
            tiempo_llegada = tiempo_actual + tiempo_viaje

            # Verificar restricción de ventana de tiempo en el siguiente nodo
            if tiempo_llegada > siguiente_nodo.due_time:
                return False
            # Calcular tiempo de espera si se llega antes del tiempo listo
            tiempo_espera = max(siguiente_nodo.ready_time - tiempo_llegada, 0)
            # Actualizar tiempo actual incluyendo el tiempo de servicio en el siguiente nodo
            tiempo_actual = tiempo_llegada + tiempo_espera + siguiente_nodo.service_time
            # Verificar si el retorno al depot se puede hacer dentro del tiempo límite del depot
            if (
                indice == len(new_path) - 2
            ):  # Verificar para el último nodo en el camino
                tiempo_retorno_depot = (
                    tiempo_actual + self.distance_matrix[siguiente_nodo.id][0]
                )  # Asumiendo que 0 es el ID del depot
                if tiempo_retorno_depot > tiempo_limite_depot:
                    return False
            # Actualizar carga actual
            carga_actual += siguiente_nodo.demand
        return True

    def total_cost_by_solution(self, solution):
        """
        Calcula el costo total de una solución basada en la suma de las distancias entre nodos consecutivos en todas las rutas.

        Parámetros:
            solution (list[list[int]]): Solución a evaluar.

        Retorna:
            float: Costo total de la solución.
        """
        total_cost = 0
        for route in solution:
            for i in range(len(route) - 1):
                total_cost += self.distance_matrix[route[i]][route[i + 1]]
        return total_cost

    def find_best_insert(self, routes, stm):
        """
        Encuentra la mejor inserción de un cliente en cualquier ruta considerando la lista tabú.

        Parámetros:
            routes (list[list[int]]): Rutas actuales.
            stm (deque): Lista tabú de movimientos recientes.

        Retorna:
            tuple: Mejor solución encontrada, cliente insertado y tiempo total de la solución.
        """
        best_solution = deepcopy(routes)
        best_time = float("inf")
        best_insertion = None
        for route_a_idx, route_a in enumerate(routes):
            for client_idx in range(1, len(route_a) - 1):
                current_solution = [route[:] for route in routes]
                current_client = current_solution[route_a_idx].pop(client_idx)
                if current_client in stm:
                    continue
                for route_b_idx, route_b in enumerate(current_solution):
                    for insert_idx in range(1, len(route_b)):
                        if route_b_idx == route_a_idx and client_idx == insert_idx:
                            continue
                        if self.can_insert(
                            current_solution[route_b_idx][:insert_idx]
                            + [current_client]
                            + current_solution[route_b_idx][insert_idx:]
                        ):
                            likely_routes = [r[:] for r in current_solution]
                            likely_routes[route_b_idx].insert(
                                insert_idx,
                                current_client,
                            )
                            total_time = self.total_cost_by_solution(likely_routes)
                            if total_time <= best_time:
                                best_time = total_time
                                best_insertion = current_client
                                best_solution = likely_routes
        return best_solution, best_insertion, best_time

    @timer
    def tabu_search(
        self,
        initial_planning,
        stm_length=10,
        intensify_threshold=100,
        diversify_threshold=300,
        max_no_diversify_=10,
    ):
        """
        Implementa la búsqueda tabú para mejorar la solución inicial.

        Parámetros:
            initial_planning (list[list[int]]): Planificación inicial.
            stm_length (int): Longitud de la lista tabú.
            intensify_threshold (int): Umbral para intensificar la búsqueda.
            diversify_threshold (int): Umbral para diversificar la búsqueda.
            max_no_diversify_ (int): Máximo número de veces para reiniciar la búsqueda desde la mejor solución sin diversificación.

        Retorna:
            tuple: Mejor solución encontrada y su costo total.
        """
        current_solution = [route[:] for route in initial_planning]
        stm = deque(maxlen=stm_length)  # Short-term memory for tabu list
        best_solution = [route[:] for route in current_solution]
        for route in best_solution:
            if not self.can_insert(route):
                best_time = float("inf")
                break
            best_time = self.total_cost_by_solution(current_solution)
        no_improvement_iterations = 0
        max_no_diversify = 0
        for iteration in range(self.iterations):
            current_solution, best_insertion, current_time = self.find_best_insert(
                current_solution, stm
            )
            if best_insertion:
                stm.append(best_insertion)  # Update the tabu list

            if current_time < best_time:
                best_solution = current_solution
                best_time = current_time
                no_improvement_iterations = 0
                max_no_diversify = 0
                print(
                    f"New best solution found at iteration {iteration} with cost {best_time}"
                )
            else:
                no_improvement_iterations += 1

            # Intensification: Focus search around the current best solution
            if no_improvement_iterations == intensify_threshold:
                print("Intensifying search...")
                current_solution = self.intensify_search(current_solution, stm)

            # Diversification: Explore new areas of the solution space
            if no_improvement_iterations >= diversify_threshold:
                print("Diversifying search...")
                current_solution = self.diversify_search(current_solution)
                no_improvement_iterations = 0  # Reset counter after diversification
                max_no_diversify += 1

            if max_no_diversify == max_no_diversify_:
                print("rerun best solution...")
                current_solution = best_solution
                no_improvement_iterations = 0
                max_no_diversify = 0
        return best_solution, best_time

    def intensify_search(self, best_solution, stm):
        """
        Intensifica la búsqueda alrededor de la mejor solución actual.

        Parámetros:
            best_solution (list[list[int]]): Mejor solución actual.
            stm (deque): Lista tabú de movimientos recientes.

        Retorna:
            list[list[int]]: Nueva mejor solución después de la intensificación.
        """
        for route_idx, route in enumerate(best_solution):
            for client_idx in range(1, len(route) - 1):
                client = route[client_idx]
                # Intenta mover este cliente a todas las posiciones posibles en la misma ruta
                for target_idx in range(1, len(route) - 1):
                    # Salta la posición original del cliente
                    if target_idx == client_idx:
                        continue

                    # Crea una nueva ruta con el cliente movido a la nueva posición
                    new_route = route[:client_idx] + route[client_idx + 1 :]
                    new_route.insert(target_idx, client)

                    # Verifica si la nueva ruta es válida y mejora la solución
                    if self.can_insert(new_route):
                        new_cost = self.total_cost_by_solution([new_route])
                        if new_cost < self.best_time:
                            best_solution[route_idx] = new_route
                            self.best_time = new_cost
                            # No es necesario agregar el cliente a stm, ya que solo se mueve dentro de la misma ruta
                            return best_solution

        return best_solution

    def diversify_search(self, current_solution):
        """
        Diversifica la búsqueda explorando nuevas áreas del espacio de soluciones.

        Parámetros:
            current_solution (list[list[int]]): Solución actual.

        Retorna:
            list[list[int]]: Nueva solución después de la diversificación.
        """
        new_solution = []
        all_clients = [
            client for route in current_solution for client in route[1:-1]
        ]  # Excluye los depósitos
        available_clients = (
            set(all_clients) - self.used_starting_clients
        )  # Excluye los clientes ya utilizados como puntos de partida

        if not available_clients:
            # Si todos los clientes han sido utilizados como puntos de partida, reinicia el conjunto
            self.used_starting_clients.clear()
            available_clients = set(all_clients)

        while all_clients:
            available_clients = set(all_clients) - self.used_starting_clients
            if not available_clients:
                # Si todos los clientes han sido utilizados como puntos de partida, reinicia el conjunto
                self.used_starting_clients.clear()
                available_clients = set(all_clients)
            new_route = [0]  # Inicia una nueva ruta desde el depósito
            # Convierte available_clients a una lista para usar random.choice()
            available_clients_list = list(available_clients)
            # Selecciona un cliente al azar como punto de partida de los disponibles
            current_client = random.choice(available_clients_list)
            self.used_starting_clients.add(current_client)
            all_clients.remove(current_client)
            new_route.append(current_client)
            while all_clients:
                closest_client, closest_distance = None, float("inf")
                for client in all_clients:
                    # Calcula la distancia desde el último cliente en la ruta
                    distance = self.distance_matrix[new_route[-1]][client]
                    # busca el cliente mas cercano y que se pueda insertar
                    if distance < closest_distance and self.can_insert(
                        new_route + [client] + [0]
                    ):
                        closest_client, closest_distance = client, distance
                if closest_client:
                    new_route.append(closest_client)
                    all_clients.remove(closest_client)
                else:
                    break
            new_route.append(0)  # Termina la ruta en el depósito
            new_solution.append(new_route)
        return (
            new_solution
            if self.total_cost_by_solution(new_solution) < self.best_time
            else current_solution
        )

    def run(self):
        """
        Ejecuta el algoritmo de búsqueda tabú y devuelve la mejor solución encontrada.

        Retorna:
            dict: Un diccionario que contiene las rutas de la mejor solución.
        """
        initial_planning = self.initial_solution
        stm_length = min(int(self.nodes_num / 5), 25)
        self.best_solution, best_time = self.tabu_search(
            initial_planning=initial_planning, stm_length=stm_length
        )
        self.best_solution = [route for route in self.best_solution if route != [0, 0]]
        print(f"best time solution : {best_time}")
        return {"routes": self.best_solution}


if __name__ == "__main__":
    filename = "data/r101.txt"
