print("=============================================")
print("      Bienvenido a la Calculadora Python")
print("=============================================")
print("Instrucciones:")
print("1. Ingresa un número (puedes usar decimales).")
print("2. Escribe la operación: suma, resta, multi o div.")
print("3. Ingresa el segundo número.")
print('4. Escribe "salir" en cualquier momento para terminar.')
print("=============================================\n")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese primer número: ")
        if resultado.lower() == "salir":
            break
        try:
            resultado = float(resultado)
        except ValueError:
            print(f"'{resultado}': Valor no válido")
            resultado = ""
        continue

    op = input("ingrese operación (suma, resta, multi, div): ")
    if op.lower() == "salir":
        break
    if op.lower() not in ("suma", "resta", "multi", "div"):
        print("Operación no valida usa: suma, resta, multi, div")
        continue

    while True:
        n2 = input("Ingrese segundo número: ")
        if n2.lower() == "salir":
            break
        try:
            n2 = float(n2)
            break
        except ValueError:
            print(f"'{n2}': Valor no válido")

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2

    else:
        print("Error de usuario")

    print(f"El resultado es: {resultado}")
