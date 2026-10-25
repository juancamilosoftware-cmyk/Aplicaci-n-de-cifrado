"""Capa de dominio: reglas de validación y transformación de los datos."""

ORDEN = (2, 3, 0, 1, 5, 4)


def validar_entrada(texto: str) -> str:
    """Quita espacios exteriores y exige seis dígitos ASCII."""
    texto = texto.strip()
    if len(texto) != 6 or any(caracter not in "0123456789" for caracter in texto):
        raise ValueError("Ingrese exactamente seis dígitos del 0 al 9, sin signos, letras, espacios internos ni decimales.")
    return texto


def cifrar(texto: str) -> str:
    texto = validar_entrada(texto)
    transformados = "".join(str((int(digito) + 7) % 10) for digito in texto)
    return "".join(transformados[indice] for indice in ORDEN)


def descifrar(texto: str) -> str:
    texto = validar_entrada(texto)
    # Los tres intercambios se deshacen repitiendo la misma permutación.
    reordenados = "".join(texto[indice] for indice in ORDEN)
    return "".join(str((int(digito) - 7) % 10) for digito in reordenados)
