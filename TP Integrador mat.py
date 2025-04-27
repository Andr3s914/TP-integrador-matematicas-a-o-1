def decimal_a_binario(n):
    """Convierte un número decimal a binario."""
    # Verifica que el número sea positivo
    if n < 0:
        return "Error: Introduzca un número entero positivo."
    # Convierte el número decimal a binario usando bin() y elimina el prefijo '0b'
    return bin(n)[2:]

def binario_a_decimal(b):
    """Convierte un número binario a decimal."""
    # Verifica que el input contenga solo caracteres '0' o '1'
    if not all(digito in "01" for digito in b):
        return "Error: Introduzca un número binario válido."
    # Convierte la cadena binaria a decimal usando int(base 2)
    return int(b, 2)

def main():
    """Función principal que gestiona la interacción con el usuario."""
    print("Conversor de números")
    print("1: Decimal a Binario")
    print("2: Binario a Decimal")
    
    # Solicita al usuario que seleccione una opción
    opcion = input("Seleccione una opción (1/2): ")
    
    if opcion == "1":
        # Maneja la conversión de decimal a binario
        try:
            num = int(input("Ingrese un número decimal: "))
            print("Resultado en binario:", decimal_a_binario(num))
        except ValueError:
            # Captura errores si el input no es un número entero
            print("Error: Introduzca un número entero válido.")
    
    elif opcion == "2":
        # Maneja la conversión de binario a decimal
        num = input("Ingrese un número binario: ")
        print("Resultado en decimal:", binario_a_decimal(num))
    
    else:
        # Maneja una opción inválida
        print("Error: Opción no válida.")

# Ejecuta la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
