class Target:
    """
    La clase Target define la interfaz específica del dominio utilizada
    por el código del cliente.
    """

    def request(self) -> str:
        return "Target: Comportamiento predeterminado."


class Adaptee:
    """
    Esta clase contiene una interfaz incompatible con el código existente.
    Necesita alguna adaptación antes de que el código pueda utilizarla.
    """

    def specific_request(self) -> str:
        return ".odatpadA laicepse otneimatropmoC"


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz Adaptee sea compatible con la de Target
    a través de herencia múltiple.
    """

    def request(self) -> str:
        return f"Adapter: (TRADUCIDO) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código implementado admite todas las clases que son compatibles con Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: Puedo trabajar correctamente con los objetos tipo Target")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: La clase Adaptee tiene una interfaz extraña. ")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: Pero puedo trabajar con ella a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)