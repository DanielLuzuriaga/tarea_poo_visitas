# modelos/visitante.py

class Visitante:
    """
    ===============================
    MODELO (CAPA DE DATOS)
    ===============================

    Esta clase representa un visitante.

    ✔ Solo contiene atributos
    ✔ No tiene lógica de negocio
    ✔ Aplica Programación Orientada a Objetos (POO)
    """

    def __init__(self, cedula, nombre, motivo):
        """
        Constructor de la clase

        Parámetros:
        - cedula: identificador único
        - nombre: nombre completo
        - motivo: motivo de la visita
        """
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo