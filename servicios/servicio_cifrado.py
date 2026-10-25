"""Casos de uso que la presentación puede solicitar al dominio."""
from dominio import algoritmos


class ServicioCifrado:
    """Expone las operaciones sin conocer ventanas ni controles gráficos."""

    def cifrar(self, entrada: str) -> str:
        return algoritmos.cifrar(entrada)

    def descifrar(self, entrada: str) -> str:
        return algoritmos.descifrar(entrada)
