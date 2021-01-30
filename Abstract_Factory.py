from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    La interfaz AbstractFactory declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos se denominan familia y son relacionados
    por un concepto de alto nivel. Los productos de una familia suelen ser capaces
    de colaborar entre ellos. Una familia de productos puede tener varias variantes,
    pero los productos de una variante no son compatibles con los productos de otra
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    ConcreteFactory produce una familia de productos que pertenecen a una variante.
    Factory garantiza que los productos resultantes sean compatibles.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Nueva variante de producto a travéz de un ConcreteFactory
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz
    básica. Todas las variantes del producto deben implementar una interfaz
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Cada producto es creado por su correspondiente ConcreteFactory
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Resultado de producto A1"


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Resultado de producto A2."


class AbstractProductB(ABC):
    """
    Aqui se implementa la interfaz base de otra variante de producto. Todos los
    productos pueden interactuar entre si, pero la interacción adecuada solo es
    posible entre productos de la misma variante
    """

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        Abstract Factory se asegura de que todos los productos que crea sean de la
        misma variante y, por lo tanto compatibles
        """
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "Resultado de producto B1."

    """
    La variante Producto B1 solo puede funcionar correctamente con la variante
    Producto A1. Sin embargo, acepta cualquier instancia de AbstractProductA
    como un argumento
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado de B1 colaborando con ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "Resultado de producto B2 B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        La variante ProductoB2 solo puede funcionar correctamente con la variante
        Producto A2. De igual manera, acepta cualquier instancia de AbstractProductA
        como argumento
        """
        result = collaborator.useful_function_a()
        return f"Resultado de B2 colaborando con ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    El código de cliente funciona con fábricas y productos a través de AbstractFactory
    y AbstractProduct. Esto permite pasar por cualquier fábrica o subclase
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    El código de cliente puede funcionar con cualquier clase ConcreteFactory
    """
    print("Cliente: probando el código del cliente con el primer tipo de fábrica")
    client_code(ConcreteFactory1())

    print("\n")

    print("Cliente: probando el código del cliente con el segundo tipo de fábrica")
    client_code(ConcreteFactory2())