"""Capa de presentación: ventanas, controles y mensajes al usuario."""
import tkinter as tk
from tkinter import messagebox, ttk

from servicios.servicio_cifrado import ServicioCifrado
from configuracion import ESTUDIANTE, ASIGNATURA, INSTITUCION, FECHA


class Aplicacion:
    def __init__(self, raiz, servicio=None):
        self.raiz = raiz
        self.servicio = servicio if servicio is not None else ServicioCifrado()
        self.ventanas = {}
        raiz.title("Cifrado de seis dígitos")
        raiz.resizable(False, False)
        estilo = ttk.Style(raiz)
        estilo.configure("TLabel", font=("Segoe UI", 11))
        estilo.configure("TButton", font=("Segoe UI", 11), padding=7)
        estilo.configure("Titulo.TLabel", font=("Segoe UI", 19, "bold"))
        marco = ttk.Frame(raiz, padding=28)
        marco.grid(sticky="nsew")
        ttk.Label(marco, text="Cifrado de seis dígitos", style="Titulo.TLabel").grid(row=0, column=0, pady=(0, 18))
        datos = f"Estudiante: {ESTUDIANTE}\nAsignatura: {ASIGNATURA}\nInstitución: {INSTITUCION}\nFecha: {FECHA}"
        ttk.Label(marco, text=datos, justify="left").grid(row=1, column=0, sticky="w", pady=10)
        ttk.Button(marco, text="Abrir cifrado", command=lambda: self.abrir("cifrado")).grid(row=2, column=0, sticky="ew", pady=5)
        ttk.Button(marco, text="Abrir descifrado", command=lambda: self.abrir("descifrado")).grid(row=3, column=0, sticky="ew", pady=5)
        ttk.Button(marco, text="Salir", command=raiz.destroy).grid(row=4, column=0, sticky="ew", pady=5)

    def abrir(self, modo):
        existente = self.ventanas.get(modo)
        if existente is not None and existente.winfo_exists():
            existente.deiconify()
            existente.lift()
            existente.focus_force()
            return
        ventana = tk.Toplevel(self.raiz)
        self.ventanas[modo] = ventana
        es_cifrado = modo == "cifrado"
        accion = "Cifrar" if es_cifrado else "Descifrar"
        ventana.title("Cifrado" if es_cifrado else "Descifrado")
        ventana.resizable(False, False)
        marco = ttk.Frame(ventana, padding=26)
        marco.grid()
        ttk.Label(marco, text=ventana.title(), style="Titulo.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 15))
        ttk.Label(marco, text="Ingrese exactamente seis dígitos (0–9):").grid(row=1, column=0, columnspan=3, sticky="w")
        entrada = ttk.Entry(marco, font=("Consolas", 20), width=22)
        entrada.grid(row=2, column=0, columnspan=3, pady=12, sticky="ew")
        resultado = tk.StringVar(value="—")

        def procesar():
            try:
                operacion = self.servicio.cifrar if es_cifrado else self.servicio.descifrar
                valor = operacion(entrada.get())
            except ValueError as error:
                resultado.set("—")  # Evita dejar un resultado anterior ante un error.
                messagebox.showerror("Entrada incorrecta", str(error), parent=ventana)
                entrada.focus_set()
                return
            resultado.set(valor)

        def limpiar():
            entrada.delete(0, tk.END)
            resultado.set("—")
            entrada.focus_set()

        ttk.Button(marco, text=accion, command=procesar).grid(row=3, column=0, padx=(0, 5))
        ttk.Button(marco, text="Limpiar", command=limpiar).grid(row=3, column=1, padx=5)
        ttk.Button(marco, text="Cerrar", command=ventana.destroy).grid(row=3, column=2, padx=(5, 0))
        ttk.Label(marco, text="Secuencia cifrada:" if es_cifrado else "Número original:").grid(row=4, column=0, columnspan=3, sticky="w", pady=(20, 4))
        ttk.Label(marco, textvariable=resultado, font=("Consolas", 26, "bold")).grid(row=5, column=0, columnspan=3)
        ventana.bind("<Return>", lambda evento: procesar())
        entrada.focus_set()


