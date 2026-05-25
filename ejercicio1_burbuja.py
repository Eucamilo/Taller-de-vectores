"""
Ejercicio 1: Ordenamiento de arreglo usando método burbuja (mayor a menor).
Taller: Vectores y matrices
"""


def generar_arreglo(n):
    arreglo = []
    print(f"\nIngresa {n} números:")
    for i in range(n):
        while True:
            try:
                elemento = float(input(f"  Elemento [{i + 1}]: "))
                arreglo.append(elemento)
                break
            except ValueError:
                print("  ⚠ Por favor ingresa un número válido.")
    return arreglo


def ordenar_burbuja(arreglo):
    arr = arreglo.copy()
    n = len(arr)

    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break

    return arr


def main():
    print("=" * 45)
    print("   ORDENAMIENTO BURBUJA - Mayor a Menor")
    print("=" * 45)

    while True:
        try:
            n = int(input("\n¿Cuántos elementos tendrá el arreglo? "))
            if n <= 0:
                print("⚠ El número debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("⚠ Ingresa un número entero válido.")

    arreglo_original = generar_arreglo(n)
    arreglo_ordenado = ordenar_burbuja(arreglo_original)

    print("\n--- Resultado ---")
    print(f"Arreglo original: {arreglo_original}")
    print(f"Arreglo ordenado: {arreglo_ordenado}")
    print("=" * 45)


if __name__ == "__main__":
    main()