def decimal_a_binario(n):
    """Convierte un número decimal a binario."""
    if n < 0:
        return "Error: Introduzca un número entero positivo."
    return bin(n)[2:]

def binario_a_decimal(b):
    """Convierte un número binario a decimal."""
    if not all(digito in "01" for digito in b):
        return "Error: Introduzca un número binario válido."
    return int(b, 2)

def main():
    print("Conversor de números")
    print("1: Decimal a Binario")
    print("2: Binario a Decimal")
    
    opcion = input("Seleccione una opción (1/2): ")
    
    if opcion == "1":
        try:
            num = int(input("Ingrese un número decimal: "))
            print("Resultado en binario:", decimal_a_binario(num))
        except ValueError:
            print("Error: Introduzca un número entero válido.")
    
    elif opcion == "2":
        num = input("Ingrese un número binario: ")
        print("Resultado en decimal:", binario_a_decimal(num))
    
    else:
        print("Error: Opción no válida.")

if __name__ == "__main__":
    main()