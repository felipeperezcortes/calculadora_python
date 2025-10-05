# Calculadora en Python

Calculadora básica desarrollada por **Felipe Pérez** como práctica de fundamentos de programación en Python.  
Incluye manejo de errores, soporte para decimales y permite escribir `salir` en cualquier momento para finalizar el programa.

---

## Características

- Operaciones disponibles: **suma**, **resta**, **multiplicación** y **división**  
- Admite números enteros y decimales (`float`)  
- Permite escribir `salir` en cualquier momento para cerrar el programa  
- Controla errores comunes:  
  - Entrada inválida (`ValueError`)  
  - División por cero (`ZeroDivisionError`)  
- Estructura de bucles anidados y uso de `try/except` para validaciones seguras  
- Mensajes claros e instrucciones en consola  

---

## Uso

1. Ejecuta el programa en tu terminal o en Visual Studio Code:
```
python calculadora1.py
```
2. Verás un mensaje de bienvenida:
```
=============================================
      Bienvenido a la Calculadora Python
=============================================
Instrucciones:
1. Ingresa un número (puedes usar decimales).
2. Escribe la operación: suma, resta, multi o div.
3. Ingresa el segundo número.
4. Escribe "salir" en cualquier momento para terminar.
=============================================

```
3. Ejemplo de ejecución:
```
Ingrese primer número: 5
Ingrese operación: multi
Ingrese segundo número: 3
El resultado es: 15.0

```
4. El programa seguirá ejecutándose hasta que escribas salir.

---

## Explicación técnica

El proyecto utiliza:

-	Estructuras de control: while, if, elif, else
- Conversión de tipos: float() para admitir números decimales
- Manejo de errores: bloques try y except para evitar fallos por entradas inválidas
- Control de flujo: uso de continue y break
- Bucles anidados: para validar el segundo número antes de continuar la operación

Flujo general del programa:

1.	Se pide el primer número (permite “salir”).
2.	Se solicita la operación y se valida.
3.	Se pide el segundo número hasta que sea válido.
4.	Se ejecuta la operación correspondiente.
5.	Se imprime el resultado y el ciclo se repite.

---

👨‍💻 Autor

Felipe Pérez
Desarrollador autodidacta en proceso de formación en Python y DevOps.
Este proyecto forma parte de su ruta de aprendizaje para consolidar fundamentos de programación.

📍 La Serena, Chile
