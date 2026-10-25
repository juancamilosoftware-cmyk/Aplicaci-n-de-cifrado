"""Punto de entrada: conecta las capas y arranca la aplicación."""
import tkinter as tk
from presentacion.ventanas import Aplicacion
from servicios.servicio_cifrado import ServicioCifrado


def main():
    raiz = tk.Tk()
    Aplicacion(raiz, ServicioCifrado())
    raiz.mainloop()


if __name__ == "__main__":
    main()
