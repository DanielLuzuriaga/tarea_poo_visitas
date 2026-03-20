# 🖥️ Sistema de Registro de Visitantes

## 📌 Descripción del Proyecto

Mi proyecto consiste en una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. El sistema permite gestionar el registro de visitantes de una oficina mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), aplicando una arquitectura modular por capas.

---

## 🎯 Objetivo

Desarrollar una aplicación que permita registrar, visualizar, editar y eliminar visitantes, separando correctamente la lógica del sistema y la interfaz gráfica, siguiendo buenas prácticas de Programación Orientada a Objetos (POO).

---

## 🧠 Arquitectura del Sistema

El proyecto está estructurado en capas para mantener una correcta organización:

* **Modelos:** Representan la estructura de los datos (Visitante).
* **Servicios:** Contienen la lógica del sistema (CRUD y persistencia).
* **UI (Interfaz Gráfica):** Maneja la interacción con el usuario.
* **Main:** Punto de entrada de la aplicación.

---

## 📁 Estructura del Proyecto

```
tarea_poo_visitas/
│
├── main.py
├── visitantes.json
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py
```

---

## ⚙️ Funcionalidades

Mi aplicación permite:

✔ Registrar nuevos visitantes
✔ Validar campos obligatorios
✔ Evitar cédulas duplicadas
✔ Visualizar visitantes en tabla
✔ Buscar visitante por cédula
✔ Editar información de visitantes
✔ Eliminar registros con confirmación
✔ Limpiar campos del formulario
✔ Persistencia de datos en archivo JSON

💾 Persistencia de Datos

El sistema utiliza un archivo visitantes.json para almacenar la información de los visitantes. Esto permite que los datos se mantengan incluso después de cerrar la aplicación.

🖥️ Interfaz Gráfica

La interfaz fue desarrollada con Tkinter e incluye:
-Formulario de ingreso de datos
-Botones de acción (Registrar, Editar, Eliminar, Limpiar)
-Buscador por cédula
-Tabla dinámica (Treeview)
-Mensajes de validación (messagebox)
-Encabezado institucional

🚀 Ejecución del Proyecto

Abrir la terminal en la carpeta del proyecto

Ejecutar el siguiente comando: python main.py

🛠️ Tecnologías Utilizadas

Python

-Tkinter (Interfaz gráfica)
-JSON (Almacenamiento de datos)

🧪 Ejemplo de Uso

-Ingresar datos del visitante
-Presionar "Registrar"
-Visualizar en la tabla
-Seleccionar para editar o eliminar
-Buscar por cédula

👨‍💻 Autor

Daniel Luzuriaga
Universidad Estatal Amazónica

🏆 Conclusión

Podemos concluir que el presente proyecto demuestra la aplicación de conceptos fundamentales de programación como la Programación Orientada a Objetos, arquitectura por capas, encapsulamiento, validaciones y persistencia de datos, logrando un sistema funcional y estructurado.
