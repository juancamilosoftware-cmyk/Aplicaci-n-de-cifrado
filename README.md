# Cifrado de seis dígitos

Proyecto académico individual en Python 3 y Tkinter, sin dependencias externas.

## Ejecutar

1. Descomprima el proyecto.
2. Instale Python 3 con Tcl/Tk (incluido habitualmente en el instalador oficial para Windows).
3. Abra una terminal dentro de `proyecto_cifrado`.
4. Ejecute `python app.py`. En Windows también puede usar `py app.py`.

Si aparece un error relacionado con tkinter, revise que su instalación de Python incluya Tcl/Tk. Puede comprobarlo con `python -m tkinter`.

Cambie las constantes ESTUDIANTE, ASIGNATURA, INSTITUCION y FECHA en `configuracion.py` y los campos de la portada del informe. Se conservaron los campos entre corchetes porque no se proporcionaron esos datos.

## Uso

Desde la ventana principal abra Cifrado o Descifrado. Ingrese seis dígitos y pulse el botón correspondiente o Enter. Limpiar borra la entrada y la salida; Cerrar cierra solamente la ventana secundaria; Salir termina la aplicación. Abrir nuevamente una ventana existente la trae al frente. Se permiten espacios exteriores; los interiores se rechazan. La salida siempre es texto, por lo que `018932` conserva su cero inicial.


## Archivos

```text
proyecto_cifrado/
  app.py
  configuracion.py
  presentacion/
    __init__.py
    ventanas.py
  servicios/
    __init__.py
    servicio_cifrado.py
  dominio/
    __init__.py
    algoritmos.py
  tests/
    test_algoritmos.py
    test_servicios.py
  verificar_interfaz.py
  README.md
  informe_funcionalidad.md
  pruebas_resultados.txt
  gui_resultados.txt
  gui_errores.txt
  capturas/INSTRUCCIONES.md
```

## Guía para comprender el código

`dominio/algoritmos.py` contiene las reglas. `validar_entrada` retorna una cadena válida o lanza `ValueError`. Se comprueba cada carácter contra `0123456789`; `isdigit()` aceptaría otros caracteres numéricos que el enunciado excluye. `cifrar` transforma los dígitos y construye la salida siguiendo ORDEN. `descifrar` reordena y resta 7 módulo 10. Las funciones retornan cadenas, nunca un número de seis dígitos convertido a entero.

`presentacion/ventanas.py` contiene `Aplicacion`, que organiza los controles mediante `grid`. Cada botón recibe una función en `command`; esa función se ejecuta al pulsarlo. `StringVar` actualiza la etiqueta del resultado. El diccionario `ventanas` conserva referencias a los Toplevel y `winfo_exists()` comprueba si siguen abiertos. `main()` crea la única raíz Tk y el único mainloop de la aplicación.

## Inconsistencia del segundo caso

Con el algoritmo indicado, `791658 → 834652 → 791658`. El resultado `835682` solicitado en el enunciado se descifra como `891651`. El informe explica los cálculos. No se introdujo una excepción para forzar un resultado incompatible con el algoritmo.

Este cifrado es un ejercicio académico y no proporciona seguridad criptográfica para datos reales.

## Arquitectura por capas

El flujo es: presentación → servicios → dominio.

- Presentación: recibe lo escrito, muestra resultados y comunica errores mediante Tkinter.
- Servicios: expone los casos de uso cifrar y descifrar; conecta la interfaz con las reglas.
- Dominio: valida y transforma las cadenas; no importa Tkinter ni conoce ventanas.

`app.py` conecta los componentes y contiene el único mainloop. `configuracion.py` conserva los datos editables. No se requiere una capa de persistencia porque el proyecto no almacena información en archivos ni bases de datos. La capa de dominio puede probarse sin abrir la interfaz.

Los registros GUI corresponden a la versión anterior a la reorganización. En la versión por capas se volvieron a ejecutar las pruebas de dominio y servicios y se comprobó la importación de la presentación; no se repitió la sesión gráfica.
