def validar_texto(campo, valor):
    """Validar que el texto no esté vacío y solo contenga letras."""
    if not valor.strip():
        raise ValueError(f"El campo '{campo}' no puede estar vacío.")
    if not valor.replace(" ", "").isalpha():
        raise ValueError(f"El campo '{campo}' solo puede contener letras.")
    return valor.strip()

def validar_numero(campo, valor):
    """Validar que sea un número válido."""
    try:
        return float(valor)
    except ValueError:
        raise ValueError(f"El campo '{campo}' debe ser un número válido.")

def validar_entero(campo, valor):
    """Validar que sea un número entero."""
    try:
        return int(valor)
    except ValueError:
        raise ValueError(f"El campo '{campo}' debe ser un número entero.")