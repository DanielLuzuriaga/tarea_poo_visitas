# ui/app_tkinter.py

import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante


class AppTkinter:
    """
    ===============================
    CAPA UI (INTERFAZ GRÁFICA)
    ===============================

    ✔ Maneja la interfaz visual
    ✔ No contiene lógica de negocio
    ✔ Usa el servicio mediante inyección de dependencias
    """

    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        # ================= CONFIGURACIÓN =================
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("700x500")
        self.root.configure(bg="#e9ecef")

        # ================= ENCABEZADO =================

        tk.Label(
            root,
            text="Universidad Estatal Amazónica",
            font=("Arial", 16, "bold"),
            fg="#2c3e50",
            bg="#e9ecef"
        ).pack(pady=5)

        tk.Label(
            root,
            text="Sistema de Registro de Visitantes",
            font=("Arial", 12),
            bg="#e9ecef"
        ).pack()

        tk.Label(
            root,
            text="Realizado por: Daniel Luzuriaga",
            font=("Arial", 10, "italic"),
            bg="#e9ecef"
        ).pack(pady=5)

        # Línea separadora
        ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=5)

        # ================= FORMULARIO =================
        frame_form = tk.LabelFrame(root, text="Datos del Visitante", bg="#e9ecef")
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Cédula:", bg="#e9ecef").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(frame_form, text="Nombre:", bg="#e9ecef").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Motivo:", bg="#e9ecef").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(frame_form)
        self.entry_motivo.grid(row=2, column=1)

        # ================= BOTONES =================
        frame_btn = tk.Frame(root, bg="#e9ecef")
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Registrar", width=12, command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Editar", width=12, command=self.editar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Eliminar", width=12, command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="Limpiar", width=12, command=self.limpiar).grid(row=0, column=3, padx=5)

        # ================= BUSCAR =================
        frame_buscar = tk.Frame(root, bg="#e9ecef")
        frame_buscar.pack(pady=5)

        tk.Label(frame_buscar, text="Buscar cédula:", bg="#e9ecef").grid(row=0, column=0)
        self.entry_buscar = tk.Entry(frame_buscar)
        self.entry_buscar.grid(row=0, column=1)

        tk.Button(frame_buscar, text="Buscar", command=self.buscar).grid(row=0, column=2, padx=5)
        tk.Button(frame_buscar, text="Mostrar Todo", command=self.actualizar_tabla).grid(row=0, column=3)

        # ================= TABLA =================
        frame_tabla = tk.Frame(root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("Cedula", "Nombre", "Motivo"),
            show="headings"
        )

        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")

        self.tree.pack(fill="both", expand=True)

        # Evento: al seleccionar fila → cargar datos
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        # Cargar datos iniciales
        self.actualizar_tabla()

    # ================= FUNCIONES =================

    def registrar(self):
        """
        Registra un visitante
        """
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Campos obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)

        if self.servicio.registrar_visitante(visitante):
            messagebox.showinfo("OK", "Registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "Cédula duplicada")

    def editar(self):
        """
        EDITAR (UPDATE)
        """
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if self.servicio.actualizar_visitante(cedula, nombre, motivo):
            messagebox.showinfo("OK", "Actualizado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "No existe")

    def eliminar(self):
        """
        Elimina un visitante
        """
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        if not messagebox.askyesno("Confirmar", "¿Eliminar registro?"):
            return

        item = self.tree.item(seleccion)
        cedula = item["values"][0]

        self.servicio.eliminar_visitante(cedula)
        self.actualizar_tabla()

    def buscar(self):
        """
        Busca visitante por cédula
        """
        cedula = self.entry_buscar.get()

        for fila in self.tree.get_children():
            self.tree.delete(fila)

        encontrados = [
            v for v in self.servicio.obtener_visitantes()
            if v.cedula == cedula
        ]

        if not encontrados:
            messagebox.showinfo("Info", "No encontrado")
            self.actualizar_tabla()
            return

        for v in encontrados:
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def seleccionar_fila(self, event):
        """
        Cuando seleccionas una fila:
        ✔ Carga datos en el formulario
        ✔ Permite editar fácilmente
        """
        seleccion = self.tree.selection()

        if seleccion:
            item = self.tree.item(seleccion)
            datos = item["values"]

            self.entry_cedula.delete(0, tk.END)
            self.entry_cedula.insert(0, datos[0])

            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, datos[1])

            self.entry_motivo.delete(0, tk.END)
            self.entry_motivo.insert(0, datos[2])

    def actualizar_tabla(self):
        """
        Recarga la tabla
        """
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for v in self.servicio.obtener_visitantes():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def limpiar(self):
        """
        Limpia todos los campos
        """
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
        self.entry_buscar.delete(0, tk.END)