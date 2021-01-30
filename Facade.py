from __future__ import annotations

class Facade:
    """
    La clase Facade proporciona una interfaz simple a la lógica compleja de uno o
    varios subsistemas. Facade delega las solicitudes del cliente a los objetos
    apropiados dentro del sistema. Facade también es responsable de gestionar todo
    su ciclo de vida. Todo esto protege al cliente de la complejidad no deseada
    del subsistema
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Dependiendo de las necesidades de la aplicación, se le pueden proporcionar
        a Facade objetos del subsistema existentes o forarlo a crearlos por si mismo
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        Los métodos Facade son atajos convenientes para la funcionalidad sofisticada
        de los subsistemas. Sin embargo, los clientes obtienen solo una fracción de las
        capacidades de un subsistema
        """

        results = []
        results.append("Facade inicializa subsistemas:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade ordena a los subsistemas comiencen a trabajar:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    El Subsistema puede aceptar solicitudes tanto de Facade como del cliente.
    Para el Subsistema, Facade es un cliente más
    """

    def operation1(self) -> str:
        return "Subsystem1: Listo!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Inicio!"


class Subsystem2:
    """
    Algunos Facade pueden funcionar con varios subsistemas al mismo tiempo
    """

    def operation1(self) -> str:
        return "Subsystem2: Prepararse!"

    def operation_z(self) -> str:
        return "Subsystem2: Fuego!"


def client_code(facade: Facade) -> None:
    """
    El código del cliente funciona con subsistemas complejos a través de una interfaz
    simple proporcionada por Facade. Cuando Facade gestiona el ciclo de vida del
    subsistema, es posible que el cliente ni siquiera sepa sobre la existencia del
    subsistema. Este enfoque le permite mantener la complejidad bajo control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)