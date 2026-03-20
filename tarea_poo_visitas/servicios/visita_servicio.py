# servicios/visita_servicio.py

import json
import os
from modelos.visitante import Visitante


class VisitaServicio:
    """
    ===============================
    CAPA DE SERVICIO (LÓGICA)
    ===============================

    Aquí se implementa TODA la lógica del sistema:

    ✔ CRUD (Crear, Leer, Actualizar, Eliminar)
    ✔ Validaciones
    ✔ Persistencia en JSON

    🔒 Encapsulamiento:
    La lista de visitantes es privada (_visitantes)
    """

    def __init__(self):
        """
        Constructor del servicio

        - Inicializa lista de visitantes
        - Define archivo JSON
        - Carga datos guardados
        """
        self._visitantes = []  # lista privada
        self.archivo = "visitantes.json"

        self.cargar_datos()  # carga datos al iniciar

    # ================= CRUD =================

    def registrar_visitante(self, visitante):
        """
        CREATE → Registrar visitante

        ✔ Verifica que la cédula no esté repetida
        ✔ Guarda en JSON si es válido
        """
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False  # cédula duplicada

        self._visitantes.append(visitante)
        self.guardar_datos()
        return True

    def obtener_visitantes(self):
        """
        READ → Obtener lista de visitantes
        """
        return self._visitantes

    def eliminar_visitante(self, cedula):
        """
        DELETE → Eliminar visitante por cédula
        """
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                self.guardar_datos()
                return True
        return False

    def actualizar_visitante(self, cedula, nuevo_nombre, nuevo_motivo):
        """
        UPDATE → Editar visitante

        ✔ Busca por cédula
        ✔ Actualiza nombre y motivo
        ✔ Guarda en JSON
        """
        for v in self._visitantes:
            if v.cedula == cedula:
                v.nombre = nuevo_nombre
                v.motivo = nuevo_motivo
                self.guardar_datos()
                return True
        return False

    # ================= JSON =================

    def guardar_datos(self):
        """
        Guarda los visitantes en un archivo JSON

        ✔ Convierte objetos a diccionarios
        ✔ Permite persistencia de datos
        """
        data = []

        for v in self._visitantes:
            data.append({
                "cedula": v.cedula,
                "nombre": v.nombre,
                "motivo": v.motivo
            })

        with open(self.archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar_datos(self):
        """
        Carga los datos desde el JSON al iniciar

        ✔ Permite que los datos no se pierdan
        """
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                data = json.load(f)

                for item in data:
                    visitante = Visitante(
                        item["cedula"],
                        item["nombre"],
                        item["motivo"]
                    )
                    self._visitantes.append(visitante)