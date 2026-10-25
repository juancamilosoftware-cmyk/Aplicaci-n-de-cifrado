# Informe de funcionalidad: cifrado y descifrado de seis dígitos

## Portada

**Título:** Aplicación de escritorio para cifrar y descifrar números de seis dígitos  
**Estudiante:** [NOMBRE COMPLETO]  
**Asignatura:** [ASIGNATURA]  
**Institución:** [INSTITUCIÓN]  
**Fecha:** [FECHA]

## Introducción

La aplicación permite practicar la transformación reversible de datos y la construcción de interfaces con Python y Tkinter. En un contexto de transmisión de datos, el emisor transforma una secuencia y el receptor aplica el procedimiento inverso para recuperarla. Este ejercicio ilustra esa idea mediante operaciones aritméticas y cambios de posición; no implementa transmisión por red.

Los objetivos son separar la lógica de la interfaz, validar las entradas, conservar ceros iniciales y verificar que el descifrado recupere el texto original. El algoritmo es académico y no proporciona seguridad criptográfica: es determinista, carece de clave secreta y puede invertirse fácilmente.

## Desarrollo

### Organización

`dominio/algoritmos.py` contiene las funciones de validación, cifrado y descifrado. `servicios/servicio_cifrado.py` expone los casos de uso. `presentacion/ventanas.py` contiene la interfaz y llama a los servicios. `app.py` conecta las capas e inicia la aplicación; `configuracion.py` contiene los datos del estudiante. La dependencia sigue presentación → servicios → dominio. No se incluye persistencia porque la aplicación no almacena datos. `tests/test_algoritmos.py` contiene pruebas con unittest, incluido en Python. `verificar_interfaz.py` comprueba botones y resultados con ventanas reales. Los registros de ejecución están en `pruebas_resultados.txt` y `gui_resultados.txt`. La carpeta `capturas` contiene las instrucciones para incorporar evidencia visual pendiente.

### Algoritmo y validación

La entrada se trata como cadena. Después de quitar espacios exteriores con `strip()`, se exige longitud seis y que cada carácter pertenezca a `0123456789`. Se rechazan campo vacío, signos, letras, decimales, espacios interiores y dígitos Unicode distintos de los ASCII. Los errores se comunican mediante messagebox y se elimina cualquier resultado anterior de la etiqueta.

Para cifrar se calcula `(int(digito) + 7) % 10` para cada carácter y luego se toman las posiciones `[2, 3, 0, 1, 5, 4]`. Los intercambios corresponden a primera con tercera, segunda con cuarta y quinta con sexta. Para descifrar se aplica la misma permutación y luego `(int(digito) - 7) % 10`. Repetir cada intercambio devuelve las posiciones originales; la resta módulo 10 revierte la suma módulo 10.

### Ventanas

La ventana principal muestra el título, los datos del estudiante y los botones de cifrado, descifrado y salida. Cada ventana secundaria ofrece una entrada, un botón de operación, Limpiar, Cerrar y una etiqueta de resultado. Se usan controles ttk, una única raíz Tk, dos Toplevel como máximo y un solo mainloop. Si una secundaria ya existe, se trae al frente. Si fue cerrada, se puede crear nuevamente.

## Pruebas de funcionalidad

### Entorno y alcance de la ejecución

Se ejecutaron las pruebas con Python 3.12.14 y Tk 8.6 en Windows. El registro final de unittest muestra **8 métodos aprobados**, con subcasos para las validaciones y 10.000 secuencias de ida y vuelta, desde `000000` hasta `009999`. Antes de la reorganización por capas se ejecutó además una comprobación de interfaz que introdujo valores e invocó los botones reales mediante Tkinter: ambos casos, conservación de ceros y reutilización de ventanas pasaron. Después de la reorganización se repitieron las pruebas de dominio y se añadieron pruebas de integración de servicios, todas aprobadas. Se comprobó la importación de la presentación, sin repetir la sesión gráfica. Los registros GUI se conservan como evidencia de la versión anterior. Los errores de validación se comprobaron en las funciones; la interacción manual con los cuadros messagebox queda pendiente.

En una primera ejecución se detectó la incompatibilidad del caso 2 con el enunciado. También se corrigieron dos valores esperados mal calculados durante la preparación de las pruebas auxiliares. El algoritmo se mantuvo; el registro entregado corresponde a la ejecución final. No se afirma haber verificado exhaustivamente el millón de entradas ni haber completado la revisión manual de toda la interfaz.

### Caso 1

1. Original: `123456`.
2. Transformación por dígito: `1→8`, `2→9`, `3→0`, `4→1`, `5→2`, `6→3`.
3. Secuencia transformada: `890123`.
4. Intercambio primera/tercera: `098123`.
5. Intercambio segunda/cuarta: `018923`.
6. Intercambio quinta/sexta: **`018932`**.
7. Para descifrar, la permutación de `018932` produce `890123`.
8. Restar 7 módulo 10 produce **`123456`**.

El cero de `018932` es parte de la secuencia. Se conserva porque la salida es una cadena y se muestra mediante StringVar.

### Caso 2 y discrepancia del enunciado

1. Original: `791658`.
2. Transformación por dígito: `7→4`, `9→6`, `1→8`, `6→3`, `5→2`, `8→5`.
3. Secuencia transformada: `468325`.
4. Intercambio primera/tercera: `864325`.
5. Intercambio segunda/cuarta: `834625`.
6. Intercambio quinta/sexta: **`834652`**.
7. Para descifrar, la permutación de `834652` produce `468325`.
8. Restar 7 módulo 10 produce **`791658`**.

El enunciado propone `835682`, pero ese valor no se deriva del algoritmo. Su permutación produce `568328` y la resta módulo 10 produce **`891651`**. Por tanto, no es posible satisfacer simultáneamente ese resultado y las reglas matemáticas dadas. Se recomienda consultar esta discrepancia con el docente; aquí se conserva el algoritmo especificado.

| Caso | Original | Cifrado del enunciado | Esperado según algoritmo | Obtenido en funciones y controles GUI | Descifrado obtenido |
|---|---|---|---|---|---|
| 1 | `123456` | `018932` | `018932` | `018932` | `123456` |
| 2 | `791658` | `835682` | `834652` | `834652` | `791658` |

La evidencia de ejecución está en `pruebas_resultados.txt` y `gui_resultados.txt`; las capturas no se obtuvieron.

### Validaciones y ceros iniciales

En cada entrada incorrecta se probaron **ambas funciones**, esperando ValueError y obteniendo ValueError.

| Comprobación | Entrada | Esperado | Obtenido |
|---|---|---|---|
| Campo vacío | cadena vacía | Rechazar | Rechazado |
| Menos de seis dígitos | `12345` | Rechazar | Rechazado |
| Más de seis dígitos | `1234567` | Rechazar | Rechazado |
| Letras | `12a456` | Rechazar | Rechazado |
| Negativo | `-12345` | Rechazar | Rechazado |
| Decimal | `123.45` | Rechazar | Rechazado |
| Espacio interior | `12 345` | Rechazar | Rechazado |
| Dígitos no ASCII | `１２３４５６`, `١٢٣٤٥٦` | Rechazar | Rechazados |
| Espacios exteriores | ` 123456 ` | `018932` al cifrar | `018932` |
| Cero en salida cifrada | `123456` | `018932` | `018932`, también en control GUI |
| Ceros en original | `000123` | Cifrar `787709`, recuperar `000123` | Ambos resultados comprobados, también en controles GUI |

### Evidencia visual pendiente

La captura de ventanas falló con el mensaje `foreground window did not report a process id`. El intento de recuperación ya no detectó las ventanas del proyecto. No se generaron capturas ni se sustituyeron por simulaciones. Siga `capturas/INSTRUCCIONES.md` para añadirlas.

- **[INSERTAR CAPTURA 1]** Ventana principal completa: `capturas/01_principal.png`.
- **[INSERTAR CAPTURA 2]** Ventana de cifrado, caso 1: entrada `123456`, resultado `018932`.
- **[INSERTAR CAPTURA 3]** Ventana de descifrado, caso 1: entrada `018932`, resultado `123456`.
- **[INSERTAR CAPTURA 4]** Ventana de cifrado, caso 2: entrada `791658`, resultado `834652`.
- **[INSERTAR CAPTURA 5]** Ventana de descifrado, caso 2: entrada `834652`, resultado `791658`.

### Revisión manual pendiente

| Acción | Resultado esperado | Estado |
|---|---|---|
| Enviar una entrada inválida en cada ventana | Cuadro de error comprensible y resultado anterior borrado | Pendiente de comprobación visual |
| Pulsar Limpiar | Entrada vacía, salida `—`, foco en entrada | Borrado usado en comprobación GUI; foco pendiente de revisión visual |
| Pulsar Cerrar y volver a abrir | Se cierra la secundaria y puede abrirse otra vez | Pendiente |
| Abrir dos veces la misma secundaria | Se reutiliza la existente | Comprobado por identidad del objeto GUI |
| Pulsar Salir | Se cierra toda la aplicación | Pendiente |
| Revisar tamaño, legibilidad y navegación | Controles visibles y utilizables | Pendiente de revisión visual |

## Conclusión

**Propuesta de reflexión para adaptar a la experiencia real del estudiante:**

«Este proyecto me permitió practicar [explicar lo aprendido realmente] y relacionar las funciones de Python con los eventos de una interfaz. La conservación de los ceros iniciales muestra por qué conviene trabajar con cadenas en este problema. Al comparar los resultados esperados con los calculados identifiqué [describir la revisión realizada y la discrepancia del segundo caso]. La dificultad que encontré fue [dificultad real] y la abordé mediante [acción real]. Como mejora propondría [mejora justificada]. Antes de entregar, completé [indicar únicamente las pruebas y capturas que realmente se realizaron].»

Esta reflexión es una propuesta, no una afirmación sobre la experiencia personal del estudiante.

