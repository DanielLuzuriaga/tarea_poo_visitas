# main.py

import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter


def main():
    """
    ===============================
    PUNTO DE ENTRADA
    ===============================

    ✔ Crea la ventana principal
    ✔ Crea el servicio (lógica)
    ✔ Inyecta el servicio en la UI
    """

    root = tk.Tk()

    servicio = VisitaServicio()
    app = AppTkinter(root, servicio)

    root.mainloop()


if __name__ == "__main__":
    main()