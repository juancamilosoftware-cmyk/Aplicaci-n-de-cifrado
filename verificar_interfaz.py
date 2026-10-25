"""Comprobación adicional con ventanas reales; requiere escritorio gráfico.

Deja las tres ventanas abiertas para que el estudiante pueda capturarlas.
"""
import tkinter as tk
from tkinter import ttk
from presentacion.ventanas import Aplicacion


def main():
    raiz = tk.Tk()
    aplicacion = Aplicacion(raiz)
    raiz.geometry("+30+40")

    def controles(modo):
        aplicacion.abrir(modo)
        ventana = aplicacion.ventanas[modo]
        marco = ventana.winfo_children()[0]
        entrada = next(w for w in marco.winfo_children() if isinstance(w, ttk.Entry))
        botones = [w for w in marco.winfo_children() if isinstance(w, ttk.Button)]
        salida = marco.winfo_children()[-1]
        return ventana, entrada, botones, salida

    def comprobar():
        cifrado, entrada_c, botones_c, salida_c = controles("cifrado")
        descifrado, entrada_d, botones_d, salida_d = controles("descifrado")
        for original, esperado in [("791658", "834652"), ("000123", "787709"), ("123456", "018932")]:
            botones_c[1].invoke()
            entrada_c.insert(0, original)
            botones_c[0].invoke()
            assert salida_c.cget("text") == esperado
            botones_d[1].invoke()
            entrada_d.insert(0, esperado)
            botones_d[0].invoke()
            assert salida_d.cget("text") == original
            print(f"GUI: {original} -> {esperado} -> {original}: OK", flush=True)
        for modo in ("cifrado", "descifrado"):
            anterior = aplicacion.ventanas[modo]
            aplicacion.abrir(modo)
            assert aplicacion.ventanas[modo] is anterior
        print("GUI: reutilización de ventanas: OK", flush=True)
        cifrado.geometry("+600+40")
        descifrado.geometry("+600+450")

    raiz.after(200, comprobar)
    raiz.mainloop()


if __name__ == "__main__":
    main()
